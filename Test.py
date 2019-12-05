from Config import *
from TextToKey import getTransformedKeys, determineTransformation
from TextToCoords import convertTextIntoCoords

print(getTransformedKeys(testKey))

testDataToEncrypt = "This is a message that must be secured"
for i in convertTextIntoCoords(testDataToEncrypt):
    print(i)
