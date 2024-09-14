tasks = []

def main(): 
    message = """
    Welcome to the Task Manager!
    1. Add a task to the list
    2. Remove a task from the list
    3. Mark a task as complete
    4. View all tasks
    5. Quit
    """
    
    while True:
        print(message)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def add_task():
    # Get the task name
    task = input("Enter task: ")

    # Define task status
    task_info = {"task": task, "completed": False}

    # Add task to the list
    tasks.append(task_info)

    # Show success message
    print("Task added successfully")

def remove_task():
    # Show list of tasks
    if not tasks:
        print("No tasks to remove")
        return
    else:
        view_tasks(tasks)
    
    # Ask user to choose a task
    try:
        task_index = int(input("Choose the task to remove: "))
        if task_index < 1 or task_index > len(tasks):
            print("Please choose from the available tasks")
            return

        # Remove the task
        tasks.pop(task_index - 1)
        # Show success message
        print("Task removed successfully")
    
    except ValueError:
        print("Invalid input, please enter a number")
  
def mark_task_complete():
    incomplete_tasks = [task for task in tasks if not task["completed"]]

    # Show list of incomplete tasks
    if not incomplete_tasks:
        print("No tasks to mark as complete")
        return

    for i, task in enumerate(incomplete_tasks):
        print(f"{i + 1}- {task['task']}")

    # Ask user to choose a task
    try:
        task_number = int(input("Choose the task to complete: "))
        if task_number < 1 or task_number > len(incomplete_tasks):
            print("Please choose from the available tasks")
            return

        # Mark the task as complete in the original tasks list
        task_to_complete = incomplete_tasks[task_number - 1]
        task_to_complete["completed"] = True

        # Show success message
        print("Task marked as complete")
    except ValueError:
        print("Invalid input, please enter a number")

def view_tasks(tasks_list):
    if not tasks_list:
        print("No tasks to view")
        return
    
    # if task["completed"] == True:
    #   task_status = "✅"
    # else:
    #   task_status = "❌"
    for i, task in enumerate(tasks_list):
        task_status = "✅" if task["completed"] else "❌"
        print(f"{i + 1}- {task['task']} {task_status}")

if __name__ == "__main__":
    main()
