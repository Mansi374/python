tasks=[]
def add_task():
    task1=input("Enter a task:")
    priority=input("Enter the priority:")
    tasks.append((task1,priority))
def view_task():
    for task in sorted(tasks,key=lambda x:x[1]):
        print(f"{task[0]} Priority:{task[1]}")
def update_task():
    update=input("Enter task to update:")
    for i,task in enumerate(tasks):
        if task[0] == update:
            new=input("Enter new task:")
            new_p=input("Enter new priority:")
            tasks[i]=(new,new_p)
            return
def del_task():
    del_=input("Enter task to delete:")
    for task in tasks:
        if task[0] == del_:
            tasks.remove(task)
            return
while True:
    print("Menu")
    print("1.Add task")
    print("2.Update task")
    print("3.View task")
    print("4.Delete task")
    choice=input("Enter your choice:")
    if choice == "1":
        add_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        view_task()
    elif choice == "4":
        del_task()
    else:
        print("Invalid choice")




