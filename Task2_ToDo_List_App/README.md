# To-Do List Application

## Description
This is a simple **command-line To-Do List application** built in Python.  
Users can **add**, **delete**, **mark tasks as done**, and **list all tasks**.  
Tasks are stored persistently in a JSON file (`tasks.json`).

## Features
- Add new tasks.
- List all tasks with their status (Pending/Done).
- Mark tasks as done.
- Delete tasks.
- Error handling for invalid input or non-existent tasks.
- Menu-based Command Line Interface (CLI).

## Files
- `todo.py` → Python script containing all functionality.
- `tasks.json` → JSON file that stores tasks persistently.

## How to Run
1. Make sure you have Python installed.
2. Place `todo.py` and `tasks.json` in the same folder.
3. Open terminal/command prompt and navigate to the folder.
4. Run the script:

```bash
python todo.py
Follow the menu to add, list, mark as done, or delete tasks.

Example
mathematica
Copy code
--- To-Do List Menu ---
1. Add Task
2. List Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
Enter your choice: 
Notes
Tasks are saved automatically in tasks.json.

The application handles invalid inputs gracefully.