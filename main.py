# Import the random module
import random

# Define a dictionary of card values
card_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}

# Define a list of all the possible cards in a deck
deck = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
]

# Define a function to shuffle the deck
def shuffle_deck():
    random.shuffle(deck)

# Define a function to deal a card
def deal_card():
    return deck.pop()

# Define a function to calculate the total value of a player's hand
def calculate_hand(hand):
    total = 0
    aces = 0
    # Loop over each card in the hand
    for card in hand:
        # If the card is an Ace, increment the aces counter
        if card == "A":
            aces += 1
        else:
            # Add the value of the card to the total
            total += card_values[card]
    # Loop over the aces in the hand
    for _ in range(aces):
        # If the total plus an Ace would bust the player, make the Ace worth 1
        if total + 11 > 21:
            total += 1
        else:
            # Otherwise, make the Ace worth 11
            total += 11
    return total

# Define a function to play a game of blackjack
def play_blackjack():
    # Shuffle the deck
    shuffle_deck()
    # Deal the player and the dealer their initial hands
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    # Print the player's initial hand
    print("Your hand:")
    print(player_hand)
    # Print the dealer's initial hand
    print("Dealer's hand:")
    print(dealer_hand[0])
    print("???")
    # Calculate the initial totals for the player and the dealer
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    # Check if the player has blackjack (21)
    if player_total == 21:
        print("You have blackjack! You win")
