from Classes import todos, get_available_todos, directory_path
def main():
    print("hello")
    todo=get_available_todos()
    new_todo=None


    while True:
        max_attempts = 3
        attempts = 0
        i=None

        while attempts < max_attempts:
            try:
                i = int(input("Select a number to perform action\n"
                              "1.Create new todolists\n"
                              "2.Use existing todolist\n"
                              "3.Exit\n"

                              ""))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")





        if i==1:
            print( "Enter name of new todolist\n")
            name = input()
            new_todo = todos(name)


        elif i==2:
            if len(todo)==0:
                print("No existing todolist\n"
                       "Enter name of new todolist\n")
                name=input()
                new_todo=todos(name)
                todo.append(name)


            else:
                try:

                    nameList=[]

                    # Print the contents
                    for index, item in enumerate(todo, start=1):
                        print(f"{index}.{item[:-4]}")
                        nameList.append(item[:-4])

                except FileNotFoundError:
                    print(f"The specified directory '{directory_path}' does not exist.")
                except PermissionError:
                    print(f"Permission denied to access directory '{directory_path}'.")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                name=input("Select todo to use:\n")
                if name not in nameList:
                    x=input("No todoList {name} found. \n"
                          "Press y to create todoList {name} or n to exit")
                    if x =='n':
                        continue
                new_todo=todos(name)






        else:
            break

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
                    data= input("Enter a todo: ")
                    new_todo.add(data)
                case '2':
                    new_todo.show()
                case '3':
                    try:
                        num = int(input("Enter the number of todo to edit:")) - 1
                        new_todo.edit(num, input("Enter updated value: ")+"\n")

                    except ValueError:
                        print("Wrong value inserted Back to menu!!")


                case '4':
                    try:
                        num = int(input("Enter the number of todo to delete:")) - 1
                        new_todo.delete(num)


                    except ValueError:
                        print("Wrong value inserted Back to menu!!")


                case '5':
                    try:
                        num = int(input("Enter the number of todo to mark Complete:")) - 1
                        new_todo.markComplete(num)

                    except ValueError:
                        print("Wrong value inserted Back to menu!!")


                case '6':
                    break

            con = input("Continue Y/N").lower()




if __name__=="__main__":
    main()



#
# class listTodos:
#     lists=[]
#     def create(self,name):
#         self.lists.append(todos(name))
#     def isEmpty(self):
#         if len(lists)==0:
#             return true
#         else:
#             return false
#     def show(self):
#         for obj in self.lists:
#             printf(f"{obj.name}")
#     def getTodo(self,name):
#         for obj in self.lists:
#             if name==obj.name:
#                 return obj