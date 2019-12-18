import copy
import Config
import TextToCoords
import Encrypt
import TextToKey


def doThings(text, layers):
    unecryptedCoords = TextToCoords.convertTextIntoCoords(text)
    numberOfBytes = len(unecryptedCoords[0]) * layers

    key = Config.generateKey(str(numberOfBytes))
    key = key.replace("\n", "")
    funcKey = TextToKey.getTransformedKeys(key)

    encrypted = Encrypt.encrypt(copy.deepcopy(unecryptedCoords[0]), copy.deepcopy(unecryptedCoords[1]), funcKey)

    decryptedData = Encrypt.decrypt(copy.deepcopy(encrypted[0]), copy.deepcopy(encrypted[1]), funcKey)
    x = [round(list(decryptedData[0])[i]) for i in range(0, len(decryptedData[0]))]
    y = [round(list(decryptedData[1])[i]) for i in range(0, len(decryptedData[1]))]
    decrypted = [x, y]

    decryptedText = TextToCoords.convertCoordsIntoText(decrypted[0], decrypted[1])

    dict = {
        "origX": unecryptedCoords[0],
        "origY": unecryptedCoords[1],
        "hexKey": key,
        "encrypX": encrypted[0],
        "encrypY": encrypted[1],
        "decrypX": decrypted[0],
        "decrypY": decrypted[1],
        "decrypText": decryptedText
    }

    return dict


layers = int(input("how many layers of security would you like?"))
unencryptedData = input("What would you like to encrypt?")
stuff = doThings(unencryptedData, layers)
# Just to see all output
print(stuff["origX"])
print(stuff["origY"])
print(stuff["hexKey"])
print(stuff["encrypX"])
print(stuff["encrypY"])
print(stuff["decrypX"])
print(stuff["decrypY"])
print(stuff["decrypText"])
