"""
Approach

selection sort is a sorting algorithm where we compare every number
we select the lowest number
and swap it between that number and the current index
TC O(n^2) | SC O(1)

"""
"""
Psuedo Code
store lowest number
loop through entire array
	loop through, find lowest number, replace it with index at first loop
return array

"""

def selectionSort(array):
    # Write your code here.
	# lowest = array[0];
	for i in range(len(array)):
		lowest = array[i]
		lowestIndex = i
		for j in range(i + 1, len(array)):
			if(array[j] < lowest):
				lowest = array[j]
				lowestIndex = j
		array[i], array[lowestIndex] = array[lowestIndex], array[i]
	return array
