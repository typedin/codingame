import string

def caesar(aString, startingNumber, decypher=False):

    def getIndex(i):
        indexInAlphabet = string.ascii_uppercase.find(aString[i])
        if decypher:
            return (indexInAlphabet - startingNumber - i) % 26
        return (indexInAlphabet + startingNumber + i) % 26

    result = ""
    for i in range(len(aString)):
        result += string.ascii_uppercase[getIndex(i)]

    return result


def decode(readings):
    result = readings[-1]

    for rotor in reversed(readings[2:5]):
        result = mapRotor(rotor, result)

    return caesar(result, int(readings[1]), True)

def encode(readings):
    result = caesar(readings[-1], int(readings[1]))

    for rotor in readings[2:5]:
        for j in range(len(result)):
            result = result[:j] + rotor[string.ascii_uppercase.find(result[j])] + result[j+1:]

    return result

def mapRotor(rotor, aString):
    mappedString = ""

    for letter in aString:
        mappedString += string.ascii_uppercase[rotor.find(letter)]

    return mappedString

def solution(readings):
    if readings[0] == "DECODE":
        return decode(readings)
    elif readings[0] == "ENCODE":
        return encode(readings)
    else:
        raise ValueError("Could not read readings")
