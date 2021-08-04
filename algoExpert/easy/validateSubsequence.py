"""
Clarifying the prompt

check if the sequence is inside the array and is in correct order
"""

"""
I/O and Edge cases

I : array = [1, 2, 3 ,4] sequence = [1, 3, 4]
O : True

I : array = [1, 4, 3, 2] sequence = [1, 3, 4]
O : False

"""

"""
Approach
	TC O(n) SC O(1)
	Stack
	
"""

"""
PsuedoCode
	loop through array starting from the end
		if sequence is empty return True
		if arrayIndex is equal to last item in seq
			sequence.pop
	return False
"""

def isValidSubsequence(array, sequence):
    # Write your code here.
	for i in range(len(array) - 1, -1, -1):
		if sequence[len(sequence) - 1] == array[i]:
			sequence.pop()
		if len(sequence) == 0: return True
	return False
    # pass

"""
Optimal Solution O(n) time | O(1) space

def isValidSubsequence(array, sequence):
    # Write your code here.
	seqIdx = 0
	print(len(sequence))
	for value in array:
		if seqIdx == len(sequence):
			break
		if sequence[seqIdx] == value:
			seqIdx += 1
    return seqIdx == len(sequence)


"""