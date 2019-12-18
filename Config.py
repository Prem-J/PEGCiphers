from Transformations import *
from bs4 import BeautifulSoup
import requests as req

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
    "10": "10",
    "11": "11",
    "12": "12",
    "13": "13",
    "14": "14",
    "15": "15",
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


def generateKey(length):
    resp = req.get(
        "https://www.fourmilab.ch/cgi-bin/Hotbits.api?nbytes=" + length + "&fmt=hex&npass=1&lpass=8&pwtype=3&apikey=&pseudo=pseudo")
    soup = BeautifulSoup(resp.text, "html.parser")
    key = soup.pre.string
    return key
