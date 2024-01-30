import random

# Define suits and ranks
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# Task 1: Create a deck of cards
Deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# Display the deck and its size
print(Deck)
print(f"There are {len(Deck)} cards in the deck.")

# Task 2: Simulate dealing 5 cards
print("Dealing ...")
hand = random.sample(Deck, 5)

# Remove the dealt cards from the deck
Deck = [card for card in Deck if card not in hand]

# Display the remaining cards in the deck and the player's hand
print(f"There are {len(Deck)} cards in the deck.")
print("Player has the following cards in their hand:")
print(hand)

# Task 3: Write all 52 cards to Text1.txt
with open("Text1.txt", "w") as file:
    for card in Deck:
        file.write(card + "\n")

# Display total number of lines in the file
with open("Text1.txt", "r") as file:
    lines = file.readlines()
print(f"Total number of lines in Text1.txt: {len(lines)}")

# Task 4: Read Text1.txt, store cards in a dictionary with corresponding key number
try:
    with open("Text1.txt", "r") as file:
        card_dict = {i: line.strip() for i, line in enumerate(file)}
    print(card_dict)
except FileNotFoundError:
    print("File not found. Please make sure Text1.txt exists.")

# Task 5: Read Text1.txt, store cards in a list of tuples
try:
    with open("Text1.txt", "r") as file:
        card_list = [(i, line.strip()) for i, line in enumerate(file)]
    print(card_list)
except FileNotFoundError:
    print("File not found. Please make sure Text1.txt exists.")
