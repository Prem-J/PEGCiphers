import numpy as np
import matplotlib.pyplot as plt
from Config import dictLetters

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
