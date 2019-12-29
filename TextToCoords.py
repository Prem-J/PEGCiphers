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

letterstohex = {
    "10": "a",
    "11": "b",
    "12": "c",
    "13": "d",
    "14": "e",
    "15": "f",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

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
