import copy
from Config import *
from TextToKey import getTransformedKeys, determineTransformation
from TextToCoords import convertTextIntoCoords
from Encrypt import *
import matplotlib.pyplot as plt

print(getTransformedKeys(testKey))

testDataToEncrypt = "This is a message that must be secured"
originalCoords = convertTextIntoCoords(testDataToEncrypt)
print(originalCoords[0])
print(originalCoords[1])

newCoords = encrypt(copy.deepcopy(originalCoords[0]), copy.deepcopy(originalCoords[1]), getTransformedKeys(testKey))
print(newCoords[0])
print(newCoords[1])

plt.figure(1)
plt.scatter(originalCoords[0], originalCoords[1])

plt.figure(2)
plt.scatter(newCoords[0], newCoords[1])

plt.show()
