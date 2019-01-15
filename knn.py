import math
  
def euclideanDistance(tupleA, tupleB):
  distance = 0
  for x in range(0, len(tupleA)):
    distance += (tupleA[x] - tupleB[x]) ** 2
  return math.sqrt(distance)
 
"""
Expected Input:
trainData = List of tuples that go: (Label, featureValue1, featureValue2...)
dataToLabel = Tuple that goes: (featureValue1, featureValue2...)
k = Integer between 1 and len(trainData)
""" 
def knnPredict(trainData, dataToLabel, k):
  S = []
  for data in trainData:
    S.append((euclideanDistance(data[1:], dataToLabel), data[0]))
  S.sort()
  
  yHat = 0
  for x in range(0, k):
    if S[x][1]:
      yHat += S[x][0]
    else:
      yHat -= S[x][0]
  return yHat >= 0
  
if __name__ == '__main__':
  trainData = []
  trainData.append((False, -1, 0, 0))
  trainData.append((False, -1, -1, 0))
  trainData.append((False, -1, -1, -1))
  trainData.append((False, 0, 0, -1))
  trainData.append((False, -1, 0, -1))
  trainData.append((True, 0, 0, 0))
  trainData.append((True, 5, 0, 0))
  trainData.append((True, 1, 2, 3))
  trainData.append((True, 6, 4, 2))
  trainData.append((True, 0, 1, 1))
  
  dataToLabel = (40, 40, 40)
  print (knnPredict(trainData, dataToLabel, 3))