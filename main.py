from todo import add_task, list_tasks, complete_task, delete_task

def show_menu():
    print("\n--- To-Do App ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")

def get_task_number(prompt):
    try:
        number = int(input(prompt))
        if number < 1:
            print("❌ Please enter a positive number.")
            return None
        return number
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return None

while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == '1':
        title = input("Task title: ").strip()
        if title:
            add_task(title)
        else:
            print("❌ Task title cannot be empty.")
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        number = get_task_number("Task number to mark complete: ")
        if number is not None:
            complete_task(number)
    elif choice == '4':
        number = get_task_number("Task number to delete: ")
        if number is not None:
            delete_task(number)
    elif choice == '5':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid option. Try again.")