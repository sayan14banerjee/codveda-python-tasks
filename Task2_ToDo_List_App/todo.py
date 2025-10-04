import json

# Load tasks from a JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to a JSON file   
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# Add a new task
def add_task():
    task_name = input("Enter the task: ")
    tasks = load_tasks()
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"Task '{task_name}' added successfully!")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{idx}. {task['task']} - {status}")

def mark_done():
    list_tasks()
    tasks = load_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        tasks[task_no - 1]["done"] = True
        save_tasks(tasks)
        print(f"Task {task_no} marked as done!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def delete_task():
    list_tasks()
    tasks = load_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' deleted!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def menu():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
