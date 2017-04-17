from node import Node
import math

def ID3(examples, default):
  for example in examples:
	for key in example.keys():
		if example[key] == '?':
			example[key] = handleMissingAttribute(examples, key, example['Class'])
  return ID3Wrapped(examples, default, True)

def ID3Wrapped(examples, default, noMissingdata):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  if examples is None:
	df = Node()
	df.label = default
	return df
  if ifSameClass(examples):
	ret = Node()
	ret.label = examples[0].get('Class')
	return ret
  if ifNoAttribute(examples):
	return mostCommonClass(examples)
  else:
	node = chooseAttribute(examples)
	for value in node.values:
		index = 0
		indicesSelected = []
		while index < len(examples):
			if examples[index][node.label] == value:
				indicesSelected.append(index)
			index += 1
		selectedData = []
		for i in indicesSelected:
			selectedData.append(examples[i])
		selectedData1 = []
		for data in selectedData:
			selectedData1.append({k: data[k] for k in list(set(data.keys()) - set([node.label]))})
		nodeSub = ID3Wrapped(selectedData1, default, True)
		node.children[value] = nodeSub
	return node	
			
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
  numOfCorrectCls = 0.0
  for example in examples:
	if example['Class'] == evaluate(node, example):
		numOfCorrectCls += 1.0
  return numOfCorrectCls / len(examples)


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
  if node is None or node.label is None:
	return "Cannot classify the given example."

  ret = ''
  if node.children == {}:
	return node.label
  for child in node.children:
	if child == example.get(node.label):
		ret = evaluate(node.children[child], example)
  return ret
  
def ifSameClass(examples):
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

def ifNoAttribute(examples):
	ret = True
	for key in examples[0].keys():
		if examples[0][key] != 'Class':
			ret = False
	return ret

def mostCommonClass(examples):
	clses = dict()
	for example in examples:
		if clses.has_key(example.get('Class')):
			clses[example.get('Class')] += 1
		else: 
			clses[example.get('Class')] = 1	
	mostCommonCls = max(clses.values())
	ret = Node()
	ret.label = mostCommonCls
	return ret

def handleMissingAttribute(examples, attribute, cls):
	map = dict()
	for example in examples:
		if example['Class'] == cls:
			if map.has_key(example[attribute]):
				map[example[attribute]] += 1
			else:
				map[example[attribute]] = 1
	mostCommonAttCnt = max(map.values())
	mostCommonAtt = ''
	for att in map.keys():
		if map[att] == mostCommonAttCnt:
			mostCommonAtt = att
	if mostCommonAtt == '?':
		for att in map.keys():
			if att != mostCommonAtt:
				mostCommonAtt = att
	return mostCommonAtt
  
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
   
def chooseAttribute(examples):
	rt = Node() 
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
			etp += atts.get(att)[value] * calcTargetEntropy(examples, att, value)
		eTx[att] = eT - etp
		etp = 0.0
	
	infoGainMax = max(eTx.values())
	for attr in eTx.keys():
		if eTx[attr] == infoGainMax:
			rt.label = attr
	
	for att in atts:
		if (att == rt.label):
			for value in atts.get(att):
				rt.values.append(value)
				
	return rt

		
	
  
	
		
   
		
		
	
   
	