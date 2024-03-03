import os
tasks=[]
def add_task(task):
      tasks.append(task)
      print(f"Added task:{task}")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Added removed:{task}")
    else:
        print("\ntask not found ")
def view_task():
    print("to-do list\n")            
    for i,task in enumerate(tasks):
        print(f"{i+1}.{task}")
while True:
    print("select the choice")
    print("1.Add task")        
    print("2.Remove task")
    print("3.view tasks")
    print("4.Exit")

    choice=int(input("enter the choice\n"))
    if choice==1:
        task=input("enter the new task:\n")
        add_task(task)
    elif choice==2:
        task=input("enter the task to remove:\n")
        remove_task(task)
    elif choice==3:
        view_task()
    elif choice==4:
        print("exiting:\n")
        break
    else:
        print("invalid choice\n")
 