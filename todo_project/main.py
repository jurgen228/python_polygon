import random

from tasks import (
    add_task, 
    show_task, 
    mark_task_as_done, 
    delete_task, 
    show_random_task
)
from data import tasks

while True:
    if len(tasks) > 0:
        print("")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Delete task")
    print("4 - Mark task as done")
    print("5 - Show random task")
    print("6 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task_text = input("Enter task: ")
        add_task(tasks, task_text)
        print("Task added!")

    elif choice == "2":
        show_task(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        mark_task_as_done(tasks)

    elif choice == "5":
        show_random_task(tasks)

    elif choice == "6":
        print("Bye!")
        break

    else:
        print("Invalid option")
