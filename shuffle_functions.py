import random
import numpy as np
from statsmodels.sandbox.stats.runs import runstest_1samp

def move_chunk_from_end(deck, start):
		"""
		Moves a sub-deck to the beginning of the deck in several chunks
		:param deck: deck at the start
		:param start: a card (number) with which you start shuffling
		:return: shuffled deck and a new start value
		"""
		n = len(deck)
		sub_deck = deck[n - start:]
		print(sub_deck, "- sub-deck; length", len(sub_deck))

		k = random.randint(5, 7)
		if k > len(sub_deck):
			k = len(sub_deck)

		print(k, "cards moved to the beginning of the deck")

		chunk = deck[n - start : n - start + k]
		del deck[n - start : n - start + k]
		deck[0:0] = chunk

		start -= k
		return deck, start

def inversions_test(arr):
		"""
		Count the number of inversions in 'arr'.
		An inversion is a pair (i, j) where i < j and arr[i] > arr[j].
		then estimate a randomness of the deck.
		"""
		inversions = 0
		n = len(arr)

		for i in range(n):
			for j in range(i+1, n):
				if arr[i] > arr[j]:
					inversions += 1

		expected = len(arr) * (len(arr) - 1) / 4  # Expected inversions for a random permutation

		# Heuristic check:
		ratio = inversions / expected
		if 0.8 < ratio < 1.2:
#			print("Inversion count is near the theoretical mean — looks fairly random.")
			rand_test_2 = 1
		else:
#			print("Inversion count significantly deviates from the mean — possible non-randomness.")
			rand_test_2 = 0

		return rand_test_2

def runs_test(deck):
	"""
	Does runs test on an array to check how well it was shuffled
	"""
	# Convert deck into a numpy array for convenience
	deck_array = np.array(deck)

	# We'll define a threshold (median, for instance, is around 38 or 39)
	median_value = np.median(deck_array)
	# Transform each card to 0 (below median) or 1 (above or equal to median)
	binary_sequence = (deck_array >= median_value).astype(int)

	# Apply the runs test
	z_stat, p_value = runstest_1samp(binary_sequence, cutoff='mean')
	# Alternatively, you could supply a numeric cutoff or use 'median' parameter.

	if p_value < 0.05:
#		print("There is statistically significant evidence this deck is NOT random.")
		rand_test_1 = 0
	else:
#		print("No strong evidence against randomness (by runs test).")
		rand_test_1 = 1

	return rand_test_1

