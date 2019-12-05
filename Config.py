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

testKey = "92BE840EC671F28A554F1BBCC27D6FDBD2B8A9612FC7D2687DF6718CFEC04A2ED918A712F16A90FFB5C8019E934C965A4B758B5D6C56F0284B277C0B7AE189B8616F127BA98CF34C2B0D33A70F655509E18D5DC0935F78681D79D927ADBF476BB504E8CAEA1DFE53E442D94FB460B35AF59DBA293A9E923BB70ABB67CA3E95954B05E4D14A64354468FF99160D4A54D158E4ED4D8285AE3DE059B339C91E435AB36CC7B44F661EE41106D7849E52EE31DC0F2D8A793FBB5D92875D672ED9E75A9D02899F6153B778E3D19C6E94CEA41EAD2DC0ED67FECB92BAB558BCEE0D0A16A031CCE462FBD427C2BD623DA7555FD1CADBFFBE0C0F44800404952F6A15C4DE"


def runTranslation(transformation, amount, coords):
    if transformation == 0:
        translateLeft(coords, amount)
    elif transformation == 1:
        translateRight(coords, amount)
    elif transformation == 2:
        translateDown(coords, amount)
    elif transformation == 3:
        translateUp(coords, amount)
    elif transformation == 4:
        scaleHorizontal(coords, amount)
    elif transformation == 5:
        scaleVertical(coords, amount)
    elif transformation == 6:
        scaleObliquePositive(coords, amount)
    elif transformation == 7:
        scaleObliqueNegative(coords, amount)
    elif transformation == 8:
        reflectX(coords)
    elif transformation == 9:
        reflectY(coords)
    elif transformation == 10:
        reflectObliquePositive(coords)
    elif transformation == 11:
        reflectObliqueNegative(coords)
    elif transformation == 12:
        rotateClockwise(coords, amount)
    elif transformation == 13:
        rotateAnticlockwise(coords, amount)
    elif transformation == 14:
        shiftObliquePositive(coords, amount)
    elif transformation == 15:
        shiftObliqueNegative(coords, amount)
