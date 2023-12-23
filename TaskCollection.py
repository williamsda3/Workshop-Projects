# Todo list 

TaskCollection = []

task = {
    'title': 'Task Title',
    'time': 'time',
    'complete': False
}

# Adding a Task
def add():
    task = input("Enter a task\n")
    TaskCollection.append(task)
    
# Show task completion
def complete(taskID):
   taskToMark =  TaskCollection[taskID]
   taskToMark['complete'] = True
    
# Viewing a Task
def view(viewOptions):
    if viewOptions == -1:
        num = 0
        for task in TaskCollection:
            print("Task" + " " + str(num) + ") " + task)  
            num += 1
    else:
        print(TaskCollection[viewOptions])  

# Deleting a Task
def delete(deleteOptions):
    if deleteOptions == -1:
       TaskCollection.clear()
    else:
        TaskCollection.remove(TaskCollection[deleteOptions])


stop = False
while stop is False:
    menu = input("select an option: \n 1: add \n 2: complete \n 3: view \n 4: delete \n 0: Exit \n ")
    if menu == '0':
        break
    if menu == '1':
        add()
    elif menu == '2':
        taskCompleted = input("which task would you like to complete")
        complete(taskCompleted)
    elif menu == '3':
        viewOptions = int(input("input -1 to view all tasks. input the task # to view a specific task")) 
        view(viewOptions)
    elif menu == '4':
        deletionOptions = int(input("input -1 to delete all tasks. input the task # to delete a specific task"))
        delete(deletionOptions)
    else:
        print("invalid input. please try again")
        menu = input("select an option: \n 1: add \n 2: complete \n 3: view \n 4: delete\n ")
# : )    