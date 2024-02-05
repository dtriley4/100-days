# 2-5-2024 Alexander: Udemy Python / Time to complete project == 1 hr
# Overview: Higher or Lower Game Project

# Build a game program that compares who has more followers on IG.
# If user guesses correctly, then continue the game and keep track of the score (streak)
# The winning comparison gets recylced into the next comparioson
# For example, A vs B, B wins, now B becomes A.
# If user guesses wrong, the game ends and displays the score streak



import random
from game_data import data

#data list variables
# 'name': '',
# 'follower_count': ,
# 'description': '',
# 'country': ''


def higher_or_lower(profile1, profile2):
    """
    Comapres instagram followers and allows user to guess which profile (A/B) has more. 
    Returns True is user guesses correctly, and returns False if inccorect
    """

    print(f"Current score: {score}")
    print(f"A:{profile1['name']}, a {profile1['description']} from {profile1['country']} \nVS. \nB:{profile2['name']}, a {profile2['description']} from {profile2['country']}")
    guess = input(f"Which has a higher follower count? A or B? ").upper()

    return (guess == 'A' and profile1['follower_count'] > profile2['follower_count']) or \
           (guess == 'B' and profile1['follower_count'] < profile2['follower_count'])

def game():
    global score
    score = 0   
    winning_profile = None

    while True:
        if winning_profile is not None:
            profile1 = winning_profile
        else:
            random.shuffle(data)
            index1 = random.randint(0, len(data) - 1)
            profile1 = data[index1]

        # Create a radnom index for profile2 that is differant that profile1
        index2 = random.randint(0, len(data) - 1)
        while index2 == index1:
            index2 = random.randint(0, len(data) - 1)
        profile2 = data[index2]

        correct_guess = higher_or_lower(profile1, profile2)

        if correct_guess:
            score += 1 
            print(f"Correct! Your current score is: {score}")
            winning_profile = profile1
        else:
            print(f"Sorry, you lose! Your final score is: {score}")
            break

game()