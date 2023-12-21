import os

# directory_path = "/home/sugamdahal/PycharmProjects/pythonProject/folder/todos"
project_root = os.path.dirname(os.path.abspath(__file__))

# Use os.path.join to construct file paths relative to the project root
directory_path = os.path.join(project_root, "todos")

# Create the directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

def get_available_todos():
    return os.listdir(directory_path)
class todos:
    name = ""


    def __init__(self, name):
        self.name = name
        self.todoList = None
        try:
            with open(directory_path+f"/{name}.txt","a+") as file:
                file.seek(0)
                self.todoList = file.readlines()

        except FileNotFoundError:
            print("Error Creating/opening file!!!\n")




    def save(self):
        with open(directory_path+f"/{self.name}.txt","w") as file:
            file.writelines(self.todoList)


    def add(self, value):
        self.todoList.append(value+'\n')
        self.save()

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
            self.save()

    def delete(self, num):
        if self.checkBounds(num):
            del self.todoList[num]
            self.save()

    def markComplete(self, num):
        if self.checkBounds(num):
            self.todoList[num] = '[completed]' + self.todoList[num]
            self.save()

    def __str__(self):
        return f"Todo list: {self.name}"
