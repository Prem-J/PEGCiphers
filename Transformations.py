import math


# 0
def translateLeft(initial, amount):
    newX = initial[0] - amount
    return (newX, initial[1])


# 1
def translateRight(initial, amount):
    newX = initial[0] + amount
    return (newX, initial[1])


# 2
def translateDown(initial, amount):
    newy = initial[1] - amount
    return (initial[0], newy)


# 3
def translateUp(initial, amount):
    newy = initial[1] + amount
    return (initial[0], newy)


# 4
def scaleHorizontal(initial, amount):
    newx = initial[0] * amount
    return (newx, initial[1])


# 5
def scaleVertical(initial, amount):
    newy = initial[1] * amount
    return (initial[0], newy)


# 6
def scaleObliquePositive(initial, amount):
    # 1 - 16 instead of 0 - 15
    x = initial[0]
    y = initial[1]
    distancePerToLine = abs(x - y) / 2
    newX = newY = 0
    if x > y:
        newX = x + ((amount) * distancePerToLine)
        newY = y - ((amount) * distancePerToLine)
    else:
        newX = x - ((amount) * distancePerToLine)
        newY = y + ((amount) * distancePerToLine)

    return (newX, newY)


# 7
def scaleObliqueNegative(initial, amount):
    x = initial[0]
    y = initial[1]
    distancePerToLine = abs(x + y) / 2
    newX = newY = 0
    if x > (-1 * y):
        newX = x + ((amount) * distancePerToLine)
        newY = y + ((amount) * distancePerToLine)
    else:
        newX = x - ((amount) * distancePerToLine)
        newY = y - ((amount) * distancePerToLine)
    return (newX, newY)


# 8
def reflectX(initial):
    newy = initial[1] * -1
    return (initial[0], newy)


# 9
def reflectY(initial):
    newx = initial[0] * -1
    return (newx, initial[1])


# A
def reflectObliquePositive(initial):
    newX = initial[1]
    newY = initial[0]
    return (newX, newY)


# B
def reflectObliqueNegative(initial):
    newX = -1 * initial[1]
    newY = -1 * initial[0]
    return (newX, newY)


# C
def rotateClockwise(initial, amount):
    angle = (180 / 15) * (amount)
    radius = math.sqrt((initial[0] ** 2) + (initial[1] ** 2))
    theta = math.atan(initial[1] / initial[0])
    newX = radius * math.cos(theta + angle)
    newY = radius * math.sin(theta + angle)
    return (newX, newY)


# D
def rotateAnticlockwise(initial, amount):
    angle = (180 / 15) * (dictLetters[amount])
    radius = math.sqrt((initial[0] ** 2) + (initial[1] ** 2))
    theta = math.atan(initial[1] / initial[0])
    newX = radius * math.cos(theta - angle)
    newY = radius * math.sin(theta - angle)
    return (newX, newY)


# E
def shiftObliquePositive(initial, amount):
    newx = initial[0] + amount
    newy = initial[1] + amount
    return (newx, newy)


# F
def shiftObliqueNegative(initial, amount):
    newx = initial[0] - amount
    newy = initial[1] - amount
    return (newx, newy)
