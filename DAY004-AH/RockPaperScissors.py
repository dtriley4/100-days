# 1-4-2024 Alexander: Udemy Python / Time to complete project == 30 mins
# Overview: Randomisation and Python Lists
 
# DAY 4 Project: Rock Paper Scissors 

#Checklist:
#1. Create greeting
#2. Create choices
#3. Store user and computer selection
#4. Compare selections and whoose winner or draw


import random
print("Play Rock, Paper, Scissors against your computer")

choices = ["rock", "paper", "scissors"]

#user choice
user_choice = input("What do you choose? Type rock, paper, or scissors. ")
user_choice = user_choice.lower()
print("You picked: " + user_choice)

#computer choice
computer_choice = random.choice(choices)
print("Computer picked: " + computer_choice)

#determine winner with condiotional statements 
if computer_choice == user_choice:
    print("No winners or loosers here.")
elif (
    (user_choice == 'rock' and computer_choice == 'scissors') or
    (user_choice == 'paper' and computer_choice == 'rock') or
    (user_choice == 'scissors' and computer_choice == 'paper')
):
    print("Congrats, you beat a machine!")
else:
    print("Damn. You lost to a peice of metal!")