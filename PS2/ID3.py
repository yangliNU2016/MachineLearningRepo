#from node import Node
import math

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  if examples is None:
	return default
  if ifSameClass(examples):
	return examples[0].get('Class')
  buildTree(examples)
  
  

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''

def ifSameClass (examples):
  '''
  Takes an array of examples returns true if the examples have the same clssification,
  otherwise returns false
  '''
  ret = True
  clas = examples[0].get('Class')
  for item in examples:
	if item.get('Class') != clas:
		return False
  return ret
 
def calcTargetEntropy(examples, attribute, value):
   '''
   Takes an array of examples return the entropy of the target
   '''
   cls = dict()
   total = 0.0
   entropy = 0.0
   
   if value is None: 
	for example in examples:
		total += 1.0
		if cls.has_key(example.get(attribute)):
			cls[example.get(attribute)] += 1
		else:
			cls[example.get(attribute)] = 1
   else:
	for example in examples:
		if example.get(attribute) == value:
			total += 1.0
			if cls.has_key(example.get('Class')):
				cls[example.get('Class')] += 1
			else:
				cls[example.get('Class')] = 1

   for cl in cls.keys():
	cls[cl] = float("{0:.2f}".format(cls[cl] / total))

   for cl in cls.keys():
	entropy -= cls[cl] * math.log(cls[cl], 2)
   return entropy
   
def buildTree(examples):
#	rt = Node()
	eT = calcTargetEntropy(examples, 'Class', None)
	eTx = dict()
	
	atts = {}
	total = 0.0
	attNum = 0
	for attribute in examples[0].keys():
		if attribute != 'Class':
			attNum += 1
			atts[attribute] = {}
			for example in examples:
				total += 1.0
				if atts[attribute].has_key(example.get(attribute)):
					atts[attribute][example.get(attribute)] += 1
				else:
					atts[attribute][example.get(attribute)] = 1
	total = total / attNum
	
	for att in atts:
		for value in atts.get(att):
			atts.get(att)[value] /= total

	
	etp = 0.0		
	for att in atts:
		for value in atts.get(att):
			print calcTargetEntropy(examples, att, value)
			etp += atts.get(att)[value] * calcTargetEntropy(examples, att, value)
		eTx[att] = eT - etp
		etp = 0.0
	print eTx
		
	

	'''
	for attribute in examples[0]:
		if attribute != 'Class':
			
			calcTargetEntropy(examples, attribute)
			#eTx[attribute] = eT - calcTargetEntropy(examples, attribute)
	'''
	
  
	
		
   
		
		
	
   
	