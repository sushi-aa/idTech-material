#most credit: https://github.com/AVIGNAN18/kingdom/blob/c669ea1ffc696c79dc9f65fbf8c5303d7ef60966/rock.py

from random import randint
t = ['Rock','Paper','Scissors']
computer=t[randint(0,2)]
player=True

while player:
    player = input("Rock, Paper, Scissors? Type Q for quit: ")

    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="paper":
            print("You lose!",computer,"covers",player)
        else:
            print("You win!",player,"smashes",computer)
    elif player=="Paper":
        if computer=="Scissors":
            print("You lose!",computer,"cut",player)
        else:
            print("You win!",player,"covers",computer)
    elif player=="Scissors":
        if computer=="Rock":
            print("You lose...",computer,"smashes",player)
        else:
            print("You win!",player,"cut",computer)

    elif player == "Q":
        player = False
        break
    else:
        print("That's not a valid play. Check your spelling!")

    player = True
    computer=t[randint(0,2)]