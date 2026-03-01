import random

def task_appender(tasks, task):
    tasks.append(task)

def add_task(tasks, task_text):
    task = {
        "title": task_text,
        "done": False
    }
    task_appender(tasks, task)

def show_task(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            marker = "v" if task['done'] else "x"
            print(f"{i}. {task['title']} [{marker}]")

def delete_task(tasks, task_number=None):
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        if task_number is None:
            index = random.randrange(len(tasks))
        else:
            index = task_number - 1
        deleted_task = tasks.pop(index)
        print(f"Deleted task: {deleted_task}")
    except (ValueError, IndexError):
        print("Invalid task number.")

def mark_task_as_done(tasks):
    show_task(tasks)
    number = int(input("Enter task number: "))
    tasks[number - 1]["done"] = True
    print("Task completed!")

def pick_random_task(tasks, actions, objects):
    word1 = random.choice(actions)
    word2 = random.choice(objects)
    task = {
        "title": word1 + " " + word2,
        "done": False
    }  
    task_appender(tasks, task)

def delete_task_by_index(tasks, task_index):
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        tasks.pop(task_index)
    except IndexError:
        print("Invalid task index.")

def delete_task_by_number(tasks, task_number):
    task_index = task_number - 1
    delete_task_by_index(tasks, task_index)

def delete_random_task(tasks):
    if not tasks:
        print("No tasks to delete jetzt.")
        return
    else:
        task_index = random.randrange(len(tasks))
        delete_task_by_index(tasks, task_index)
