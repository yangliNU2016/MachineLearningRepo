import json
import math
import numpy as np
def cos_sim(v1,v2):
	num = [0, 0, 0]	
	for i in range(len(v1)):       
		vec = [v1[i], v2[i]]
		num[0] = num[0] + vec[0] * vec[0]
		num[1] = num[1] + vec[0] * vec[1]
		num[2] = num[2] + vec[1] * vec[1]
	return num[1] / math.sqrt(num[0] * num[2])
	
def imgIdx(img):
	with open('dataset.json') as data_file:
		data = json.load(data_file)
		for index, image in enumerate(data['images']):
			if img == image:
				return index
				
'''
with open('cnn_dataset.json') as data_file:
	data = json.load(data_file)
	
	print cos_sim(data['vgg_rep']['mj1'], data['vgg_rep']['mj2'])
	print cos_sim(data['vgg_rep']['mj1'], data['vgg_rep']['cat'])
	print cos_sim(data['vgg_rep']['mj2'], data['vgg_rep']['cat'])
	print cos_sim(data['pixel_rep']['mj1'], data['pixel_rep']['mj2'])
	print cos_sim(data['pixel_rep']['mj1'], data['pixel_rep']['cat'])
	print cos_sim(data['pixel_rep']['mj2'], data['pixel_rep']['cat'])
'''

with open('dataset.json') as data_file1:
	data = json.load(data_file1)
	testingSet = data['test']
	trainingSet = data['train']
	imgPixelRep = np.load('pixel_rep.npy')
	imgVggRep = np.load('vgg_rep.npy')
	file1 = open('pixel.txt', 'w')
	file2 = open('vgg.txt', 'w')
	for testImg in testingSet:
		highestCosSim1 = -1
		idxToRecord1 = 0
		highestCosSim2 = -1
		idxToRecord2 = 0
		imgToRecord1 = ''
		imgToRecord2 = ''
		for trainImg in trainingSet:
			cosSim1 = cos_sim(imgPixelRep[imgIdx(testImg)], imgPixelRep[imgIdx(trainImg)])
			cosSim2 = cos_sim(imgVggRep[imgIdx(testImg)], imgVggRep[imgIdx(trainImg)])	
			if cosSim1 > highestCosSim1:
				highestCosSim1 = cosSim1
				idxToRecord1 = imgIdx(trainImg)
				imgToRecord1 = trainImg
			if cosSim2 > highestCosSim2:
				highestCosSim2 = cosSim2
				idxToRecord2 = imgIdx(trainImg)
				imgToRecord2 = trainImg
		caption1 = data['captions'][data['images'][idxToRecord1]]
		caption2 = data['captions'][data['images'][idxToRecord2]]
		file1.write(str(imgIdx(testImg)) + ' ' + str(imgIdx(imgToRecord1)) + ' ' + caption1 + '\n')
		file2.write(str(imgIdx(testImg)) + ' ' + str(imgIdx(imgToRecord2)) + ' ' + caption2 + '\n')
	file1.close()
	file2.close()

		
	