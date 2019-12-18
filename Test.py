# from Transformations import *
import numpy as np
import math
# from Config import *
import TextToCoords

initial = [0, 4]

# print(scaleHorizontal(initial, 0))
#
# for i in range(30, 0, -1):
#     print(i)

# newCoords = runTranslation(3, 5, initial)
# print(newCoords)
# backToOriginal = runOppositeTranslation(3, 5, newCoords)
# print(backToOriginal)
print(hex(ord('n')))
test = "1C1581EAAF61CD08D4AB9E52CB57FF03581227FD353A8D48F5215D3D98324E0D\n378999C38951310A4F2E7BD56E37B83A2EF2CCE29F30491E99598FB3ACA6B90F"
print(test)

print(test.replace("\n", ""))

print(hex(ord('a')))
print(chr(int('61', 16)))

test = TextToCoords.convertTextIntoCoords("this is a test string")
print(test)
print(TextToCoords.convertCoordsIntoText(test[0], test[1]))


# for i in range(16):
#     newCoords = runTranslation(i, 5, initial)
#     # print(newCoords)
#     backToOriginal = runOppositeTranslation(i, 5, newCoords)
#     print(backToOriginal)

# def rotate(angle, initial):
#     trans = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
#     initial = np.array([initial[0], initial[1]])
#     return initial.dot(trans)
#
# print(rotate(2.64, [4, -4]))
# print(rotate(-2.64, [-1.583981101622533, 5.430562021531719]))


# print(rotateClockwise(initial, 0))

def rotate(angle, initial):
    newX = (initial[0] * math.cos(angle)) - (initial[1] * math.sin(angle))
    newY = (initial[1] * math.cos(angle)) + (initial[0] * math.sin(angle))

# newCoords = scaleObliqueNegative(initial, 1)
# print(newCoords)
#
#
# newNewCoords = scaleObliqueNegative(newCoords, -0.5)
# # print(newNewCoords)
#
#
# amount = 7
# newCoords = rotateClockwise(initial, amount)
# print(newCoords)
#
# newNewCoords = rotateAnticlockwise(newCoords, amount)
# print(newNewCoords)

# newCoords = scaleObliqueNegative(initial, 2)
# print(newCoords)
#
#
# newNewCoords = scaleObliqueNegative(newCoords, -0.6666666666)
# print(newNewCoords)

# TODO: - Rotation doesnt work in reverse mode
