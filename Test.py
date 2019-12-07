from Transformations import *

initial = (7, 4)

# newCoords = scaleObliqueNegative(initial, 1)
# print(newCoords)
#
#
# newNewCoords = scaleObliqueNegative(newCoords, -0.5)
# print(newNewCoords)


amount = 7
newCoords = rotateClockwise(initial, amount)
print(newCoords)

newNewCoords = rotateAnticlockwise(newCoords, amount)
print(newNewCoords)

# newCoords = scaleObliqueNegative(initial, 2)
# print(newCoords)
#
#
# newNewCoords = scaleObliqueNegative(newCoords, -0.6666666666)
# print(newNewCoords)

# TODO: -Rotation doesnt work in reverse mode
