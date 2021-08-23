"""
Clarification

Add the depths of each node and return sum
"""

"""
Approach

1. breadth first search
2. have a separate variable that stores the depth
3. have a separate variable that stores the sum 
4. if that node has children, add to sum, the depth
5. return sum

"""

"""
Psuedo Code
if node is None:
	return
implement queue with root value initialized in the first index
i = 0
depth = 1
sum = 0
while queue is not None:
	node = queue[i]
	if node.left is not None:
		queue.append(node.left)
		sum += depth
	if node.right is not None:
		queue.append(node.left)
		sum += depth
	depth += 1
	i++
return sum
"""
def nodeDepths(root):
    # Write your code here.
	depth = 1
	sum = 0
	queue = [root]
	while len(queue) != 0:
		node = queue[0]
		if node.left is not None:
			queue.append(node.left)
			sum += depth
		if node.right is not None:
			queue.append(node.right)
			sum += depth
		if(queue)
		queue.pop(0)
	return sum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
