'''
I have irrational fondness for Binary Search
Here's a conversational (tending to verbose) implementation. 
'''

def binary_search(my_list, key):
	# MISSION: look for key in a sorted list:my_list

	'''
	How this works:
	We follow the process of elimination - divide and conquer to be precise.
	* See how the key matches up to the midddle element of the list
	* if it's the same as the key, look no further: our job is done
	* if the key's greater, we narrow down to the second half
	* if the key's less, we check only the first half
	The previous 2 steps are pretty intuitive since our list is sorted in ascending order
	(You'll have to reverse the logic for a descending array)
	'''


	'''
	Since we don't want to butcher the original list, we'll keep track
	of the half we're interested in with indices: low and high (for the first and
	last index of the list segment we intend to search in)
	mid is the hero here - he's the index of the middle element of the list (again,
	just the part we care about)
	'''
	low = 0
	high = len(my_list) - 1
	mid = None

	while(low <= high):
		# start by finding the middle index of the list
		mid = int((low + high)/2)   						# indices are integers, don't forget!

		# now compare away
		if key == my_list[mid]:								# found at a match at the middle. Hoooray!
			print("We found", key, "at index", mid)
			return mid
		elif key < my_list[mid]:							# choose first half
			high = mid - 1
		else:
			low = mid + 1									# choose second half
	print("I'm sorry,", key, "isn't in the list")

	'''
	Neat isn't it? By updating high and low, we kept narrowing down our list
	Since we kept chopping our search list by half, the complexity is a cool O(log n)
	'''




def init():
	some_numbers = [num for num in range(10)]
	binary_search(some_numbers, 3)
	binary_search(some_numbers, 9)
	binary_search(some_numbers, 5)
	binary_search(some_numbers, 12)

init()

