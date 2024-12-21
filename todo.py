print("welcome to your todo-list!")
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks ,1):
            print(f"{i}.{task}")

def add_tasks(task, due_date=None):
    tasks.append({"task" : task, "{due_date" : due_date})
    print(f"Added:{task} (Due: {due_date})")

def remove_tasks(index):
    if 0 < index <= len(tasks):
        print(f"Removed:{tasks.pop(index - 1)}")
    else:
        print("Invalid task number")

while True:
    print("\nOptions:[1] Show Tasks [2] Add Tasks [3]Remove Tasks [4]Quit")
    choice = input("Choose a option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter a task: ")
        add_tasks(task)
    elif choice == "3":
        show_tasks()
        try:
            index = int(input("Enter task number to remove: "))
            remove_tasks(index)
        except ValueError:
            print("Please enter the valid number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
