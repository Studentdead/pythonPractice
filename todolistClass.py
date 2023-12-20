import os

directory_path = "/home/sugamdahal/PycharmProjects/pythonProject/folder/todos"
class todos:
    name = ""


    def __init__(self, name):
        self.name = name
        self.todoList = None
        try:
            file = open(directory_path+f"/{name}.txt","r+")
            self.todoList = file.readlines()
            file.close()
        except FileNotFoundError:
            file = open(directory_path+f"/{name}.txt","w+")  # Open in write mode to create the file
            self.todoList = file.readlines()
            file.close()




    def __del__(self):
        file=open(directory_path+f"/{self.name}.txt","w")
        file.writelines(self.todoList)
        file.close()


    def add(self, value):
        self.todoList.append(value+'\n')

    def show(self):
        for index, value in enumerate(self.todoList, start=1):
            print(f"{index}.{value}",end="")

    def getTodo(self, num):
        if (self.checkBounds(num)):
            return self.todoList[num]

    def checkBounds(self, num):
        if num < len(self.todoList) and num >= 0:
            return True
        else:
            print("Value out of bounds!!!Try again")
            return False

    def edit(self, num, value):
        if self.checkBounds(num):
            self.todoList[num] = value

    def delete(self, num):
        if self.checkBounds(num):
            del self.todoList[num]

    def markComplete(self, num):
        if self.checkBounds(num):
            self.todoList[num] = '[completed]' + self.todoList[num]

    def __str__(self):
        return f"Todo list: {self.name}"

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
def main():
    print("hello")
    todo=os.listdir(directory_path)
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
                    # Get the list of files and directories in the specified path
                    contents = os.listdir(directory_path)

                    # Print the contents
                    for index, item in enumerate(contents, start=1):
                        print(f"{index}.{item.rstrip('.txt')}")

                except FileNotFoundError:
                    print(f"The specified directory '{directory_path}' does not exist.")
                except PermissionError:
                    print(f"Permission denied to access directory '{directory_path}'.")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                name=input("Select todo to use:\n")
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
                        new_todo.edit(num, input("Enter updated value: "))
                        break
                    except ValueError:
                        print("Wrong value inserted Back to menu!!")


                case '4':
                    try:
                        num = int(input("Enter the number of todo to delete:")) - 1
                        new_todo.delete(num)
                        break
                    except ValueError:
                        print("Wrong value inserted Back to menu!!")


                case '5':
                    try:
                        num = int(input("Enter the number of todo to mark Complete:")) - 1
                        new_todo.markComplete(num)
                        break
                    except ValueError:
                        print("Wrong value inserted Back to menu!!")


                case '6':
                    break

            con = input("Continue Y/N").lower()
            if con == 'n':
                del new_todo
                break



if __name__=="__main__":
    main()