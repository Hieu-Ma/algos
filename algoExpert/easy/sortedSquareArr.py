def sortedSquaredArray(array):
    # Write your code here.
	copyArr = [0 for ele in array]
	
	smallestValueIdx = 0
	largestValueIdx = len(array) - 1
	
	for idx in reversed(range(len(array))):
		smallestValue = array[smallestValueIdx]
		largestValue = array[largestValueIdx]
		
		if abs(smallestValue) > abs(largestValue):
			copyArr[idx] = smallestValue * smallestValue
			smallestValueIdx += 1
		else:
			copyArr[idx] = largestValue * largestValue
			largestValueIdx -= 1
		
	return copyArr
	