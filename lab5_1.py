#Name: Anthia Gardner-Celestine
#Lab Title: Lab 5 
#Date: 5/28/2026

#Section 1: Functions

#Task

#1.1 Create an empty list named todo_list

# todo_list = []

from lab5_3 import load_task_list
from lab5_3 import store_task_list


#1.2 Create a function called add_task

def add_task(task):
    '''Adding Tasks To Do List'''

    todo_list.append(task)

    print(f"Task was added {task}")


#1.3 Create a function called show_tasks

def show_tasks():
    '''Displays every task in the to do list'''

    if todo_list == []:

        print("To do list is empty.")

    else:

        index = 1

        for task in todo_list:

            print(f"{index}. {task}")

            index += 1


#1.4 Create a function called remove_task

def remove_task(num):
    '''Function removes a task from the list'''

    try:

        if num >= 1 and num <= len(todo_list):

            removed = todo_list.pop(num - 1)

            print(f"Task removed: {removed}")

        else:

            print("Invalid task number.")

    except:

        print("Please enter a valid number.")


#Task 2

#2.1 Create a function called run_todo_app()

def run_todo_app():
    '''Runs the todo application'''

    #2.2 Display welcome message

    print("Welcome To The Todo App")

    #2.3 Create an infinite loop

    while True:

        #2.4 Display menu

        print("\n1. Show all tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("What would you like to do? Please select a number > ")

        #2.5 Handle the choices

        if choice == "1":

            show_tasks()

        elif choice == "2":

            task = input("Enter a task description > ")

            if task.strip() == "":

                print("Task cannot be blank.")

            else:

                add_task(task)

        elif choice == "3":

            show_tasks()

            task_number = input("Enter the task number to remove > ")

            try:

                task_number = int(task_number)

                remove_task(task_number)

            except:

                print("Please enter a valid number.")

        elif choice == "4":

            print("Thank you for using the Todo App")

            break

        else:

            print("Invalid menu option.")


#2.6 Call the run_todo_app only if the script is executed

todo_list = load_task_list()

if __name__ == "__main__":
    run_todo_app()
    store_task_list(todo_list)