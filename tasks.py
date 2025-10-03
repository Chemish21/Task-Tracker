#Python
import json
import os

def add_task(task: str):
    #If JSON file does not already exist
    if not os.path.exists('data.json'):
        with open('data.json', 'w', encoding='utf-8') as json_file:
            #Set first task
            the_task = {"task": task, "id": 1}
            #Initializing Array for tasks and creating JSON file
            obj_tasks = {"tasks":[the_task]}
            json.dump(obj_tasks, json_file, indent=2)
    else:
        with open('data.json', 'r+', encoding='utf-8') as json_file:
            #Get JSON data or handle event if JSON file exists but is empty
            try:
                json_data = json.load(json_file)
            except json.JSONDecodeError:
                #Reset JSON file if necessary
                json_data = {"tasks": []}

            obj_tasks = json_data["tasks"]

            #Find Max id number
            max_id = max([t["id"] for t in obj_tasks], default=0)

            #Set and append new task
            the_task = {"task": task, "id": max_id + 1}
            obj_tasks.append(the_task)

            #Place new data into JSON file
            json_file.seek(0)
            json_file.truncate()
            json.dump(json_data, json_file, indent=2)

def delete_task(the_id: int):
    #If JSON data file does not exist
    if not os.path.exists('data.json'):
        print("No tasks exist to be deleted")
    else:
        with open('data.json', 'r+', encoding='utf-8') as json_file:
            #Get JSON data
            json_data = json.load(json_file)
            obj_tasks = json_data["tasks"]

            #Iterate through tasks and delete relevant task
            for task in obj_tasks:
                if task["id"] == the_id:
                    obj_tasks.remove(obj_tasks[the_id - 1])
                    json_file.seek(0)
                    json_file.truncate()
                    json.dump(json_data, json_file, indent=2)
                    break

def update_task(the_id: int, the_task: str):
    with open('data.json', 'r+', encoding='utf-8') as json_file:
        #Get JSON data
        json_data = json.load(json_file)
        obj_tasks = json_data["tasks"]

        #Finding task and updating with new task
        for task in obj_tasks:
            if task["id"] == the_id:
                task["task"] = the_task
                json_file.seek(0)
                json_file.truncate()
                json.dump(json_data, json_file, indent=2)
                break

def update_id():
    with open('data.json', 'r+', encoding='utf-8') as json_file:
        #Get JSON data and set reset id variable
        json_data = json.load(json_file)
        obj_tasks = json_data["tasks"]
        reset = 1

        #Iterate tasks and reset id's
        for task in obj_tasks:
            task["id"] = reset
            reset = reset + 1

        #Update JSON file id values
        json_file.seek(0)
        json_file.truncate()
        json.dump(json_data, json_file, indent=2)

def mark_task(the_id: int, the_mark: str):
    #If invalid mark inform the user
    if the_mark != "todo" and the_mark != "in-progress" and the_mark != "done":
        print("Invalid mark, options [1] todo [2] in-progress [3] done")
    else:
        with open('data.json', 'r+', encoding='utf-8') as json_file:
            #Get JSON data
            json_data = json.load(json_file)
            obj_tasks = json_data["tasks"]

            #Finding task and adding mark
            for task in obj_tasks:
                if task["id"] == the_id:
                    mark = {"mark": the_mark}
                    task.update(mark)
                    json_file.seek(0)
                    json_file.truncate()
                    json.dump(json_data, json_file, indent=2)
                    break

def list_one(the_id: int):
    with open('data.json', 'r', encoding='utf-8') as json_file:
        #Get JSON data
        json_data = json.load(json_file)
        obj_tasks = json_data["tasks"]

        #Finding task to list
        for task in obj_tasks:
            if task.get("id") == the_id:
                for key, value in task.items():
                    print(f"{key}: {value}")
                print("-----------------")

def list_all():
    with open(r'data.json', 'r', encoding='utf-8') as json_file:
        #Get JSON data
        json_data = json.load(json_file)
        obj_tasks = json_data["tasks"]

        #Listing all tasks
        for task in obj_tasks:
            for key, value in task.items():
                print(f"{key}: {value}")
            print("-----------------")

def list_done():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        #Get JSON data
        json_data = json.load(json_file)
        obj_tasks = json_data["tasks"]

        #Listing all 'done' tasks
        for task in obj_tasks:
            if task.get("mark") == "done":
                for key, value in task.items():
                    print(f"{key}: {value}")
                print("-----------------")

def list_not_done():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        #Get JSON data
        json_data = json.load(json_file)
        obj_tasks = json_data["tasks"]

        #Listing all 'not done' tasks
        for task in obj_tasks:
            if task.get("mark") in ("todo", "in-progress"):
                for key, value in task.items():
                    print(f"{key}: {value}")
                print("-----------------")

def list_in_progress():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        #Get JSON data
        json_data = json.load(json_file)
        obj_tasks = json_data["tasks"]

        #Listing all 'in-progress' tasks
        for task in obj_tasks:
            if task.get("mark") == "in-progress":
                for key, value in task.items():
                    print(f"{key}: {value}")
                print("-----------------")
