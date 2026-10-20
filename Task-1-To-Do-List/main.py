tasks = []
task_id = 1

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter task description: ").strip()

        if description == "":
            print("Please enter a task.")

        else:
            task = {
                "id": task_id,
                "description": description,
                "completed": False
            }

            tasks.append(task)
            task_id += 1

            print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")

        else:
            print("\nYour Tasks:")

            for task in tasks:
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f'{task["id"]}. {task["description"]} - {status}')

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available to complete.")

        else:
            for task in tasks:
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f'{task["id"]}. {task["description"]} - {status}')

            try:
                selected_id = int(input("Enter task ID to complete: "))

                for task in tasks:
                    if task["id"] == selected_id:
                        if task["completed"]:
                            print("This task is already completed.")
                        else:
                            task["completed"] = True
                            print("Task completed successfully!")
                        break

                else:
                    print("Task ID not found.")

            except ValueError:
                print("Please enter a valid task ID.")

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")

