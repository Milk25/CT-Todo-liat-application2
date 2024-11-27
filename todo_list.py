 todo_list.py

tasks = []  # Global list to store tasks


def display_menu():
    """Displays the main menu."""
    print("\nWelcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")


def add_task():
    """Adds a new task to the to-do list."""
    title = input("Enter the task title: ").strip()
    if title:
        tasks.append({"title": title, "status": "Incomplete"})
        print(f'Task "{title}" added successfully.')
    else:
        print("Task title cannot be empty.")


def view_tasks():
    """Displays all tasks with their statuses."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} - {task['status']}")


def mark_task_complete():
    """Marks a selected task as complete."""
    if not tasks:
        print("No tasks available.")
        return

    try:
        view_tasks()
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "Complete"
            print(f'Task "{tasks[task_num - 1]["title"]}" marked as complete.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    """Deletes a selected task."""
    if not tasks:
        print("No tasks available.")
        return

    try:
        view_tasks()
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task["title"]}" deleted successfully.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main function to run the To-Do List application."""
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")