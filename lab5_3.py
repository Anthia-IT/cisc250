#Section 3: Files

#Task 1

#1.1 Import Path and json

from pathlib import Path
import json


#1.2 Create a function called store_task_list

def store_task_list(task_list):
    '''Stores the task list in a JSON file'''

    #1.2 Create a variable with the Path

    file_path = Path("task_list.json")

    #1.3 Convert list to JSON string

    json_string = json.dumps(task_list)

    #Write JSON string to file

    file_path.write_text(json_string)

    #1.4 Print message

    print("Task list was saved.")


#Task 2

#2.1 Create a function called load_task_list

def load_task_list():
    '''Loads the task list from a JSON file'''

    #2.2 Create a variable with the Path

    file_path = Path("task_list.json")

    #2.3 Check if file exists

    if file_path.exists():

        json_string = file_path.read_text()

        return json.loads(json_string)

    else:

        return []
    
    # End of Section 3