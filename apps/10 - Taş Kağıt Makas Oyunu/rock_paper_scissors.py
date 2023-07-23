from random import randint
import time
#list of choices
t = ["Rock", "Paper", "Scissors"]

comp = randint(t[0,2])

player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")
    if player == comp:
        print("Tie!")
    elif player == "Rock":
        if comp == "Paper":
            print("You lose!", comp, "covers", player)
        else:
            print("You win!", player, "smashes", comp)
    elif player == "Paper":
        if comp == "Scissors":
            print("You lose!", comp, "cut", player)
        else:
            print("You win!", player, "covers", comp)
    elif player == "Scissors":
        if comp == "Rock":
            print("You lose...", comp, "smashes", player)
        else:
            print("You win!!!", player, "cut", comp)
    elif player == "q":
        print("you are finishing the program...")
        time.sleep(1)
        break
    else:
        print("The Program had an Error. Please try again...")
    player = False
    comp = randint(t[0,2])