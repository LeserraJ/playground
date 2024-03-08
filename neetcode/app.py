


tasks = input("Enter Item Here. \n")
todoList = {tasks}


userInput = input("Would you like to add or remove an item? Add or Remove?\n")


def remove_function(): 
    #print("Here are the Items:\n", tasks)
    removeTask = todoList.remove(input("Which Item to Remove? \n"))
    #return todoList
    

     
   
def add_function():
    #print("Here are the current Items:\n", tasks)
    addTask = todoList.add(input("What would you like to add?\n"))
    return todoList



while userInput.upper() == "ADD":
    add_function()
    addMore = input("Add More Items?\n Yes or No? \n")
    print(todoList)
    if addMore.upper() == "NO":
        userInput = input("Would you like to add or remove an item? Add or Remove?\n")




while userInput.upper() == "REMOVE":
    remove_function()
    removeMore = input("Remove More Items?\n Yes or No? \n")
    print(todoList)
    if todoList == set():
        print("Nothing to remove.")
    if removeMore.upper() == "NO":
        userInput = input("Would you like to add or remove an item? Add or Remove?\n")





#if user_change.upper() == "YES":
 #   userChoice = input("Would you like to do add or remove? \n")
 #   if userChoice.upper() =="ADD":
  #      add_function()
        
  #  else: 
  #      remove_function()











