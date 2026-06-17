# ============================================================
#  Simple To-Do List App
#  Just run this file and follow the menu on screen!
# ============================================================

import os

# This list holds all your tasks while the app is running
tasks = []

# ── Helpers ─────────────────────────────────────────────────

def clear_screen():
    """Clear the terminal so the display stays tidy."""
    os.system("cls" if os.name == "nt" else "clear")

def press_enter():
    """Pause until the user is ready to continue."""
    input("\nPress Enter to go back to the menu...")

def show_header():
    """Print a simple title banner."""
    clear_screen()
    print("=" * 40)
    print("        ✅  MY TO-DO LIST APP")
    print("=" * 40)

# ── Core features ────────────────────────────────────────────

def view_tasks():
    """Display all tasks with their status."""
    show_header()
    if not tasks:
        print("\n  You have no tasks yet. Add one!")
    else:
        print(f"\n  You have {len(tasks)} task(s):\n")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "⬜"
            print(f"  {index}. {status}  {task['name']}")
    press_enter()


def add_task():
    """Ask the user for a task name and save it."""
    show_header()
    print("\n── Add a New Task ──\n")
    name = input("  What do you need to do? ").strip()
    if name == "":
        print("\n  ⚠️  You didn't type anything. Task not added.")
    else:
        tasks.append({"name": name, "done": False})
        print(f"\n  ✅  '{name}' has been added!")
    press_enter()


def complete_task():
    """Mark a task as done."""
    show_header()
    print("\n── Mark a Task as Done ──\n")

    if not tasks:
        print("  No tasks to complete yet!")
        press_enter()
        return

    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "⬜"
        print(f"  {index}. {status}  {task['name']}")

    print()
    choice = input("  Enter the number of the task you finished: ").strip()

    if choice.isdigit():
        num = int(choice)
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f"\n  🎉  Great job! '{tasks[num - 1]['name']}' is done!")
        else:
            print("\n  ⚠️  That number is not on the list.")
    else:
        print("\n  ⚠️  Please type a number, not a word.")

    press_enter()


def delete_task():
    """Remove a task from the list."""
    show_header()
    print("\n── Delete a Task ──\n")

    if not tasks:
        print("  No tasks to delete yet!")
        press_enter()
        return

    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "⬜"
        print(f"  {index}. {status}  {task['name']}")

    print()
    choice = input("  Enter the number of the task to delete: ").strip()

    if choice.isdigit():
        num = int(choice)
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"\n  🗑️  '{removed['name']}' has been deleted.")
        else:
            print("\n  ⚠️  That number is not on the list.")
    else:
        print("\n  ⚠️  Please type a number, not a word.")

    press_enter()


def clear_all_tasks():
    """Delete every task after asking for confirmation."""
    show_header()
    print("\n── Clear All Tasks ──\n")

    if not tasks:
        print("  The list is already empty!")
        press_enter()
        return

    confirm = input("  Are you sure you want to delete ALL tasks? (yes / no): ").strip().lower()
    if confirm == "yes":
        tasks.clear()
        print("\n  🗑️  All tasks have been cleared.")
    else:
        print("\n  Cancelled. Your tasks are safe.")

    press_enter()


# ── Main menu ────────────────────────────────────────────────

def show_menu():
    """Print the main menu choices."""
    show_header()
    done_count = sum(1 for t in tasks if t["done"])
    total      = len(tasks)
    print(f"\n  Progress: {done_count} / {total} tasks completed\n")
    print("  1.  View all tasks")
    print("  2.  Add a new task")
    print("  3.  Mark a task as done")
    print("  4.  Delete a task")
    print("  5.  Clear ALL tasks")
    print("  6.  Quit")
    print()


def run():
    """Keep showing the menu until the user quits."""
    while True:
        show_menu()
        choice = input("  Choose an option (1-6): ").strip()

        if   choice == "1": view_tasks()
        elif choice == "2": add_task()
        elif choice == "3": complete_task()
        elif choice == "4": delete_task()
        elif choice == "5": clear_all_tasks()
        elif choice == "6":
            clear_screen()
            print("\n  👋  Goodbye! Have a productive day!\n")
            break
        else:
            input("\n  ⚠️  Please type a number from 1 to 6. Press Enter to try again...")


# ── Entry point ──────────────────────────────────────────────

if __name__ == "__main__":
    run()