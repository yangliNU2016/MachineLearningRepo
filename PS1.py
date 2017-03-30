# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - dictionary containing the children where the key is child number (1,...,k) and the value is the actual node object
# if node has no children, self.children = None
# value - value at the node
#
#
# The values for bfs should be returned as simply a string of value space value space value. For example if the tree looks like the following:
#     5
#   2   3
#
# The tree data structure is a node with value 5, with a dictionary of children {1: b, 2: c} where b is a node with value 2 and c is a node with value 3.  Both b and c have children of None.
# The bfs traversal of the above tree should return the string '5 2 3'
class Node:
	def __init__(self):
		self.value = None
		self.children = None

	def get_value(self):
		
		'''
		given a node, will return the value at this node
		'''
		return self.value


	def get_children(self):
		
		'''
		given a node, will return the children of this node
		'''
		return self.children
		
	
def breadth_first_search(root):
	
	'''
	given the root node, will complete a breadth-first-search on the tree, returning the value of each node in the correct order
	'''
	ret = ''
	if root.value != None:
		ret += str(root.get_value()) + ' ' 
	if root.children != None:
		for key, child in root.children.iteritems():
			ret += str(child.get_value()) + ' '
		for key, child in root.children.iteritems():
			breadth_first_search(child)
	return ret[:-1]

def tester():
	a = Node()
	a.value = 5
        b = Node()
	b.value = 7
	a.children = {1: b}
	print str(a.get_value()) + ' should be 5.'
	print str(a.get_children()) + ' should be {1: ' + str(b) + '}.'
	print str(breadth_first_search(a)) + ' should be 5 7.'
	
if __name__ == "__main__":
    tester()