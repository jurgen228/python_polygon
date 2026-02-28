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
    done = "v"
    undone = "x"
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} [{done if task['done'] else undone}]")

def delete_task(tasks, number=None):
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        if number is None:
            index = random.randrange(len(tasks))
        else:
            index = number - 1
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
