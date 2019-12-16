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
        return scaleHorizontal(coords, (amount + 1))
    elif transformation == 5:
        return scaleVertical(coords, (amount + 1))
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
        return scaleHorizontal(coords, (1 / (amount + 1)))
    elif transformation == 5:
        return scaleVertical(coords, (1 / (amount + 1)))
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


testKey = "E2998AFC5498F2ED71AE64FB5511B6E8C5C67998C33A1EBC36293359B9F94AC5958F35E39CEEFFDE198D0277FE5373CD43109F423322F9E15C881A9014CDD5EF60EAA351817A8FCA86798B2F6647663DAF21A22228025C1563C734A6CAAF68E28A4951B8D24919C13D960FA8DB8B2EC1886FD513CED08010A32538D49638ED3E1F7BE6B371D362005814D6C9E5265EC3D5EBBD89F62C67DF506D1CC814158333E98E910F6A04DE3C0C67A72D80EB4790DB6B4380A6283FB13DC1DE28E00DF79098CE52DB038483DC9F8AFD78CD2D6BE7FDCC1CA33722C6875062984FCF69188F1008DC2C6C091454A0F0DD3B843AC4CE5489518C0A34EB5A107E882CF3AD3D9E9D0020C0C56521AAE0B9B3A5E7825D6C9BA7A266656D8855523EB051A8749FA83739E10DBFA214B3C613F3CB2AD2B982DFECD4DD27C5ED9F1AB3465965C73BFEF3A9C400F577BCC71C19D7DE164B65140BD770BCC4F13CDFCE9FA0FE25E7B979AA08FEC3B34BDC1135A7D328BDFA55916E44AAF4810C878673AA9F82D75189C35215112AEA2318423E33AD5BB0736AC1D251BA138912EE9F70F258BC4672AF7FED74D007F2117988D17DC4830EF4389DDECF17FF73BCAC98E86CA35CFFB8BA098D4AD2CC355855C991DA4B295C069DB3DFF16CC51210B2B193992576155CE023DED329032FD4B7CA275CF77BE603ADFA3B1324EBA1CE53BFDC9F3A84B2F6363D3887AE2A69BF4D49C94B0B24AE0EB3B33DE0C33D77ECA1EF59536EB679785E37A387DF72814DE80178018BBF19C79614C0A637750A3A52D5DC6E71DBF5F31EF9"
