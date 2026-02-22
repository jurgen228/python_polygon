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


tasks = []


while True:
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Delete task")
    print("5 - Exit")


    choice = input("Choose option: ")


    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks jetzt.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted!")
            else:
                print("Invalid number")

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid option")

print("Hallo, Welt")
