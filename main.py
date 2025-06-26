import todo

def menu():
    while True:
        print("\n📝 To-Do Menu")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Task description: ")
            todo.add_task(desc)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            try:
                index = int(input("Task number to complete: ")) - 1
                todo.complete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()