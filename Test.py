from Transformations import *
import numpy as np
import math

initial = [0, 5.657]

print(rotateAnticlockwise(initial, 5))


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
