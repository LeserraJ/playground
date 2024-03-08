


tasks = input("Enter Item Here. \n")
todoList = [tasks]


user_change = input("Would you like to make a change? \n")


def remove_function(): 
    print("Here are the Items:\n", tasks)
    removeTask = todoList.remove(input("Which Item to Remove? \n"))
   

if user_change.upper() == "YES":
    remove_function()
    print(todoList)
else:
    print(todoList)








