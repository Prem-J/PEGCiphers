import numpy as np
import matplotlib.pyplot as plt
from Config import dictLetters, letterstohex

'''
Converts text into a coordinates based on their unicode digit.
'''


def convertTextIntoCoords(text):
    hexArray = []
    for i in text:
        # print(hex(ord(i)))
        hexArray.append(hex(ord(i))[2:])

    xCoor = []
    yCoor = []

    for i in hexArray:
        xCoor.append(dictLetters[i[0]])
        yCoor.append(dictLetters[i[1]])

    return xCoor, yCoor


def convertCoordsIntoText(xCoords, yCoords):
    codesArray = [letterstohex[str(xCoords[i])] + letterstohex[str(yCoords[i])] for i in range(len(xCoords))]
    finalString = [chr(int(codesArray[i], 16)) for i in range(len(codesArray))]
    return ''.join(finalString)
