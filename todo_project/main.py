from tasks import (
    add_task, 
    show_task, 
    mark_task_as_done, 
    delete_task_by_number, 
    delete_random_task,
    pick_random_task
)
from data import tasks, actions, objects

while True:
    if len(tasks) > 0:
        print("")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Delete task")
    print("4 - Mark task as done")
    print("5 - Pick random task")
    print("6 - Delete random task")
    print("7 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task_text = input("Enter task: ")
        add_task(tasks, task_text)
        print("Task added!")

    elif choice == "2":
        show_task(tasks)

    elif choice == "3":
        task_number = int(input("Enter index of the task: "))
        delete_task_by_number(tasks, task_number)

    elif choice == "4":
        mark_task_as_done(tasks)

    elif choice == "5":
        pick_random_task(tasks, actions, objects)
        print(f"Random task added: {len(tasks)} - {tasks[-1]["title"]}")

    elif choice == "6":
        delete_random_task(tasks)

    elif choice == "7":
        print("Bye!")
        break
    else:
        print("Invalid option")
