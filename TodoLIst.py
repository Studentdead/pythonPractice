#without using classes
file = open('todos.txt', 'r')
todos = file.readlines()
file.close()
while True:
    user_action = input("------Select a number to perform action-----\n"
                        "1.Add\n"
                        "2.Show\n"
                        "3.Edit\n"
                        "4.Delete\n"
                        "5.Mark as Complete\n"
                        "6.Exit\n")

    match user_action:
        case '1':
            todo = input("Enter a todo: ")+'\n'
            todos.append(todo)

        case '2':
            for index,i in enumerate(todos,start=1):
                print(f"{index}. {i}",end="")
        case '3':
            num=int(input("Enter the number of todo to edit:"))-1
            if num<=len(todos) and num>=0:
                value=input("Enter updated value: ")
                todos[num]=value
            else:
                print("Invalid number>>>")
        case '4':
            num = int(input("Enter the number of todo to delete:")) - 1
            if num <= len(todos) and num > 0:
                todos.remove(todos[num])
            else:
                print("Invalid number>>>")

        case '5':

           num = int(input("Enter the number of todo to mark Complete:")) - 1
           if num <= len(todos) and num >= 0:
                todos[num]='[Completed]'+todos[num]
           else:
                print("Invalid number>>>")


        case '6':
            break
    file = open('todos.txt', 'w')
    file.writelines(todos)
    file.close()

    con= input("Continue Y/N").lower()
    if con=='n':
        break;



