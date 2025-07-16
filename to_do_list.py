import os
import json
tasks=[]
completed_tasks=[]
def add_task():
    task = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal): ")
    tasks.append({"task": task, "category": category})

def view_task():
    print("All tasks to do:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. [{task['category']}] {task['task']}")
    
    print("\nCompleted tasks:")
    for i, task in enumerate(completed_tasks):
        print(f"{i+1}. [{task['category']}] {task['task']}")

def remove_task():
    index=0
    for i in tasks:
        print(f"{index+1}.{i}")
        index+=1    
    print("Enter the task number that you want to remove:")
    choice=int(input())    
    if choice<0 and choice>len(tasks)-1:
        raise ValueError(f"No task at {choice}")
    choice-=1
    tasks.pop(choice)
def display_completed_tasks():
    print(completed_tasks)    
def mark_as_complete():
    for i, task in enumerate(tasks):
        print(f"{i+1}. [{task['category']}] {task['task']}")
    
    choice = int(input("Enter the task number you completed: ")) - 1
    if 0 <= choice < len(tasks):
        completed_tasks.append(tasks.pop(choice))
    else:
        print("Invalid task number.")

def load_from_json_file():
    global tasks, completed_tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            data = json.load(f)
            tasks = data.get("tasks", [])
            completed_tasks = data.get("completed_tasks", [])

def save_to_json_file():
    data = {
        "tasks": tasks,
        "completed_tasks": completed_tasks
    }
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)  # indent=4 makes it readable

def remove_completed_tasks():
    for completed_task in completed_tasks:
        i=0
        while i<=len(tasks)-1:
            if(tasks[i]==completed_task):
                tasks.pop(i)
                break
            i+=1    
load_from_json_file()
while True:
    print("1.Add task")
    print("2.View tasks")
    print("3.Remove task")
    print("4.Mark as completed")
    print("5.Remove completed tasks from list")
    print("6.Save to file")
    print("7.Exit")
    choice=int(input("Enter choice:"))
    if(choice<1 or choice>7):
        raise ValueError("Input from 1 to 7")
    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        remove_task()
    elif choice==4:
        mark_as_complete()    
    elif choice==5:
        remove_completed_tasks()
    elif choice==6:
        save_to_json_file()
    elif choice==7:
        break