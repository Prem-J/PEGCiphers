from Config import runTranslation


def encrypt(xCoords, yCoords, keys):
    xPoints = xCoords
    yPoints = yCoords
    numberOfPoints = len(xPoints)
    for i in range(0, len(keys)):
        key = keys[i]
        x = xPoints[i % numberOfPoints]
        y = yPoints[i % numberOfPoints]

        newCoords = runTranslation(key[0], key[1], (x, y))
        # print(newCoords)
        xPoints[i % numberOfPoints] = newCoords[0]
        yPoints[i % numberOfPoints] = newCoords[1]
    return xPoints, yPoints
