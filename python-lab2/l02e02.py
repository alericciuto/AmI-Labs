from sys import argv

fileName = argv[1]
file = open(fileName, "r")
task = file.read().splitlines()
file.close()

while True:
    print("Insert the number corresponding to the action you want to perform:\n\
    1. insert a new task;\n\
    2. remove a task;\n\
    3. show all the tasks, sorted in alphabetic order;\n\
    4. close the program.\n\n\
Your choice:\n")

    n = int(input())
    if n == 1:
        newTask = input("Enter a task:")
        task.append(newTask)
        print(newTask + ", APPENDED\n")
    elif n == 2:
        if len(task) > 0:
            t = input("Which task?")
            if t in task:
                task.remove(t)
                print(t + ", REMOVED\n")
            else:
                print(t + ", NOT IN LIST\n")
        else:
            print("No element to remove\n")
    elif n == 3:
        if len(task) > 0:
            print(sorted(task))
            print("\n")
        else:
            print("No such element\n")
    elif n == 4:
        file = open(fileName, "w")
        file.write("\n".join(task))
        file.close()
        print("TERMINATED\n")
        break
    else:
        print("Command error\n")