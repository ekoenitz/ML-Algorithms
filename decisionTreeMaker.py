import math

def calcTotals(listOfDicts):
  totals = {}
  for dict in listOfDicts:
    index = dict["label"]
    if index in totals:
      totals[index] += 1
    else:
      totals[index] = 1
  return totals
  
def calcEntropy(samples):
  entropy = 0
  totals = calcTotals(samples)
  
  for total in totals.values():
    proportion = total/len(samples)
    entropy -= proportion * math.log(proportion, 2)
  return entropy


def calcBestFeature(samples, features):
  baseEntropy = calcEntropy(samples)
  bestInfoGain = -1
  bestFeature = features[0]
  
  for feature in features:
    featureEntropy = 0
    for possibleValue in getAllPossibleValues(samples, feature):
      relevantSamples = getSamplesWithFeatureValue(samples, feature, possibleValue)
      proportion = len(relevantSamples)/len(samples)
      featureEntropy += proportion * calcEntropy(relevantSamples)
    featureInfoGain = baseEntropy - featureEntropy
    if featureInfoGain > bestInfoGain:
      bestInfoGain = featureInfoGain
      bestFeature = feature
  return bestFeature
  
def getAllPossibleValues(samples, feature):
  possibleValues = []
  for sample in samples:
    if sample[feature] not in possibleValues:
      possibleValues.append(sample[feature])
  return possibleValues
  
def getSamplesWithFeatureValue(samples, feature, featureValue):
  desiredSamples = []
  for sample in samples:
    if sample[feature] == featureValue:
      desiredSamples.append(sample)
  return desiredSamples
  
def allSamplesHaveSameLabel(samples):
  allLabelsSame = True
  label = samples[0]["label"]
  for sample in samples:
    if sample["label"] != label:
      allLabelsSame = False
  return allLabelsSame

# Expected Input format:
# samples = List of dictionaries
# features = List of keys for samples' dictionaries; excluding label
def id3(samples, features):
  root = {}
  if allSamplesHaveSameLabel(samples) or len(features) < 1:
    return samples[0]["label"]
  bestFeature = calcBestFeature(samples, features)
  features.remove(bestFeature)
  root[bestFeature] = {}
  
  for possibleValue in getAllPossibleValues(samples, bestFeature):
    root[bestFeature][possibleValue] = id3(getSamplesWithFeatureValue(samples, bestFeature, possibleValue), features)
    
  return root
  
if __name__ == '__main__':
  s = []
  dict = {}
  dict["outlook"] = 'S'
  dict["temperature"] = 'H'
  dict["humidity"] = 'H'
  dict["wind"] = 'W'
  dict["label"] = 0
  s.append(dict)

  dict = {}
  dict["outlook"] = 'S'
  dict["temperature"] = 'H'
  dict["humidity"] = 'H'
  dict["wind"] = 'S'
  dict["label"] = 0
  s.append(dict)

  dict = {}
  dict["outlook"] = 'O'
  dict["temperature"] = 'H'
  dict["humidity"] = 'H'
  dict["wind"] = 'W'
  dict["label"] = 1
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'R'
  dict["temperature"] = 'M'
  dict["humidity"] = 'H'
  dict["wind"] = 'W'
  dict["label"] = 1
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'R'
  dict["temperature"] = 'C'
  dict["humidity"] = 'N'
  dict["wind"] = 'W'
  dict["label"] = 1
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'R'
  dict["temperature"] = 'C'
  dict["humidity"] = 'N'
  dict["wind"] = 'S'
  dict["label"] = 0
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'O'
  dict["temperature"] = 'C'
  dict["humidity"] = 'N'
  dict["wind"] = 'S'
  dict["label"] = 1
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'S'
  dict["temperature"] = 'M'
  dict["humidity"] = 'H'
  dict["wind"] = 'W'
  dict["label"] = 0
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'S'
  dict["temperature"] = 'C'
  dict["humidity"] = 'N'
  dict["wind"] = 'W'
  dict["label"] = 1
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'R'
  dict["temperature"] = 'M'
  dict["humidity"] = 'N'
  dict["wind"] = 'W'
  dict["label"] = 0
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'S'
  dict["temperature"] = 'M'
  dict["humidity"] = 'N'
  dict["wind"] = 'S'
  dict["label"] = 1
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'O'
  dict["temperature"] = 'M'
  dict["humidity"] = 'H'
  dict["wind"] = 'S'
  dict["label"] = 1
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'O'
  dict["temperature"] = 'H'
  dict["humidity"] = 'N'
  dict["wind"] = 'W'
  dict["label"] = 1
  s.append(dict)
  
  dict = {}
  dict["outlook"] = 'R'
  dict["temperature"] = 'M'
  dict["humidity"] = 'H'
  dict["wind"] = 'S'
  dict["label"] = 0
  s.append(dict)
  dt = id3(s, ["outlook", "temperature", "humidity", "wind"])
  print(dt)