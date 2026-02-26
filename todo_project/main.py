# TASK: Simple CLI To-Do List (In Memory Only)

# Write a single Python program that runs in the terminal and manages a simple to-do list.

# IMPORTANT:
# - Keep all data in RAM (memory).
# - When the program exits, all data is lost (this is expected). 
# - Do NOT use files.
# - Do NOT use external libraries.

# ----------------------------------------
# PROGRAM BEHAVIOR

# When the program starts, it must display:

# 1 - Add task
# 2 - Show tasks
# 3 - Mark task as done
# 4 - Delete task
# 5 - Exit

# The user selects an option by typing a number.
# The menu must repeat until the user chooses "Exit".

# ----------------------------------------
# DATA STRUCTURE

# Store tasks in a list.

# Each task must be a dictionary with:
# - id (integer)
# - title (string)
# - done (boolean)

# Example structure:

# [
#     {"id": 1, "title": "Buy milk", "done": False},
#     {"id": 2, "title": "Learn Python", "done": True}
# ]

# IDs must be assigned automatically and incremented (1, 2, 3, ...).

# ----------------------------------------
# FUNCTIONAL REQUIREMENTS

# 1) Add Task
# - Ask the user to enter a task title.
# - Create a new task.
# - Assign a unique incremental ID.
# - Add it to the list.

# 2) Show Tasks
# Display tasks in this format:

# [ ] 1 - Buy milk
# [x] 2 - Learn Python

# Where:
# [ ] = not done
# [x] = done

# If there are no tasks, display:
# "No tasks yet."

# 3) Mark Task as Done
# - Ask the user for a task ID.
# - If the ID exists, set done = True.
# - If the ID does not exist, show an error message.

# 4) Delete Task
# - Ask the user for a task ID.
# - If the ID exists, remove the task.
# - If the ID does not exist, show an error message.

# 5) Exit
# - Stop the program cleanly.

# ----------------------------------------
# TECHNICAL REQUIREMENTS

# - Use functions (no giant block of code in main).
# - Use a while loop for the menu.
# - Validate user input:
#   - Handle non-numeric input.
#   - Handle invalid menu choices.
#   - Handle non-existing IDs.
# - Keep the code clean and readable.

#   Structurize code by splitting it into several functions DONE
#   Add list item status DONE                                  
#   defend program from incorrect input attempts DONE
#       zum Beispiel:
#          Choose option 3            
#               'abrakadabra'
#   pull request machen

from tasks import add_task, show_task, mark_task_as_done, delete_task

tasks = []

# functions (moved to tasks.py)

while True:
    if len(tasks) > 0:
        print("")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Delete task")
    print("4 - Mark task as done")
    print("5 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        show_task(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        mark_task_as_done(tasks)

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid option")


