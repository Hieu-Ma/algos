"""
Approach

To implement bubble sort, we need to do a double for loop
The outer loop goes from 0 to the length of the array - 1
this is to repeat the shifting of numbers for the inner loop

TC O(n^2) | SC O(1)
"""
"""
Psuedo Code 

for(i = 0; i < array.length; i++) {
	for(i = 0; i < array.length; i++) {}
}

for i in array:
	for j in range(len(array) - 2):
		if array[j] > array[j + 1]:
			let numToSwap = array[j + 1]
			array[j + 1] = array[j]
			array[j] = numToSwap
return array
			

"""


def bubbleSort(array):
    # Write your code here.

	isSorted = False
	counter = 0
	while isSorted is False:
		isSorted = True
		for j in range(len(array) - 1 - counter):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				isSorted = False
		counter += 1
	return array
