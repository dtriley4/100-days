# 1-26-2024 Alexander: Udemy Python / Time to complete project =~ 2 hours
#Overview: Blackjack Capstone Project

############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Draw a card function
def draw_card():
    return random.choice(cards)

# Calculate hand value function and Ace adjustments
def hand_value(hand):
    value = sum(hand)
    num_aces = hand.count(11)

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

# Define Blackjack hand
def is_blackjack(hand):
    return len(hand) == 2 and hand_value(hand) == 21

# Define bust hand
def is_bust(hand):
    return hand_value(hand) > 21

# Define main game function
def blackjack_game():
    print("Welcome to Blackjack, ladies and gentlemen!")
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card()]

    # Check if the player has Blackjack
    if is_blackjack(player_hand):
        print(f"Congratulations! You have Blackjack! You won with {player_hand}.")
        return

    # Player hand and action
    while True:
        print(f"Your hand is {player_hand} with a value of {hand_value(player_hand)}")
        print(f"The dealer shows a {dealer_hand[0]}")

        if is_bust(player_hand):
            print("You busted, loser!")
            break

        action = input("Type 'y' to hit, or 'n' to stay: ").lower()
        if action == 'y':
            player_hand.append(draw_card())
        elif action == 'n':
            break

    # Check if the player busted
    if is_bust(player_hand):
        return  # Do not proceed with the dealer's turn if the player busted

    # Dealer hand
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())

    # Show all hands
    print(f"Your hand is {player_hand} with a value of {hand_value(player_hand)}")
    print(f"The dealer hand is {dealer_hand} with a value of {hand_value(dealer_hand)}")

    # Determine the winner
    if is_blackjack(dealer_hand):
        print("Dealer has Blackjack! You lose :(")
    elif is_bust(dealer_hand):
        print("Dealer busts! You win!")
    elif hand_value(player_hand) > hand_value(dealer_hand):
        print("You win!")
    elif hand_value(player_hand) < hand_value(dealer_hand):
        print("You lose!")
    else:
        print("It's a draw!")

# Play again loop
while True:
    blackjack_game()

    play_again = input("Do you want to play again? Type 'y' for yes, 'n' for no: ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break
