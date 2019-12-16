import copy
from random import randint

from Config import *
from TextToKey import getTransformedKeys, determineTransformation
from TextToCoords import convertTextIntoCoords
from Encrypt import *
import matplotlib.pyplot as plt

# for i in range(0, 16):
#     for k in range(0, 16):
#         x = randint(0, 100)
#         y = randint(0, 100)
#         newCoords = runTranslation(i, k, (x, y))
#         convertBack = runOppositeTranslation(i, k, newCoords)
#         OrigCoords = (round(convertBack[0]), round(convertBack[1]))
#
#         if (OrigCoords != (x, y)):
#             print(i, k)
#             print(x, y)
#             print(newCoords)
#             print(convertBack)
#             print()



print(getTransformedKeys(testKey))

testDataToEncrypt = "This is a message that must be secured"
originalCoords = convertTextIntoCoords(testDataToEncrypt)
print(originalCoords[0])
print(originalCoords[1])

newCoords = encrypt(copy.deepcopy(originalCoords[0]), copy.deepcopy(originalCoords[1]), getTransformedKeys(testKey))
# print(newCoords[0])
# print(newCoords[1])

backToOriginalCoords = decrypt(copy.deepcopy(newCoords[0]), copy.deepcopy(newCoords[1]), getTransformedKeys(testKey))
x = backToOriginalCoords[0]
y = backToOriginalCoords[1]

for i in range(0, len(backToOriginalCoords[1])):
    x[i] = round(x[i])
    y[i] = round(y[i])

print(x)
print(y)

# plt.figure(1)
# plt.scatter(originalCoords[0], originalCoords[1])
#
# plt.figure(2)
# plt.scatter(newCoords[0], newCoords[1])
#
# plt.show()

# TODO: Fix transformation number 4 which does not map back to correct values
