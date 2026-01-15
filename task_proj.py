def task():
    tasks=[]
    print("---------------------Welcome to the task management app---------------------")
    total_task=int(input("Enter How many Task you want to add = "))
    for i in range(1,total_task+1):
        task_name=input("enter task ,{i},=")
        tasks.append(task_name)

    print("Today's Task are\n {tasks}")

    
    while True:
        operation=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        if operation==1:
            add=input("Enter task you want to add = ")
            tasks.append(add)
            print("Task {add} has been succesfully added..")
        elif operation==2:
            updated_var=input("Enter the task that you want to update=")
            if updated_var in tasks:
                up=input("Enter new Task=")
                ind=tasks.index(updated_var)
                tasks[ind]=up
                print("Updated task {up}")
task()