# Text-based Blackjack
#Import necessary libraries
import random
import os

# Define a clear/reset function
def clear():
    os.system('cls||clear')

# Define a function to allow the user to play again or quit
def restart_game(player_response):
    while player_response == 0:

    # The lower() function makes sure the user input is always lowercase when read by the system
        player_response = str(input("Do you want to play again? [Y]es/[N]o/[M]aybe").lower())
        if player_response == "y" and __name__ == '__main__':
            clear()
            start_game()

        # If the player chooses to quit, the program will quit
        elif player_response == "n":
            print()
            print("Bye! See you next time!")
            exit()

        # Create a 'maybe' option that tells the user to play again, and then loops the 'play again' question
        elif player_response == 'm':
            print()
            print("You know you want to play :)")
            print()
            player_response = 0

    # Create an alternate response that activates when the user goes into an unlucky situation
    if player_response == 1:
        print("That's some bad luck. As they say, second time's the charm ;)")
        print()
        player_response = str(input("Do you want to play again? [Yes]/[No]").lower())
        if player_response == "yes" and __name__ == '__main__':
            clear()
            start_game()
        elif player_response == "no":
            print()
            print("Bye! See you next time!")
            exit()

def start_game():
    # Create the player hand, dealer hand, and the deck of cards
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4
    dealer_hand = []
    player_hand = []

    # Starts the Game
    clear()
    print("Welcome to Black Jack")
    print()

    # Add cards to the dealer's hand and print the value of the second card in the terminal
    while len(dealer_hand) != 2:
        random.shuffle(deck)
        dealer_hand.append(deck.pop())
        if len(dealer_hand) == 2:
            # Only shows the second card in the dealer's hand
            print("The dealer shows [X] &", dealer_hand[1])

    # If the sum of the dealer's hand is less than 14, the dealer will hit their card hand and increase their card count by 1
    if sum(dealer_hand) < 14:
        random.shuffle(deck)
        dealer_hand.append(deck.pop())
        # Only shows the user the second and third cards in the dealer's hand
        print("The dealer hit and now shows [X],", dealer_hand[1],"& ", dealer_hand[2])

    # Add cards to the player's hand and print the value of both cards in the terminal
    while len(player_hand) != 2:
        random.shuffle(deck)
        player_hand.append(deck.pop())
        if len(player_hand) == 2:
            print("You have ", player_hand)
    
    # Define possible Win/Lose conditions for the dealer without needing the player's hand
    # Find and display the sum of the Dealer's hand
    if sum(dealer_hand) == 21:
        print("The Dealer has a Blackjack and Wins!")
        print()
        restart_game(1)
    elif sum(dealer_hand) > 21:
        print("The Dealer got over 21 and Busted!")
        print()
        restart_game(0)

    # Define other possible Win/Lose conditions for the player after comparing with the dealer's hand
    # Find and display the sum of the Player's hand
    while sum(player_hand) < 21:
        # Allows the user to either add a card to their hand or stay with the cards they currently have.
        player_response = str(input("Do you want to [S]tay or [H]it? ").lower())
        if player_response == "h":
            random.shuffle(deck)
            player_hand.append(deck.pop())
            print("You now have a total of " + str(sum(player_hand)) + " from these cards ", player_hand)
            print()
        else:
            print("The dealer has a total of " + str(sum(dealer_hand)) + " with ", dealer_hand)
            print("You have a total of " + str(sum(player_hand)) + " with ", player_hand)
            if sum(dealer_hand) > sum(player_hand):
                print("You lost. The dealer wins!")
                print()
                # Each restart_game() function allows the user to continuously play Blackjack without needing to manually restart the program
                restart_game(0)
            elif sum(dealer_hand) == sum(player_hand):
                print("You tied with the dealer. No one wins!")
                print()
                restart_game(1)
            elif sum(player_hand) > sum(dealer_hand):
                print("You win!")
                print()
                restart_game(0)

    # Define possible Win/Lose conditions for the player without needing the dealer's hand
    if sum(player_hand) > 21:
        print("You BUSTED! Dealer wins.")
        print()
        restart_game(1)
    elif sum(player_hand) == 21 and len(player_hand) == 2:
        print("You have Blackjack! Congrats, You Win!")
        print()
        restart_game(0)
    elif sum(player_hand) == 21 and len(player_hand) != 2:
        print("You got 21! Congrats, You win!")
        print()
        restart_game(0)

# Start the Blackjack game using the previously defined start_game() procedure
start_game()