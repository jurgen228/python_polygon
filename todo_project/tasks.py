def add_task(tasks):
    task_text = input("Enter task: ")
    task = {
        "title": task_text,
        "done": False
    }
    tasks.append(task)
    print("Task added!")

def show_task(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} [{'v' if task['done'] else 'x'}]")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    while True:
        try:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted!")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number!")

def mark_task_as_done(tasks):
    show_task(tasks)
    number = int(input("Enter task number: "))
    tasks[number - 1]["done"] = True
    print("Task completed!")