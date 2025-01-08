#!/usr/local/bin/python3

import random

# create a deck of 78 cards:
deck = list(range(78))

n = len(deck)

start = random.randint(11, 17) # pick random number (11-17)
#start = 78
#print(start)

while start > 0: # do until sub-deck is empty

	sub_deck = deck[n-start:] # create of a sub-deck of a random amount of cards from the end of the deck

	print(sub_deck, "- sub-deck; length ", len(sub_deck))

	k = random.randint(5, 7) # create a number for a shuffling stack
	if k > len(sub_deck):
		k = len(sub_deck)

	print(k,"cards moved to the beginning of the deck")

	chunk = deck[n - start : n - start + k] # pick shuffling stack
	del deck[n - start : n - start + k]

	deck[0:0] = chunk # move our shuffling chunk to start fo the deck
	
	start = start - k # start position shifts towards the end of the deck

	print(deck)
	print(start,"new position")
	print("")

