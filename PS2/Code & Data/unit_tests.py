import ID3, parse, random
import matplotlib.pyplot as plt

def testID3AndEvaluate():
  data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]
  tree = ID3.ID3(data, 0)
  if tree != None:
    ans = ID3.evaluate(tree, dict(a=1, b=0))
    if ans != 1:
      print "ID3 test failed."
    else:
      print "ID3 test succeeded."
  else:
    print "ID3 test failed -- no tree returned"
  
def testPruning():
  data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1), dict(a=0, b=1, Class=0), dict(a=0, b=0, Class=1)]
  validationData = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1), dict(a=0, b=0, Class=0), dict(a=0, b=0, Class=0)]
  tree = ID3.ID3(data, 0)
  ID3.prune(tree, validationData)
  if tree != None:
    ans = ID3.evaluate(tree, dict(a=0, b=0))
    if ans != 0:
      print "pruning test failed."
    else:
      print "pruning test succeeded."
  else:
    print "pruning test failed -- no tree returned."

def testID3AndTest():
  trainData = [dict(a=1, b=0, c=0, Class=1), dict(a=1, b=1, c=0, Class=1), 
  dict(a=0, b=0, c=0, Class=0), dict(a=0, b=1, c=0, Class=1)]
  testData = [dict(a=1, b=0, c=1, Class=1), dict(a=1, b=1, c=1, Class=1), 
  dict(a=0, b=0, c=1, Class=0), dict(a=0, b=1, c=1, Class=0)]
  tree = ID3.ID3(trainData, 0)
  fails = 0
  if tree != None:
    acc = ID3.test(tree, trainData)
    if acc == 1.0:
      print "testing on train data succeeded."
    else:
      print "testing on train data failed."
      fails = fails + 1
    acc = ID3.test(tree, testData)
    if acc == 0.75:
      print "testing on test data succeeded."
    else:
      print "testing on test data failed."
      fails = fails + 1
    if fails > 0:
      print "Failures: ", fails
    else:
      print "testID3AndTest succeeded."
  else:
    print "testID3andTest failed -- no tree returned."

# inFile - string location of the house data file
def testPruningOnHouseData(inFile):
  withPruning = []
  withPruningAve = []
  withoutPruning = []
  withoutPruningAve = []
  data = parse.parse(inFile)
  trainingSize = 10
  while trainingSize < 300:
	for i in range(100):
		random.shuffle(data)
		train = data[:trainingSize]
		valid = data[trainingSize:]
		test = data[trainingSize:]
	  
		tree = ID3.ID3(train, 'democrat')
		acc = ID3.test(tree, train)
		#print "training accuracy: ",acc
		acc = ID3.test(tree, valid)
		#print "validation accuracy: ",acc
		acc = ID3.test(tree, test)
		#print "test accuracy: ",acc
	  
		ID3.prune(tree, valid)
		acc = ID3.test(tree, train)
		#print "pruned tree train accuracy: ",acc
		acc = ID3.test(tree, valid)
		#print "pruned tree validation accuracy: ",acc
		acc = ID3.test(tree, test)
		#print "pruned tree test accuracy: ",acc
		withPruning.append(acc)
		tree = ID3.ID3(train+valid, 'democrat')
		acc = ID3.test(tree, test)
		#print "no pruning test accuracy: ",acc
		withoutPruning.append(acc)
	#print withPruning
	#print withoutPruning
	#print "average with pruning",sum(withPruning)/len(withPruning)," without: ",sum(withoutPruning)/len(withoutPruning)
	withPruningAve.append(sum(withPruning)/len(withPruning))
	withoutPruningAve.append(sum(withoutPruning)/len(withoutPruning))
	trainingSize += 1
  num_examples = [i for i in range(290)]
  #print len(withPruningAve)
  #print len(withoutPruningAve)

  plt.title('Training curve with and without pruning')
  plt.plot(num_examples, withoutPruningAve, label="without pruning")
  plt.xlabel('Number of training examples')
  plt.plot(num_examples, withPruningAve, label="with pruning")
  plt.ylabel('Accuracy on testing set')
  plt.legend()
  plt.show()

  
 
if __name__ == '__main__':
	testPruningOnHouseData("house_votes_84.data")