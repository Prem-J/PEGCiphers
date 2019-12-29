from Transformations import *
from bs4 import BeautifulSoup
import requests as req




def generateKey(length):
    resp = req.get(
        "https://www.fourmilab.ch/cgi-bin/Hotbits.api?nbytes=" + length + "&fmt=hex&npass=1&lpass=8&pwtype=3&apikey=&pseudo=pseudo")
    soup = BeautifulSoup(resp.text, "html.parser")
    key = soup.pre.string
    return key
