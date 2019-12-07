from Transformations import *

dictLetters = {
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


def runTranslation(transformation, amount, coords):
    if transformation == 0:
        return translateLeft(coords, amount)
    elif transformation == 1:
        return translateRight(coords, amount)
    elif transformation == 2:
        return translateDown(coords, amount)
    elif transformation == 3:
        return translateUp(coords, amount)
    elif transformation == 4:
        return scaleHorizontal(coords, amount)
    elif transformation == 5:
        return scaleVertical(coords, amount)
    elif transformation == 6:
        return scaleObliquePositive(coords, amount)
    elif transformation == 7:
        return scaleObliqueNegative(coords, amount)
    elif transformation == 8:
        return reflectX(coords)
    elif transformation == 9:
        return reflectY(coords)
    elif transformation == 10:
        return reflectObliquePositive(coords)
    elif transformation == 11:
        return reflectObliqueNegative(coords)
    elif transformation == 12:
        return rotateClockwise(coords, amount)
    elif transformation == 13:
        return rotateAnticlockwise(coords, amount)
    elif transformation == 14:
        return shiftObliquePositive(coords, amount)
    elif transformation == 15:
        return shiftObliqueNegative(coords, amount)


def runOppositeTranslation(transformation, amount, coords):
    if transformation == 0:
        return translateRight(coords, amount)
    elif transformation == 1:
        return translateLeft(coords, amount)
    elif transformation == 2:
        return translateUp(coords, amount)
    elif transformation == 3:
        return translateDown(coords, amount)
    elif transformation == 4:
        return scaleHorizontal(coords, (1 / amount))
    elif transformation == 5:
        return scaleVertical(coords, (1 / amount))
    elif transformation == 6:
        return scaleObliquePositive(coords, (-1 * (amount / (amount + 1))))
    elif transformation == 7:
        return scaleObliqueNegative(coords, (-1 * (amount / (amount + 1))))
    elif transformation == 8:
        return reflectX(coords)
    elif transformation == 9:
        return reflectY(coords)
    elif transformation == 10:
        return reflectObliquePositive(coords)
    elif transformation == 11:
        return reflectObliqueNegative(coords)
    elif transformation == 12:
        return rotateAnticlockwise(coords, amount)
    elif transformation == 13:
        return rotateClockwise(coords, amount)
    elif transformation == 14:
        return shiftObliquePositive(coords, -amount)
    elif transformation == 15:
        return shiftObliqueNegative(coords, -amount)

testKey = "92BE840EC671F28A554F1BBCC27D6FDBD2B8A9612FC7D2687DF6718CFEC04A2ED918A712F16A"
