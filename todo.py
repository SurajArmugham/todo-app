import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            # File is empty or corrupted, return empty list
            return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            title = task.get("title", "Untitled")
            done = task.get("done", False)
            status = "✅" if done else "❌"
            print(f"{i}. {title} [{status}]")

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f"🎉 Marked as complete: {tasks[task_number - 1]['title']}")
    else:
        print("❌ Invalid task number.")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['title']}")
    else:
        print("❌ Invalid task number.")