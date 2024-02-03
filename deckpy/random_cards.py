import random
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# Answer 1
def deck():
    cardList = [y+ " of "+ x for x in suits for y in ranks]
    return cardList

def play(cards):
    print("Dealing ...")
    player = random.choices(cards, k=5)
    for k in player:
        cards.remove(k)
    print("There are " , len(cards) ," cards in the deck.")
    print("Player has the following cards in their hand: ")
    return player

decks = deck()
print(decks)
print(play(decks))
# Answer 2

with open('Text1.txt', 'w+') as f:
    deck = deck()
    for i in deck:
        f.writelines(i + '\n')
    print(len(deck))
    f.close()

# Answer 3

try:
    with open('Text1.txt', 'r') as f:
        card_dict = {}
        for key, line in enumerate(f):
            card_dict[key] = line.strip()
        print(card_dict)

except FileNotFoundError:
    print("File not found. Please make sure 'Text1.txt' exists.")
except Exception as e:
    print(f"An error occurred: {e}")

# Answer 4

try:
    with open('Text1.txt', 'r') as f:
        cards_list = [(key, line.strip()) for key, line in enumerate(f)]
    print(cards_list)
except FileNotFoundError:
    print("File not found. Please make sure 'Text1.txt' exists.")
except Exception as e:
    print(f"An error occurred: {e}")