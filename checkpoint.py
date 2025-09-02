import random

tasks = {
123456 : {"description": "work on the checkpoint tp ", "priority": "high", "status": "not completed"} ,
789101 :  {"description": "go on a walk ", "priority": "medium", "status": "not completed"}
}
def generate_unique_id(tasks):
    while True:
        a = random.randint(100000, 999999)
        if a not in tasks:
            return a


def add(tasks):
    task_id = generate_unique_id(tasks)  # get unique ID
    des = input("Enter your task description: ")
    pri = input("Enter your task's priority (high-medium-low): ")

    tasks[task_id] = {
    "description": des,
    "priority": pri,
    "status": "not completed"
    }

def view(tasks):
    i=1
    for key , value in tasks.items():
        print("*-------------- TASK",i,"--------------*")
        print("Task's ID : ",key)
        print("Task's description : ",value['description'])
        print("Task's priority :",value['priority'])
        print("Task's status : ",value['status'])
        print("*----------------------------*")
        i +=1

def complete(tasks):
    done = int(input("Enter the task's ID  : "))
    if done in tasks:
        tasks[done]["status"] = "Complete"
        print("Task's status has been updated successfully ! ")
    else:
        print("There is no task with such ID ! ")

def delete(tasks):
    ifdeleted = False
    ID = int(input("Enter the task's ID you have done : "))

    if ID in tasks:  
        del tasks[ID]
        ifdeleted = True
        print("Task has been deleted succesfully ! ")
    else:
        ifdeleted = False

        if not ifdeleted:
            print("There is no task with such ID to delete!")

def menu():
    while True:
        print("\n====== Main Menu ======")
        print("1. Add Task ")
        print("2. View Tasks ")
        print("3. Mark Task as Completed ")
        print("4. Delete a Task ")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add(tasks)

        elif choice == "2":
            view(tasks)

        elif choice == "3":
            complete(tasks)

        elif choice == "4":
            delete(tasks)
                
        elif choice == "5":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

menu()
