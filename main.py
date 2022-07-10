from random import randint
t = ["rock", "paper", "scissors"]
n = t[randint(0,2)]
player=False
while player==False:
    player=input("Rock Paper or Scissors?")
    if player==n:
        print("Tie!")
    elif player=="rock":
        if n=="paper":
            print("You lose!", n,"covers",player)
        else:
            print("You win!",player,"smashes",n)
    elif player=="paper":
        if n=="scissors":
            print("You lose!",n,"cut",player)
        else:
            print("You win!",player,"covers",n)
    elif player=="scissors":
        if n=="rock":
            print("You lose!",n,"smashes",player)
        else:
            print("You win!",player,"cut",n)
    else:
        print("That is not a valid answer! Make sure there is no capital letter.")
    player=False
    n=t[randint(0,2)]