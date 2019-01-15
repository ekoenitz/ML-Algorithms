import math
import random
  
def euclideanDistance(tupleA, tupleB):
  distance = 0
  for x in range(0, len(tupleA)):
    distance += (tupleA[x] - tupleB[x]) ** 2
  return math.sqrt(distance)
  
def kMeansInitialize(trainData, k):
  centers = []
  for i in range(0, k):
    new_center = random.choice(trainData)
    while new_center in centers:
      new_center = random.choice(trainData)
    centers.append(new_center)
  return centers
    
def kMeansAssignCluster(centers, data):
  assignment = centers[0]
  bestDist = euclideanDistance(centers[0], data)
  for center in centers:
    newDist = euclideanDistance(center, data)
    if newDist < bestDist:
      bestDist = newDist
      assignment = center
  return assignment
  
def getListOfDataInCluster(data, clusterAssignments, cluster):
  dataInCluster = []
  for i in range(0, len(data)):
    if clusterAssignments[i] == cluster:
      dataInCluster.append(data[i])
  return dataInCluster
  
def getAverage(listOfTuples):
  average = []
  for i in range(0, len(listOfTuples[0])):
    dimensionAverage = 0
    for tuple in listOfTuples:
      dimensionAverage += tuple[i]
    average.append(dimensionAverage/len(listOfTuples))
  return average
  
def kMeansTrain(trainData, k):
  clusterAssignments = [None]*len(trainData)
  centers = kMeansInitialize(trainData, k)
  centersChanged = True
  while centersChanged:
    for n, data in enumerate(trainData):
      clusterAssignments[n] = kMeansAssignCluster(centers, data)
    for i in range(0, k):
      dataInCluster = getListOfDataInCluster(trainData, clusterAssignments, centers[i])
      print("Center", i, centers[i])
      new_center = getAverage(dataInCluster)
      if new_center == centers[i]:
        centersChanged = False
      else:
        centers[i] = new_center
  return clusterAssignments
    
  
if __name__ == '__main__':
  trainData = []
  trainData.append((-1, 0, 0))
  trainData.append((-1, -1, 0))
  trainData.append((-1, -1, -1))
  trainData.append((0, 0, -1))
  trainData.append((-1, 0, -1))
  trainData.append((0, 0, 0))
  trainData.append((5, 0, 0))
  trainData.append((1, 2, 3))
  trainData.append((6, 4, 2))
  trainData.append((0, 1, 1))
  
  print(kMeansTrain(trainData, 2))