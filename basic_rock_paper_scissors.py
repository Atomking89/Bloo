import random

human = input("Enter rock, paper, or scissors: ")
computer = random.choice(["rock", "paper", "scissors"]) 
if computer == "scissors" and human == "rock":
    print("computer wins")
elif computer == "rock" and human == "paper":
    print("human wins")
elif computer == "paper" and human == "scissors":
    print("human wins")
else:
    print("computer wins")