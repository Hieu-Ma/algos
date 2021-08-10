"""
Clarification

implement insertion sort
"""

"""
Approach

loop through the array, for each element, we want to iterate backwards and find it's place in the array
to find the place in the array, we constantly swap between two numbers, based off of it's value
if it's < the number we swap, else no swapping is needed

[1, 3, 2]
"""

"""
Pseudo Code

for i in range(1, len(array)):
	for j in range(len(array), 0, -1):
		if array[i] < array[j]:
			array[i], array[j] = array[i], array[j]
return array
"""


def insertionSort(array):
    # Write your code here.
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j-1]  > array[j]:
			swap(j, j-1, array)
			j -= 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
	return array;