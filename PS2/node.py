class Node:
	def __init__(self):
		self.label = None
		self.children = {}
		self.values = []
		self.parent = None
		
	def getAncestors(self):
		ancestors = []
		while self.parent is not None:
			ancestors.append(self.parent.label)
			self = self.parent
		return ancestors	
		
			
	

		 