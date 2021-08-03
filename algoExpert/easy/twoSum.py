# Clarification: We want to find two numbers that add up to the target sum
# Sample I/O:
"""
input: array, targetSum

ex 1:  Array [1, 2, 3, 4, 5] targetSum 5
		return [2, 3]
"""
"""
Approach:

1st approach (O(n^2))
	double for loop
	
2nd approach T: O(n) SC: O(n)
	hash table
"""

"""
Psuedo Code
	hashTable = {}
	for num in hashTable:
		if targetSum - num in array:
			return [targetSum, targetSum - num]
		else:
			hashTable[targetSum - num] = True;
	return []
"""


def twoNumberSum(array, targetSum):
    # Write your code here.
	hashTable = {}
	for num in array:
		if targetSum - num in hashTable:
			return [num, targetSum - num]
		else:
			hashTable[num] = True;
	return []

"""
def twoNumberSum(array, targetSum):
    # Write your code here.
	nums = {}
	for num in array:
# 		potentialSum = targetSum - num
# 		if potentialSum in nums
		if targetSum - num in nums:
			return [targetSum - num, num]
		else:
			nums[num] = True;
	return []
"""