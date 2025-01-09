import random

# Import the 3 functions
from shuffle_functions import move_chunk_from_end, inversions_test, runs_test

def main():

	deck = list(range(78)) # 78 cards deck
	shuffles = 0
	rand_test_1 = runs_test(deck)				# rand_test_1 should be 0, the deck is not shuffled
	rand_test_2 = inversions_test(deck)	# same for rand_test_2

	while not (rand_test_1 == 1 and rand_test_2 == 1):

		start = random.randint(25, 35) # here we randomly pick a sub-deck 
		while start > 0:
			deck, start = move_chunk_from_end(deck, start)
			print(deck)
			print(start, "new position\n")
	
		shuffles += 1
		print(shuffles)

		rand_test_1 = runs_test(deck)
		rand_test_2 = inversions_test(deck)

	print("The deck was shuffled randomly after",shuffles,"number of iterations")	

if __name__ == "__main__":
	main()


#TODO:
# add return to main
# write a wrapper to call this script and evaluate an average number of shuffles
