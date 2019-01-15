import math
import random

def calcKernel(a, b):
  kernel = 0
  for i in range(1, len(a)):
    kernel += a[i] * b[i]
  return math.pow(kernel, 2)

def getPrediction(alpha, bias, data, dataInstance):
  prediction = bias
  for i in range(1, len(alpha)):
    prediction += alpha[i] * calcKernel(data[i], dataInstance)
  return prediction

# Assumes array of 2D data with format (label, value1, value2)
def perceptronTrain(data, iterations):
  alpha = [0]*len(data)
  bias = 0
  for i in range(0, iterations):
    random.shuffle(data)
    for ind, instance in enumerate(data):
      prediction = getPrediction(alpha, bias, data, instance)
      if (instance[0] * prediction) <= 0:
        alpha[ind] += instance[0]
        bias += instance[0]
  return (alpha, bias)
  
def perceptronPredict(perceptron, data, instance):
  weights = perceptron[0]
  bias = perceptron[1]
  prediction = bias
  getPrediction(weights, bias, data, instance)
  return prediction >= 0
  
  
if __name__ == '__main__':
  trainData = []
  trainData.append([1, 1, 1])
  trainData.append([1, -1, 1])
  trainData.append([1, -20, 5])
  trainData.append([-1, 11, -1])
  trainData.append([-1, 5, -31])
  trainData.append([-1, 89, -11])
  
  pred = 0
  for i in range(0, 100):
    perceptron = perceptronTrain(trainData, 10)
    pred += 1 if perceptronPredict(perceptron, trainData, [0, -30, 1]) else 0
  print(pred/100)