To-Do List Manager (Python CLI)
This is a command-line To-Do List application written in Python that lets users add, view, complete, remove, and persist tasks with category support. Tasks are saved in a JSON file for permanent storage between sessions.

🚀 Features
✅ Add tasks with categories (e.g., Work, Personal)

✅ View pending and completed tasks

✅ Mark tasks as completed

✅ Remove tasks from the list

✅ Save and load tasks from a tasks.json file

✅ Simple command-line interface (CLI)

🛠️ Technologies Used
Python 3

json module

os module

File I/O

▶️ How to Run
Make sure Python 3 is installed.

Clone this repository or download the .py file.

Open terminal/command prompt in the project directory.

Run:

bash
Copy
Edit
python todo.py
Follow the menu options.

📁 File Structure
pgsql
Copy
Edit
📦to-do-list-manager
 ┣ 📜 todo.py
 ┗ 📜 tasks.json (auto-generated after saving)
💾 Sample tasks.json (after saving)
json
Copy
Edit
{
    "tasks": [
        {"task": "Finish Python assignment", "category": "Work"},
        {"task": "Buy groceries", "category": "Personal"}
    ],
    "completed_tasks": [
        {"task": "Go for a walk", "category": "Health"}
    ]
}
