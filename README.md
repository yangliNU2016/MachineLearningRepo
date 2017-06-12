# Hyperparameter Optimaztion of Convolutional Neural Networks (CNN) on Digit Recoginition Task

**Yang Li**

**yangli2016@u.northwestern.edu**

**EECS 349 Northwestern University**
  
## Abstract
  
### Task
The task of this project is to optimize hyperparameters of CNN to maximize the testing accuracy of hand-written digit recognition. Hand-written digits recognition is important. People often scratch numbers with their fingers on phones, tablets, and other mobile devices, and it makes handwritten digits recognition a key feature of mobile devices. Another application that handwritten digit recognition comes into play is auto-grading exams. Being able to correctly and quickly recognize handwritten digits is essential for a lot of applications not just the two mentioned above.

### Learner and Features
In this project, I use CNN to train and test on MNIST dataset which is developed for evaluating machine learning moodels on hand-written digit recognition problem. Five hyperparameters to optimize are: learning rate, training iterations, batch size, display steps, and dropout.    

### Show of Work
![Image](https://github.com/yangliNU2016/MachineLearningRepo/blob/master/Course%20Project/Pics%26Paper/table.png)

Here is the output table. I manage to optimize the above five hyperparameters to achieve a testing accuracy 0.988281. Here are some observations:

- To achieve decent testing accuracies avoid too big or too small learning rates. 
- To achieve decent testing accuracies make training iterations big and batch size small.
- Display steps does not have any obvious influences on testing accuracies.
- From 0 to 1 the bigger the dropouts are the better training accuracies are; from 1 to infinity the bigger the dropouts are the worse training accuracies are.  

### Details and Code
Paper: [Link](https://github.com/yangliNU2016/MachineLearningRepo/blob/master/Course%20Project/Pics%26Paper/hyperparameter-optimazation-convolutional.pdf)
Code: [Link](https://github.com/yangliNU2016/MachineLearningRepo/tree/master/Course%20Project/NeuralNetworks)


```markdown


# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
