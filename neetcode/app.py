


tasks = input("Enter Item Here. \n")
todoList = {tasks}


user_change = input("Would you like to make a change? Yes or No?\n")


def remove_function(): 
    print("Here are the Items:\n", tasks)
    removeTask = todoList.remove(input("Which Item to Remove? \n"))
    return todoList
   
def add_function():
    #print("Here are the current Items:\n", tasks)
    addTask = todoList.add(input("What would you like to add?\n"))
    return todoList



while user_change.upper() == "YES":
    add_function()
    addMore = input("Add More Items?\n Yes or No? \n")
    print(todoList)
    if addMore.upper() == "NO":
        break







#if user_change.upper() == "YES":
 #   userChoice = input("Would you like to do add or remove? \n")
 #   if userChoice.upper() =="ADD":
  #      add_function()
        
  #  else: 
  #      remove_function()











