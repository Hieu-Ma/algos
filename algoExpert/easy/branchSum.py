# This is the class of the input root. Do not edit it.

# Clarification: get the sums of each branch.

"""
Approach
	1. Create helper function that calculates each traversed node
	2. In the main function, we define the sumArr
	3. Inside helper function, we do a dfs 
	4. If we reach a node that doesn't have children, push sum into sumArr
	5. return sumArr
	O(N) O(N)
"""

"""
Psuedo Code
	sumArr = []
	calcSum(root, sum, sumArr)
	
	calcSum(root, sum, sumArr):
		newSum += sum + root.value
		
		if root.left is None and root.right is None:
			sumArr.append(newSum)
		calcSum(root.left, newSum, sumArr)
		calcSum(root.right, newSum, sumArr)
		return sumArr
"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	sumArr = []
	calcSum(root, 0, sumArr)
	return sumArr

def calcSum(root, sum, sumArr):
	if root is None:
		return
	
	newSum = sum + root.value
	
	if root.left is None and root.right is None:
		sumArr.append(newSum)
	calcSum(root.left, newSum, sumArr)
	calcSum(root.right, newSum, sumArr)
	return sumArr