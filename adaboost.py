import math
  
def euclideanDistance(tupleA, tupleB):
  distance = 0
  for x in range(0, len(tupleA)):
    distance += (tupleA[x] - tupleB[x]) ** 2
  return math.sqrt(distance)
  
def trainDecisionStump(data, importance):
  bestTracker = {}
  for i in range(0, len(data)):
    xKey = 'x' + str(data[i][1])
    yKey = 'y' + str(data[i][2])
    if xKey not in bestTracker.keys():
      bestTracker[xKey] = 0.0
    if yKey not in bestTracker.keys():
      bestTracker[yKey] = 0.0
    sign = 1 if data[i][0] is True else -1
    bestTracker[xKey] += importance[i] * sign * data[i][1]
    bestTracker[yKey] += importance[i] * sign * data[i][2]
   
  bestKey = -1
  bestAxis = 'z'
  posIsPos = False
  for key in bestTracker.keys():
    if abs(bestTracker[key]) > bestKey:
      bestKey = abs(bestTracker[key])
      bestAxis = key[0]
      posIsPos = True if bestTracker[key] > 0 else False
  return(bestAxis, bestKey, posIsPos)
  
def isMisclassified(label, a, b, posIsPos):
  misclassified = False
  if a < b and not (label and posIsPos):
    misclassified = True
  elif a > b and not (label and posIsPos):
    misclassified = True
  return misclassified
  
def getStumpError(stump, data, importance):
  error = 0
  index = 1 if stump[0] == 'x' else 2
  for i, d in enumerate(data):
    if isMisclassified(d[0], d[index], stump[1], stump[2]):
      error += importance[i]
  return error/len(data)
  
def updateImportance(stump, data, importance, ada):
  newImportance = importance
  index = 1 if stump[0] == 'x' else 2
  for i, imp in enumerate(importance):
    sign = -1 if isMisclassified(data[0], data[i][index], stump[1], stump[2]) else 1
    newImportance[i] = 1/len(data) * imp * math.exp(-1 * ada * sign)
  return newImportance
  
def adaBoost(data, iterations):
  stumps = []
  importance = [1/len(data)]*len(data)
  for i in range(0, iterations):
    newStump = trainDecisionStump(data, importance)
    error = getStumpError(newStump, data, importance)
    adaptive = 0.5 * math.log((1-error)/error)
    stumps.append((adaptive, newStump))
    importance = updateImportance(newStump, data, importance, adaptive)
  return stumps
  
if __name__ == '__main__':
  trainData = []
  trainData.append((False, -1, 0))
  trainData.append((False, -1, -1))
  trainData.append((False, -1, -1))
  trainData.append((False, 0, 0))
  trainData.append((False, -1, 0))
  trainData.append((True, 0, 0))
  trainData.append((True, 5, 0))
  trainData.append((True, 1, 2))
  trainData.append((True, 6, 4))
  trainData.append((True, 0, 1))
  
  dataToLabel = (40, 40, 40)
  print (adaBoost(trainData, 10))