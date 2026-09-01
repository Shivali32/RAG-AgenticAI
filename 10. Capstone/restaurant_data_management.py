from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional
import json
import os
import shutil
import io
import unittest
from unittest.mock import patch


# ============================================================
# FILE PATHS
# ============================================================

FILEPATH = 'structured_restaurant_data.json'
BACKUP_PATH = 'structured_restaurant_data.json.bak'

EXAMPLE_RESTAURANT_PARAGRAPH = (
    'Down in **Santa Monica**, **Mar de Cortez** serves as a '
    '**sun-drenched**, **casual taqueria** specializing in '
    '**Baja-style seafood**. With a **4.2/5** rating, it captures '
    'the salt-air energy of the coast through its signature '
    'beer-battered snapper tacos and zesty octopus ceviche, making '
    'it a premier spot for open-air dining near the pier. '
    'Price range: $'
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_data(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_data(data, file_path, backup_path):
    # Create a backup before writing
    if os.path.exists(file_path):
        shutil.copy(file_path, backup_path)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def show_restaurant_card(res, index):
    """Displays restaurant data in a clean, vertical format."""

    print(f"\n{'=' * 15} RESTAURANT #{index} {'=' * 15}")

    # Prioritize 'name' if it exists, otherwise use 'restaurant_name'
    name = res.get(
        'name',
        res.get('restaurant_name', 'Unnamed Restaurant')
    )

    print(f"NAME        : {name}")

    for key, value in res.items():
        if key.lower() not in ['name', 'restaurant_name']:
            label = key.replace('_', ' ').upper()
            print(f"{label:<12}: {value}")

    print('=' * 45)


# ============================================================
# PYDANTIC RESTAURANT SCHEMA
# ============================================================

class Restaurant(BaseModel):
    """The restaurant pydantic schema used in lesson 1."""

    name: str
    location: str
    type: str
    food_style: str
    rating: Optional[float] = None
    price_range: Optional[int] = None
    signatures: List[str] = Field(default_factory=list)
    vibe: Optional[str] = None
    environment: str
    shortcomings: List[str] = Field(default_factory=list)


# ============================================================
# EXERCISE 1
# INTEGRATE THE LLM MODEL
# ============================================================

def restaurant_data_structure_prompt_generation(restaurant_paragraph):

    system_msg = (
        "You are a restaurant data extraction assistant. "
        "Your task is to convert restaurant descriptions into "
        "structured JSON data. Return only valid JSON and no "
        "additional explanation."
    )

    prompt_txt = f"""
Convert the following restaurant description into JSON.

The JSON must contain exactly these fields:

name
location
type
food_style
rating
price_range
signatures
vibe
environment
shortcomings

Rules:

1. name must be a string.
2. location must be a string. If unavailable, use "Unknown".
3. type must describe the restaurant type.
4. food_style must describe the cuisine or food style.
5. rating must be a number or null.
6. price_range must be an integer:
   $ = 1
   $$ = 2
   $$$ = 3
   $$$$ = 4
7. signatures must be a JSON list of signature dishes.
8. vibe may be a string or null.
9. environment must be a string. If unavailable, use "Unknown".
10. shortcomings must be a JSON list.
11. Do not include Markdown code blocks.
12. Do not include comments or explanations.
13. Return only one valid JSON object.

Restaurant description:

{restaurant_paragraph}
"""

    return system_msg, prompt_txt


def llm_model(system_msg, prompt_txt, params=None):

    if params is None:
        params = {
            "max_tokens": 800,
            "temperature": 0
        }

    credentials = Credentials(
        url="https://us-south.ml.cloud.ibm.com"
    )

    model = ModelInference(
        model_id="mistralai/mistral-small-3-1-24b-instruct-2503",
        # model_id="ibm/granite-3-8b-instruct",
        credentials=credentials,
        project_id="skills-network",
        params=params
    )

    messages = [
        {
            "role": "system",
            "content": system_msg
        },
        {
            "role": "user",
            "content": prompt_txt
        }
    ]

    response = model.chat(messages=messages)

    return response["choices"][0]["message"]["content"]


def JSON_auto_repair_prompts(response, error_message):

    system_msg = (
        "You are a JSON repair assistant. "
        "Fix invalid JSON so that it matches the required restaurant "
        "schema. Return only the corrected JSON object."
    )

    prompt_txt = f"""
The following restaurant JSON could not be parsed or validated.

Invalid response:

{response}

Error:

{error_message}

Repair the response.

The corrected JSON must contain:

name: string
location: string
type: string
food_style: string
rating: number or null
price_range: integer or null
signatures: list of strings
vibe: string or null
environment: string
shortcomings: list of strings

Return ONLY valid JSON.
Do not use Markdown code blocks.
Do not provide any explanation.
"""

    return system_msg, prompt_txt


def clean_json_response(response):
    """Remove common Markdown formatting around JSON."""

    response = response.strip()

    if response.startswith("```json"):
        response = response[7:]

    elif response.startswith("```"):
        response = response[3:]

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    # Extract the JSON object if the model added extra text
    start = response.find("{")
    end = response.rfind("}")

    if start != -1 and end != -1:
        response = response[start:end + 1]

    return response


def new_data_entry_process(paragraph, itemId):

    # Generate the original prompts
    system_msg, prompt_txt = (
        restaurant_data_structure_prompt_generation(paragraph)
    )

    # Get structured data from the LLM
    response = llm_model(
        system_msg,
        prompt_txt
    )

    # Try parsing and validating the response
    for attempt in range(3):

        try:
            cleaned_response = clean_json_response(response)

            restaurant_dict = json.loads(cleaned_response)

            validated_restaurant = Restaurant.model_validate(
                restaurant_dict
            )

            structured_data = validated_restaurant.model_dump()

            # Add the supplied item ID
            structured_data = {
                "id": itemId,
                **structured_data
            }

            return structured_data

        except (json.JSONDecodeError, ValidationError, TypeError) as e:

            if attempt == 2:
                raise ValueError(
                    f"Unable to create valid restaurant data: {e}"
                )

            repair_system_msg, repair_prompt_txt = (
                JSON_auto_repair_prompts(
                    response,
                    str(e)
                )
            )

            response = llm_model(
                repair_system_msg,
                repair_prompt_txt
            )


# ============================================================
# EXERCISE 2
# MAIN COMMAND-LINE UI
# ============================================================

def manage_restaurants(file_path, backup_path):

    while True:

        data = load_data(file_path)

        print(
            f"\n🏨 RESTAURANT DATABASE | Records: {len(data)}"
        )

        print("1. Browse All (Names)")
        print("2. View Detailed Record")
        print("3. Add New Restaurant")
        print("4. Edit Restaurant Info")
        print("5. Delete Restaurant")
        print("6. Exit")

        choice = input("\nAction: ")


        # ----------------------------------------------------
        # OPTION 1: BROWSE RESTAURANTS
        # ----------------------------------------------------

        if choice == '1':

            print("\n--- Current Listings ---")

            for index, restaurant in enumerate(data):

                name = restaurant.get('name', 'N/A')

                print(
                    f"{index}: {name}"
                )


        # ----------------------------------------------------
        # OPTION 2: VIEW RESTAURANT DETAILS
        # ----------------------------------------------------

        elif choice == '2':

            try:

                index = int(
                    input("Enter record index: ")
                )

                if 0 <= index < len(data):

                    show_restaurant_card(
                        data[index],
                        index
                    )

                else:
                    print("invalid index.")

            except (ValueError, TypeError):
                print("invalid index.")


        # ----------------------------------------------------
        # OPTIONS THAT MODIFY THE DATABASE
        # ----------------------------------------------------

        elif choice in ['3', '4', '5']:

            # Strict Security Warning

            print(
                "\n❗ SECURITY WARNING: "
                "You are entering write-mode."
            )

            print(
                "Changes will be saved to the "
                "database immediately."
            )

            confirm = input(
                "Are you sure? (type 'yes' to proceed): "
            ).lower()

            if confirm != 'yes':

                print("Operation cancelled.")

                continue


            # ------------------------------------------------
            # OPTION 3: ADD NEW RESTAURANT
            # ------------------------------------------------

            if choice == '3':

                itemId = 1000000 + len(data) + 1

                paragraph = input(
                    "Enter the new restaurant description: "
                )

                new_restaurant = new_data_entry_process(
                    paragraph,
                    itemId
                )

                data.append(
                    new_restaurant
                )

                save_data(
                    data,
                    file_path,
                    backup_path
                )

                print("✅ Restaurant added.")


            # ------------------------------------------------
            # OPTION 4: EDIT RESTAURANT
            # ------------------------------------------------

            elif choice == '4':

                try:

                    index = int(
                        input("Enter record index: ")
                    )

                    if 0 <= index < len(data):

                        current_record = data[index]

                        print(
                            "\nPress Enter without typing "
                            "anything to keep the current value."
                        )

                        for key in list(current_record.keys()):

                            current_value = current_record[key]

                            new_value = input(
                                f"{key} [{current_value}]: "
                            )

                            if new_value.strip() == "":
                                continue


                            # Preserve list values
                            if isinstance(current_value, list):

                                try:

                                    parsed_value = json.loads(
                                        new_value
                                    )

                                    if isinstance(
                                        parsed_value,
                                        list
                                    ):
                                        current_record[key] = (
                                            parsed_value
                                        )

                                    else:
                                        current_record[key] = [
                                            item.strip()
                                            for item
                                            in new_value.split(',')
                                        ]

                                except json.JSONDecodeError:

                                    current_record[key] = [
                                        item.strip()
                                        for item
                                        in new_value.split(',')
                                    ]


                            # Preserve integer values
                            elif (
                                isinstance(current_value, int)
                                and
                                not isinstance(
                                    current_value,
                                    bool
                                )
                            ):

                                try:
                                    current_record[key] = int(
                                        new_value
                                    )

                                except ValueError:
                                    print(
                                        f"Invalid integer for "
                                        f"{key}. Value unchanged."
                                    )


                            # Preserve floating point values
                            elif isinstance(
                                current_value,
                                float
                            ):

                                try:
                                    current_record[key] = float(
                                        new_value
                                    )

                                except ValueError:
                                    print(
                                        f"Invalid number for "
                                        f"{key}. Value unchanged."
                                    )


                            # Handle known numeric fields that
                            # currently contain None
                            elif (
                                current_value is None
                                and key == 'rating'
                            ):

                                try:
                                    current_record[key] = float(
                                        new_value
                                    )

                                except ValueError:
                                    print(
                                        "Invalid rating. "
                                        "Value unchanged."
                                    )


                            elif (
                                current_value is None
                                and key == 'price_range'
                            ):

                                try:
                                    current_record[key] = int(
                                        new_value
                                    )

                                except ValueError:
                                    print(
                                        "Invalid price range. "
                                        "Value unchanged."
                                    )


                            # Strings and other values
                            else:

                                current_record[key] = new_value


                        save_data(
                            data,
                            file_path,
                            backup_path
                        )

                        print("✅ Record updated.")

                    else:
                        print("invalid index.")

                except (ValueError, TypeError):

                    print("invalid index.")


            # ------------------------------------------------
            # OPTION 5: DELETE RESTAURANT
            # ------------------------------------------------

            elif choice == '5':

                try:

                    index = int(
                        input("Enter record index: ")
                    )

                    if 0 <= index < len(data):

                        data.pop(index)

                        save_data(
                            data,
                            file_path,
                            backup_path
                        )

                        print("✅ Restaurant deleted.")

                    else:
                        print("invalid index.")

                except (ValueError, TypeError):

                    print("invalid index.")


        # ----------------------------------------------------
        # OPTION 6: EXIT
        # ----------------------------------------------------

        elif choice == '6':

            break


        # ----------------------------------------------------
        # INVALID MENU INPUT
        # ----------------------------------------------------

        else:

            print("Invalid input.")


# ============================================================
# EXERCISE 3
# UNIT TESTS
# ============================================================

class TestRestaurantDatabase(unittest.TestCase):

    def setUp(self):
        """Create a temporary clean database for testing."""

        self.test_file = (
            'structured_restaurant_data_unit_test.json'
        )

        self.test_file_backup = (
            'structured_restaurant_data_unit_test.json.bak'
        )

        self.initial_data = [
            {
                "name": "Test Cafe",
                "location": "Test City"
            }
        ]

        with open(self.test_file, 'w') as f:
            json.dump(
                self.initial_data,
                f
            )


    def tearDown(self):
        """Clean up the test files after tests."""

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        if os.path.exists(self.test_file_backup):
            os.remove(self.test_file_backup)


    @patch('builtins.input')
    @patch(
        'sys.stdout',
        new_callable=io.StringIO
    )
    def test_add_and_delete_restaurant_success(
        self,
        mock_stdout,
        mock_input
    ):

        """
        Test Scenario: Add a new restaurant.

        Inputs:
        '3' = Add
        'yes' = Confirm
        restaurant paragraph
        '6' = Exit
        """

        mock_restaurant = (
            'The Copper Sprout is a high-concept, '
            'Modern Appalachian farm-to-table destination '
            'that blends an industrial-chic aesthetic with '
            'rustic forest charm, featuring reclaimed wood '
            'and amber lighting to create a sophisticated '
            'yet cozy vibe. Priced in the $$$ category, '
            'the menu celebrates seasonal foraging and local '
            'heritage, headlined by signature dishes like '
            'Cast-Iron Smoked Trout with pickled fiddlehead '
            'ferns and hand-foraged Wild Mushroom Risotto '
            'with aged goat cheese. The experience is '
            'designed to be intimate and earthy, making it '
            'a premier spot for those seeking high-quality, '
            'smokehouse-influenced cuisine in a refined, '
            'atmospheric setting.'
        )

        mock_input.side_effect = [
            '3',
            'yes',
            mock_restaurant,
            '6'
        ]

        # Run the app
        try:

            manage_restaurants(
                self.test_file,
                self.test_file_backup
            )

        except SystemExit:

            pass


        # Check if the data was saved

        with open(self.test_file, 'r') as f:
            data = json.load(f)

        print(data)

        self.assertEqual(
            len(data),
            2
        )

        self.assertIn(
            "✅ Restaurant added.",
            mock_stdout.getvalue()
        )


        # Now test deleting the newly-added restaurant

        mock_input.side_effect = [
            '5',
            'yes',
            1,
            '6'
        ]

        try:

            manage_restaurants(
                self.test_file,
                self.test_file_backup
            )

        except SystemExit:

            pass


        with open(self.test_file, 'r') as f:
            data = json.load(f)

        print(data)

        self.assertEqual(
            len(data),
            1
        )


    @patch('builtins.input')
    @patch(
        'sys.stdout',
        new_callable=io.StringIO
    )
    def test_delete_security_cancel(
        self,
        mock_stdout,
        mock_input
    ):

        """
        Test Scenario:
        Try to delete but say 'no'
        to the security warning.

        Inputs:
        '5' = Delete
        'no' = Cancel
        '6' = Exit
        """

        mock_input.side_effect = [
            '5',
            'no',
            '6'
        ]

        manage_restaurants(
            self.test_file,
            self.test_file_backup
        )


        with open(self.test_file, 'r') as f:
            data = json.load(f)


        self.assertEqual(
            len(data),
            1
        )

        self.assertIn(
            "Operation cancelled.",
            mock_stdout.getvalue()
        )


# ============================================================
# RUN UNIT TESTS
# ============================================================

if __name__ == "__main__":

    # unittest.main()
    
    manage_restaurants(FILEPATH, BACKUP_PATH)