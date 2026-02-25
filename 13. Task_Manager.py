# First we need to create a file named task.txt file b4 running this pgm
import os

FILE_NAME = "tasks.txt"

#Loading Tasks from the task.txt file
def load_tasks():
        tasks = {}
        if os.path.exists(FILE_NAME):
                with open(FILE_NAME,"r") as file:
                        for line in file.readlines():
                                task_id, title, status = line.strip().split(" | ")
                                tasks[int(task_id)] = {"title": title, "status": status}
        return tasks

#Saving tasks into task.txt file
def save_tasks(tasks):
        with open(FILE_NAME, "w") as file:
                for task_id, task in tasks.items:
                        file.write(f"{task_id} | {tasks["title"]} | {tasks["status"]}\n")

def add_task(tasks):
        title = input("Enter the task title: ")
        task_id = max(tasks.keys(), default=0)+1
        tasks[task_id] = {"title": title, "status": "Incomplete"}

def view_tasks(tasks):
        if not tasks:
                print("No tasks available.")
        else:
                for task_id, task in tasks.items:
                        print(f"[{task_id}] {task['title']} - {task['status']}")

def mark_task_complete(tasks):
        task_id = int(input("Enter the task id to be marked as complete"))
        if task_id in tasks:
                tasks[task_id]["status"] = "Complete"
                print(f"Task '{tasks[task_id]['title']}' marked as complete.")
        else:
                print("Task ID not found")
        
def delete_tasks(tasks):
        task_id = int(input("Enter the task id to Delete: "))
        if task_id in tasks:
                deleted_task = tasks.pop(task_id)
                print(f"Task '{tasks[task_id]['title']}' deleted.")
        else:
                print("Task ID not found.")

def main():
        tasks = load_tasks()
        while True:
                print("\nTask Manager Menu")
                print("1. Add Task")
                print("2. View Task")
                print("3. Mark Task as completed")
                print("4. Delete Task")
                print("5. Exit")
                choice = int(input("Enter your choice :-"))
                match(choice):
                        case 1:
                                add_task(tasks)
                        case 2:
                                view_tasks(tasks)
                        case 3:
                                mark_task_complete(tasks)
                        case 4:
                                delete_tasks(tasks)
                        case 5:
                                save_tasks(tasks)
                                print("Goodbye")
                                break
                        case _:
                                print("INvalid Choice. Please try again")

if "__name__" == "__main__":
        main()

