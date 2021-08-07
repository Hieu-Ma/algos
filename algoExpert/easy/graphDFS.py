# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.

"""
Clarification

do a depth first search and store each node as we traverse
"""

"""
Approach 
	We could solve this "recursively"
	we iterate through each node's children
	and as we go through each node's children we append
"""

"""
Psuedo Code 
	push current node into array
	iterate through current node's children
		call depth first search on child
"""
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		return array