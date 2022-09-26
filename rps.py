#rock paper scissors game.
import random

while True:
    
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? ").lower()
        
    
    if player == computer:     
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("You choose ", player)
            print("Computer picks", computer)
            print("Oops,You Lose!")
        if computer == "scissors":
            print("You choose ", player)
            print("Computer picks", computer)
            print("Yay! You win!")
            
    
        
    elif player == "paper":
        if computer == "rock":
            print("You choose ", player)
            print("Computer picks", computer)
            print("Yay! You win!")
        if computer == "scissors":
            print("You choose ", player)
            print("Computer picks", computer)
            print("Oops,You Lose!")
        
    
    elif player == "scissors":
        if computer == "rock":
            print("You choose ", player)
            print("Computer picks", computer)
            print("Oops,You Lose!")
        if computer == "scissors":
            print("You choose ", player)
            print("Computer picks", computer)
            print("Oops,You Lose!")
        
    play_again = input("Play again? (yes/no): ")
    
    if play_again != "yes":
        break

print("Bye!")
