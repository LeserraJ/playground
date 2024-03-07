


tasks = input("Enter Item Here. \n")
todoList = [tasks]


def remove_function(): 
    input("Would you like to make a change? \n")
    removeTask = todoList.remove(input("Which Item to Remove? \n"))



print(todoList)