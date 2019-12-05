from Config import dictLetters


def determineTransformation(entry):
    s = [entry[i:i + 1] for i in range(0, len(entry), 1)]
    transformed = [dictLetters[i] for i in s]
    return transformed


def getTransformedKeys(key):
    splitKey = [key[i:i + 2].lower() for i in range(0, len(key), 2)]
    keys = [determineTransformation(i) for i in splitKey]
    return keys
