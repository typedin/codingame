ALPHA = "ABCDEFGHEJKLMNOPQRSTUVWXYZ"

def caesarShift(aString, startingNumber):

    def getIndex(letter, startingNumber):
        return (ALPHA.find(letter) + startingNumber) % 26

    result = ""
    for letter in aString:
        result = result + ALPHA[(getIndex(letter, startingNumber))]
        startingNumber += 1
    return result


def solution(readings):
    rotors = [
        "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    ]

    aString = "AAA"
    result = caesarShift(aString, 4)

    for i in range(len(rotors)):
        for letter in result[-len(aString):]:
            found = ALPHA.find(letter)
            result += rotors[i][found]

    return result[-len(aString):]
