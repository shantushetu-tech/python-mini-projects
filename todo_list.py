# ==========================================
# To-Do List CLI App
# Created by: Shantha Kumari
# ==========================================

tasks = []

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"✅ '{removed}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please try again.")