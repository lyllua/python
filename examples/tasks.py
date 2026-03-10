tasks = []
while True:
    try:
        print("1. Add task")
        print("2. Show all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        option = input("Choose an option: ")

        match option:
            case "1":
                try:
                    task = input("Write the new task: ")
                    if task.strip() == "":
                        print("Error: Task cannot be empty.")
                    else:
                        tasks.append({"name": task, "completed": False})
                        print("Task added.")
                except Exception as e:
                    print("Unexpected error while adding task:", e)

            case "2":
                try:
                    if tasks:
                        print("\nTask list:")
                        for i, t in enumerate(tasks, 1):
                            status = "Completed" if t["completed"] else "Not completed"
                            print(f"{i}. {t['name']} - {status}")
                    else:
                        print("There are no tasks.")
                except Exception as e:
                    print("Unexpected error while showing tasks:", e)

            case "3":
                try:
                    if not tasks:
                        print("No tasks to mark.")
                    else:
                        num = int(input("Number of the task to mark as completed: ")) - 1
                        if 0 <= num < len(tasks):
                            tasks[num]["completed"] = True
                            print("Task marked as completed.")
                        else:
                            print("Invalid number.")
                except ValueError:
                    print("Error: Please enter a valid number.")
                except Exception as e:
                    print("Unexpected error:", e)

            case "4":
                try:
                    if not tasks:
                        print("No tasks to delete.")
                    else:
                        num = int(input("Number of the task to delete: ")) - 1
                        if 0 <= num < len(tasks):
                            removed = tasks.pop(num)
                            print(f"Task '{removed['name']}' deleted.")
                        else:
                            print("Invalid number.")
                except ValueError:
                    print("Error: Please enter a valid number.")
                except Exception as e:
                    print("Unexpected error:", e)

            case "5":
                print("Goodbye!")
                break

            case _:
                print("Invalid option, try again.")

    except Exception as e:
        print("An unexpected error occurred:", e)