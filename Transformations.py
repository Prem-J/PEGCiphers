import math


# 0
def translateLeft(initial, amount, opposite):
    if opposite:
        return translateRight(initial, amount, False)
    else:
        newX = initial[0] - amount
        return newX, initial[1]


# 1
def translateRight(initial, amount, opposite):
    if opposite:
        return translateLeft(initial, amount, False)
    else:
        newX = initial[0] + amount
        return newX, initial[1]


# 2
def translateDown(initial, amount, opposite):
    if opposite:
        return translateUp(initial, amount, False)
    else:
        newy = initial[1] - amount
        return initial[0], newy


# 3
def translateUp(initial, amount, opposite):
    if opposite:
        return translateDown(initial, amount, False)
    else:
        newy = initial[1] + amount
        return initial[0], newy


# 4
def scaleHorizontal(initial, amount, opposite):
    if opposite:
        newx = initial[0] * (1 / (amount + 1))
        return newx, initial[1]
    else:
        newx = initial[0] * (amount + 1)
        return newx, initial[1]


# 5
def scaleVertical(initial, amount, opposite):
    if opposite:
        newy = initial[1] * (1 / (amount + 1))
        return initial[0], newy
    else:
        newy = initial[1] * (amount + 1)
        return initial[0], newy


# 6
def scaleObliquePositive(initial, amount, opposite):
    scaleFactor = amount
    if opposite:
        scaleFactor = (-1 * (amount / (amount + 1)))
    # 1 - 16 instead of 0 - 15
    x = initial[0]
    y = initial[1]
    distancePerToLine = abs(x - y) / 2
    newX = newY = 0
    if x > y:
        newX = x + (scaleFactor * distancePerToLine)
        newY = y - (scaleFactor * distancePerToLine)
    else:
        newX = x - (scaleFactor * distancePerToLine)
        newY = y + (scaleFactor * distancePerToLine)

    return (newX, newY)


# 7
def scaleObliqueNegative(initial, amount, opposite):
    scaleFactor = amount
    if opposite:
        scaleFactor = (-1 * (amount / (amount + 1)))
    x = initial[0]
    y = initial[1]
    distancePerToLine = abs(x + y) / 2
    newX = newY = 0
    if x > (-1 * y):
        newX = x + (scaleFactor * distancePerToLine)
        newY = y + (scaleFactor * distancePerToLine)
    else:
        newX = x - (scaleFactor * distancePerToLine)
        newY = y - (scaleFactor * distancePerToLine)
    return newX, newY


# 8
def reflectX(initial, amount, opposite):
    newy = initial[1] * -1
    return initial[0], newy


# 9
def reflectY(initial, amount, opposite):
    newx = initial[0] * -1
    return newx, initial[1]


# A
def reflectObliquePositive(initial, amount, opposite):
    newX = initial[1]
    newY = initial[0]
    return newX, newY


# B
def reflectObliqueNegative(initial, amount, opposite):
    newX = -1 * initial[1]
    newY = -1 * initial[0]
    return newX, newY


# C
def rotateClockwise(initial, amount, opposite):
    if opposite:
        return rotateAnticlockwise(initial, amount, False)
    else:
        return rotate(initial, -amount)


# D
def rotateAnticlockwise(initial, amount, opposite):
    if opposite:
        return rotateClockwise(initial, amount, False)
    else:
        return rotate(initial, amount)


def rotate(initial, amount):
    angle = (math.pi / 15) * amount
    newX = (initial[0] * math.cos(angle)) - (initial[1] * math.sin(angle))
    newY = (initial[1] * math.cos(angle)) + (initial[0] * math.sin(angle))
    return newX, newY


# E
def shiftObliquePositive(initial, amount, opposite):
    amt = amount
    if opposite:
        amt = -amount
    newx = initial[0] + amt
    newy = initial[1] + amt
    return newx, newy


# F
def shiftObliqueNegative(initial, amount, opposite):
    amt = amount
    if opposite:
        amt = -amount
    newx = initial[0] - amt
    newy = initial[1] - amt
    return newx, newy


transformationList = [translateLeft, translateRight, translateDown, translateUp, scaleHorizontal, scaleVertical,
                      scaleObliquePositive, scaleObliqueNegative, reflectX, reflectY, reflectObliquePositive,
                      reflectObliqueNegative, rotateClockwise, rotateAnticlockwise, shiftObliquePositive,
                      shiftObliqueNegative]

def runTranslation(transformation, amount, coords):
    return transformationList[transformation](coords, amount, False)


def runOppositeTranslation(transformation, amount, coords):
    return transformationList[transformation](coords, amount, True)
