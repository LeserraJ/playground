import random

#array of choices
throws = ["rock","paper","scissor"]

#computer choice
comp_throw = random.choice(throws)

#user choice
user_throw = (input("What do you want to throw?\n Rock, Paper, or Scissor?\n"))






#Rock functionality
def rock_function():
    if user_throw == throws[0] and comp_throw == throws[0]:
        print("tie")
    elif comp_throw == throws[1]:
        print("lose")
    else:
        print("win")

#Paper functionality
def paper_function():
    if user_throw == throws[1] and comp_throw == throws[1]:
        print("tie")
    elif comp_throw == throws[2]:
        print("lose")
    else:
        print("win")


#Scissor functionality
def scissor_function():
    if user_throw == throws[2] and comp_throw == throws[2]:
        print("tie")
    elif comp_throw == throws[0]:
        print("lose")
    else:
        print("win")




if user_throw == throws[0]:
    rock_function()
elif user_throw == throws[1]:
    paper_function()
elif user_throw == throws[2]:
    scissor_function()
else:
    print("No Choice")

    









