import math

def calcDerivative(number):
  return 2 * number

def calcGradient(point):
  return calcDerivative(point)

# Calculates gradient for maxThis = x-value from y = x^2
def gradientDescent(maxThis, K=10, learningRate=0.25):
  z = []
  z.append(maxThis)
  for k in range (0, K):
   gradient = calcGradient(z[k])
   z.append(z[k] - learningRate*gradient)
  return z[K-1]
  
if __name__ == '__main__':
  minimizeMe = (900)
  print (gradientDescent(minimizeMe))