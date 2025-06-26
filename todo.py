import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from the file, or start with an empty list
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save current tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Initialize tasks from file
tasks = load_tasks()

def add_task(description):
    task = {"description": description, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added: {description}")

def list_tasks():
    if not tasks:
        print("📭 No tasks found.")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['description']}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"🎉 Completed: {tasks[index]['description']}")
    else:
        print("⚠️ Invalid task number.")