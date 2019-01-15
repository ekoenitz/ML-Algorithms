import math
import random

# Assumes array of 2D data with format (label, value1, value2)
def perceptronTrain(data, iterations):
  weights = [0, 0]
  bias = 0
  for i in range(0, iterations):
    random.shuffle(data)
    for instance in data:
      prediction = bias
      prediction += weights[0] * instance[1]
      prediction += weights[1] * instance[2]
      if (instance[0] * prediction) <= 0:
        weights[0] += instance[0] * instance[1]
        weights[1] += instance[0] * instance[2]
        bias += instance[0]
  return (weights, bias)
  
def perceptronPredict(perceptron, instance):
  weights = perceptron[0]
  bias = perceptron[1]
  
  prediction = bias
  prediction += weights[0] * instance[0]
  prediction += weights[1] * instance[1]
  return prediction >= 0
  
  
if __name__ == '__main__':
  trainData = []
  trainData.append([1, 1, 1])
  trainData.append([1, -1, 1])
  trainData.append([1, -20, 5])
  trainData.append([-1, 11, -1])
  trainData.append([-1, 5, -31])
  trainData.append([-1, 89, -11])
  
  perceptron = perceptronTrain(trainData, 10)
  print(perceptronPredict(perceptron, [-30, 1]))