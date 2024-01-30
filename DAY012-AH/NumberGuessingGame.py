# 1-27-2024 Alexander: Udemy Python / Time to complete project == 
# Overview: Namespaces: Local vs Global Scopes


# Local scopes exist within funtions. variables are only valid inside the function block. 
# The code below will produce an undefined variable error:

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
# print(potion_strength)


# Global scope is defined outside function and are availble within and outside functions

# player_health = 10

# def drink_potion():
#      potion_strength = 2
#      print(player_health)
# drink_potion()


# There is no block scope in Python language, the scope is either local (only available inside functions) or global (named outside of functions but useable inside and outside of functions)
# If you create a variable inside anything with indentaiton and colon, it doesnt make a new seperate local scope

# game_level = 3
# def create_enemy():
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
#     print(new_enemy)


# Mpdifying global scopes, you need to explictly state inside function that you are modifyig a global scope variable

# enemies = 1 #variable as a global scope

# def increase_enemies():
#     global enemies #stating the variable we are modifying in the following function code
#     enemies += 1 #vmodifys the global scope 
#     print(f"enemies inside the function: {enemies}") #will print 2

# increase_enemies()
# print(f"enemies outside of function: {enemies}") #will print 1

### Avoid modifying global scopes inside local scope functions as they are prone to producing errors ###
### Instead you can do something like return statements, as shown in code below ###

# enemies = 1 #

# def increase_enemies():
#     print(f"enemies inside the function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies() #now it takes the return and saves it into the global function that was defined earlier above in the code
# print(f"enemies outside of function: {enemies}")

# Global Constants are variables that you never plan to change again

# PI = 3.14159 #The naming convention in Python is to turn the constant variable name into all upper case
# URL - "https://wwww.google.com"
# TWITTER_HANDLE = "@PYTHONDAD"

# def calc():
#     TWITTER_HANDLE


### PROJECT: NUMBER GUESSING GAME ###

#TODO 
# 1. Allow the player to submit a guess for a number between 1 and 100.
# 2. Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# 3. If they got the answer correct, show the actual answer to the player.
# 4. Track the number of turns remaining.
# 5. If they run out of turns, provide feedback to the player. 
# 6. Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import random

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choose a random number between 1 and 100
    answer = random.randint(1, 100)

    # Set the number of turns based on difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        if guess == answer:
            print(f"You win! You guessed the correct number of {answer}.")
            break
        elif guess < answer:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        attempts -= 1

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {answer}.")
game()