::page{title="Lab: Build a Command-Line Data Management UI for Restaurant Data"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-WD0231EN-SkillsNetwork/IDSN-logo.png" alt="cognitiveclass.ai logo" width="200" />

Estimated time needed: **45 minutes**

## **Background**

You have mastered the art of using generative AI to transform chaotic, unstructured data, from dense paragraphs to visual imagery, into organized assets.

The app is now powered by these refined data files, but raw JSON is difficult for humans to manage at scale. To bridge this gap, your next challenge is to build a streamlined user interface that enables seamless interaction with the database.

This UI will serve as the command center for the app's knowledge, allowing users to read, edit, and update the structured files with precision and ease.

## **Objectives**

In this lab, you will develop a functional Python application designed to:

-   Build a robust interface to read from and write to your structured restaurant database on demand
    
-   Seamlessly embed generative functions to automate data processing and enrichment within your application
    
-   Apply safety protocols to manage file updates and prevent accidental data loss
    

## **Important: About the lab environment**

Please be aware that sessions for this lab environment are not persisted. Every time you connect to this lab, a new environment is created for you. Any data you may have saved in the earlier session would get lost. Plan to complete these labs in a single session, to avoid losing your data.

## **Screenshot requirement for this lab**

You will be prompted to take a screenshot and save it on your own device. You will need this screenshot either to answer graded quiz questions or to upload as your submission for the Final Project at the end of this course. You can use various free screen-grabbing tools or your operating system's shortcut keys to do this (for example, `Alt+PrintScreen` on Windows and `Command+shift+4` on Mac).
**Note**: The screenshot can be saved with either the **.jpg** or **.png** extension.

::page{title="Exercises: Define the core functions"}

## Set up the lab environment

Run the following to create a virtual environment.

```bash
python3.11 -m venv venv
source venv/bin/activate

```

Install the required packages.

```bash
pip install ibm-watsonx-ai==1.4.7 pydantic==2.12.4

```

**Important:** Upload your saved restaurant data to the folder.

In this lab, you will write codes in the python file `restaurant_data_management.py`. Click the following button to create and open the file.

&nbsp;

::openFile{path="restaurant_data_management.py"}

In this Python file, copy and paste the following code for the required packages and some pre-defined helper functions.

**Note**: After completing the **new_data_entry_process()** function in the code below, take a screenshot of your implementation and save it as **M1L3_new_data_entry_process.jpg**.
```python
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

FILEPATH = 'structured_restaurant_data.json'
BACKUP_PATH = 'structured_restaurant_data.json.bak'
EXAMPLE_RESTAURANT_PARAGRAPH = 'Down in **Santa Monica**, **Mar de Cortez** serves as a **sun-drenched**, **casual taqueria** specializing in **Baja-style seafood**. With a **4.2/5** rating, it captures the salt-air energy of the coast through its signature beer-battered snapper tacos and zesty octopus ceviche, making it a premier spot for open-air dining near the pier. Price range: $'

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
    print(f"\n{'='*15} RESTAURANT #{index} {'='*15}")
    # Prioritize 'name' if it exists, otherwise use 'id'
    name = res.get('name', res.get('restaurant_name', 'Unnamed Restaurant'))
    print(f"NAME        : {name}")
    
    for key, value in res.items():
        if key.lower() not in ['name', 'restaurant_name']:
            # Handle long descriptions by wrapping slightly
            label = key.replace('_', ' ').upper()
            print(f"{label:<12}: {value}")
    print('='*45)
	
class Restaurant(BaseModel):
	"""The restaurant pydantic scheme used in lesson 1."""
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

```

## Exercise 1: Integrate the LLM model from Lesson 1

You will need the LLMs you defined in lesson 1 to structure new restaurant paragraph inputs. In addition to these functions, you will need to implement a new function `new_data_entry_process(paragraph, itemId)`, which takes inputs:

-   `paragraph`: the new restaurant paragraph;
    
-   `itemId`: the ID of this new item.
    

This new function combines and uses the generative models you defined in lesson 1 to structure a given new restaurant paragraph.

In your `restaurant_data_management.py`, copy and paste the following code block and complete the functions.

  **Important**: Take a screenshot of your implementation of the `new_data_entry_process()` and name it `M1L3_new_data_entry_process.jpg`.

```python
#Update your restaurant_data_structure_prompt_generation
def restaurant_data_structure_prompt_generation(restaurant_paragraph):
	#YOUR CODE HERE
    pass

# Might need to explain why we are using granite here (cheap)
def llm_model(system_msg, prompt_txt, params=None):
	#YOUR CODE HERE
    pass

def JSON_auto_repair_prompts(response, error_message):
	#YOUR CODE HERE
    pass

def new_data_entry_process(paragraph, itemId):
	#YOUR CODE HERE
    pass

```

::page{title="Exercises: Implement your UI"}

## Exercise 2: The main UI function

In this exercise, you will implement the main UI function `manage_restaurants()`.

The main logic works as follow:

1.  Users first select an action from the following six options: (1) Browse the names of the restaurants in the data (2) View the detailed record (3) Add a new restaurant record (4) Edit an existing restaurant record (5) Delete a restaurant record (6) Exit
    
2.  Different actions have different responses: a. For actions (1) and (2), the interface will directly display the corresponding information. b. For actions (3), (4) and (5), security info is required to confirm with users their intent to modify the database. Then perform the requested action. c. For (6), quit the system.
    

The skeleton of the function is provided to you. You need to fill in the blanks in the code. Again, please first copy and paste the code skeleton to the `restaurant_data_management.py`, and then write inside the file.

```python
def manage_restaurants(file_path, backup_path):
    while True:
        data = load_data(file_path)
        print(f"\n🏨 RESTAURANT DATABASE | Records: {len(data)}")
        print("1. Browse All (Names)")
        print("2. View Detailed Record")
        print("3. Add New Restaurant")
        print("4. Edit Restaurant Info")
        print("5. Delete Restaurant")
        print("6. Exit")
        
        choice = input("\nAction: ")

        if choice == '1':
            print("\n--- Current Listings ---")
			# YOUR CODE HERE
			# Instruction: 
			# Iterate through the records in the data file and show their names. 
			# If name doesn't exist, print 'N/A'.
        
        elif choice == '2':
			# YOUR CODE HERE:
			# Instruction: 
			# Get the record index in demand from the user with input(). Check 
			# the validity of the input index. If the index is valid, use the  
			# helper function show_restaurant_card(res, index); Otherwise, 
			# print "invalid index." 
			continue #should be removed after your implementation

        elif choice in ['3', '4', '5']:
            # Strict Security Warning
            print("\n❗ SECURITY WARNING: You are entering write-mode.")
            print("Changes will be saved to the database immediately.")
            confirm = input("Are you sure? (type 'yes' to proceed): ").lower()
            if confirm != 'yes':
                print("Operation cancelled.")
                continue

            if choice == '3': # ADD NEW DATA
				itemId = 1000000 + len(data) + 1 #the item id for the new data
				
				# YOUR CODE HERE
				# Instruction:
				# First: ask the user to input a new restaurant description.
				# Second: use new_data_entry_process() to process the new paragraph.
				# Third: append the new restaurant data to the original data list.
				# Finally: save using save_data().
				
                print("✅ Restaurant added.")

            elif choice == '4': # EDIT DATA
				# YOUR CODE HERE
				# Instruction:
				# First: ask for the input record index.
				# Second: iterate over the keys of the current record, and ask for
				#         new values. If the user doesn't want to update, a simple 
				#         Enter can skip. Update it only when the input index is 
				#         valid.
				# Third: save with save_data() and notify ("✅ Record updated.")
				continue #should be removed after your implementation

            elif choice == '5': # DELETE DATA
				# YOUR CODE HERE
				# Instruction:
				# First: ask for the input record index.
				# Second: use pop() to delete if the index is valid.
				# Third: save_data() and notify.
				continue #should be removed after your implementation

        elif choice == '6': # EXIT
            break
        else:
            print("Invalid input.")

# RUN THE UI
if __name__ == "__main__":
    manage_restaurants()

```

## Exercise 3: Test your UI

Before deploying any user interface, rigorous testing is essential to ensure data integrity and a smooth user experience.

**Important:** Copy and paste the code block below to the same `restaurant_data_management.py`. Then run the provided Unit Test. A successful implementation will return an "OK" status in the console, confirming that your core logic is sound.

Good luck!

```python
class TestRestaurantDatabase(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary clean database for testing."""
        self.test_file = 'structured_restaurant_data_unit_test.json'
        self.test_file_backup = 'structured_restaurant_data_unit_test.json.bak'
        self.initial_data = [{"name": "Test Cafe", "location": "Test City"}]
        with open(self.test_file, 'w') as f:
            json.dump(self.initial_data, f)

    def tearDown(self):
        """Clean up the test file after tests."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
		if os.path.exists(self.test_file_backup):
			os.remove(self.test_file_backup)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_and_delete_restaurant_success(self, mock_stdout, mock_input):
        """
        Test Scenario: Add a new restaurant.
        Inputs: '3' (Add), 'yes' (Confirm), 'New Burger Joint', '6' (Exit)
        """
        # We mock the sequence of user inputs
        mock_restaurant = 'The Copper Sprout is a high-concept, Modern Appalachian farm-to-table destination that blends an industrial-chic aesthetic with rustic forest charm, featuring reclaimed wood and amber lighting to create a sophisticated yet cozy vibe. Priced in the $$$ category, the menu celebrates seasonal foraging and local heritage, headlined by signature dishes like Cast-Iron Smoked Trout with pickled fiddlehead ferns and hand-foraged Wild Mushroom Risotto with aged goat cheese. The experience is designed to be intimate and earthy, making it a premier spot for those seeking high-quality, smokehouse-influenced cuisine in a refined, atmospheric setting.'
        mock_input.side_effect = ['3', 'yes', mock_restaurant, '6']
        
        # Run the app
        try:
            manage_restaurants(self.test_file, self.test_file_backup)
        except SystemExit:
            pass # Handle exit if your script uses sys.exit()

        # Check if the data was actually saved
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        
        print(data)
        self.assertEqual(len(data), 2)
        self.assertIn("✅ Restaurant added.", mock_stdout.getvalue())

        mock_input.side_effect = ['5', 'yes', 1, '6']
        
        # Run the app
        try:
            manage_restaurants(self.test_file, self.test_file_backup)
        except SystemExit:
            pass # Handle exit if your script uses sys.exit()

        # Check if the data was actually saved
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        
        print(data)
        self.assertEqual(len(data), 1)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_security_cancel(self, mock_stdout, mock_input):
        """
        Test Scenario: Try to delete but say 'no' to security warning.
        Inputs: '5' (Delete), 'no' (Cancel), '6' (Exit)
        """
        mock_input.side_effect = ['5', 'no', '6']
        
        manage_restaurants(self.test_file, self.test_file_backup)
        
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        
        self.assertEqual(len(data), 1) # Data should remain unchanged
        self.assertIn("Operation cancelled.", mock_stdout.getvalue())
		
if __name__ == "__main__":
    unittest.main() # Unit Test
	# manage_restaurants(FILEPATH, BACKUP_PATH) # Actual UI Call

```

Run the unit test by executing the following:

```bash
python restaurant_data_management.py

```

::page{title="Conclusion"}

You have successfully completed this lab! Congratulations!

In the following modules, you will keep building more interesting generative AI applications, along with more modern and interactive UI interfaces!

## Author(s)

[Jianping Ye](https://www.linkedin.com/in/jianping-ye/)

### © IBM Corporation. All rights reserved.

&nbsp;
