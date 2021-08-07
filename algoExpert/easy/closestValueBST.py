"""
Clarification

find the number closest to the target
"""

"""
Sample I/O
"""

"""
Approach
	1.Iterative
	2.While loop
	3.While we iterate, we find the value that has the smallest difference and store it as we iterate
		3.5 We do this by storing the abs value of the (current node - target value)
	4.return closestValue
"""

"""
Pseudo Code
	closestValue = None
	currentNode = tree.value
	while (currentNode is not None):
		if abs(target - currentNode) < closestValue:
			closestValue = currentNode
		if currentNode > target:
			currentNode = currentNode.left
		if currentNode < target:
			currentNode = currentNode.right
	return closestValue
"""

def findClosestValueInBst(tree, target):
	# return findClosestValueInBstHelper(tree, target)
	currentNode = tree
	closestValue = tree.value
	while currentNode is not None:
		if abs(target - currentNode.value) < abs(closestValue - target):
			closestValue = currentNode.value
		if currentNode.value > target:
			currentNode = currentNode.left
		elif currentNode.value < target:
			currentNode = currentNode.right
		else:
			break
	return closestValue

def findClosestValueInBstHelper(tree, target):
	currentNode = tree
	closestValue = tree.value
	while currentNode is not None:
		if abs(target - currentNode.value) < abs(closestValue - target):
			closestValue = currentNode.value
		if currentNode.value > target:
			currentNode = currentNode.left
		elif currentNode.value < target:
			currentNode = currentNode.right
		else:
			break
	return closestValue

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None