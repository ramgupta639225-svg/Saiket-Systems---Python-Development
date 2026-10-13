
tasks = []
task_id = 1

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter your task: ").strip()

        if not description:
            print("Task cannot be empty!")

        elif any(task["description"].lower() == description.lower() for task in tasks):
            print("Task is already added!")

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
        if not tasks:
            print("No tasks available!")

        else:
            for task in tasks:
                status = "Completed" if task["completed"] else "Pending"
                print(f'ID: {task["id"]} | {task["description"]} | {status}')

    elif choice == "3":
        if not tasks:
            print("No tasks available!")

        else:
            for task in tasks:
                status = "Completed" if task["completed"] else "Pending"
                print(f'ID: {task["id"]} | {task["description"]} | {status}')

            try:
                selected_id = int(input("Enter task ID: "))

                for task in tasks:
                    if task["id"] == selected_id:
                        if task["completed"]:
                            print("Task is already completed!")
                        else:
                            task["completed"] = True
                            print("Task marked as completed!")
                        break
                else:
                    print("Invalid task ID!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice!")
