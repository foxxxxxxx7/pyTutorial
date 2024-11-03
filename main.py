# Python program to shuffle a deck of cards

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1, 15), ['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# mapping for special card values
value_map = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A'
}

# draw five cards
print("You got:")
for i in range(5):
    # get the card value, check if it's in the map, otherwise use the number
    value = value_map.get(deck[i][0], deck[i][0])
    print(value, "of", deck[i][1])
