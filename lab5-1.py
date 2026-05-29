#Name: Anthia Gardner-Celestine
#Lab Title: Lab 5 
#Date: 5/28/2026

#Section 1:Functions
#Task
#1.1 Create an empty list named todo_list [1 point] 

todo_list = []

#1.2 Create a function called add_task. This function takes a string as a parameter and 
#appends it to the todo_list. It also prints a statement that the task was added, use an f 
#string to display the actual task added. 

def add_task(task):
    '''Adding Tasks To Do List'''
    todo_list.append(task)
    print(f"Task was added {task}")
    
#1.3 Create a function called show_tasks. This function displays every task in the todo list 
#and numbers them starting at 1. If the todo list is empty, it shows a message stating that. [5 
#points]

def show_tasks():
    '''Displays every task in the to do list'''
    index = 1
    for task in todo_list:
        print(f"{index}. {task}")
        index += 1
        if todo_list == []:
         print("To do list is empty.")

        


#1.4 Create a function called remove_task. This function takes in an integer that is based on 
#the number assigned to the tasks from show_tasks. So, it is a 1-based index. So, you have 
#to compensate for that to remove the correct task from the list. Please ensure to handling 
#invalid numbers/text. [6 points]

def remove_task(num):
    '''Function takes in an integer'''
    if num >=1 and num <= len(todo_list):
       removed = todo_


