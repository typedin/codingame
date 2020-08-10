def toString(anArray):
    return "\n".join(anArray)


def solution(score):
    tryValue = 5
    convValue = 2
    kickValue = 3

    if score == 1 or score == 2 or score == 4:
        return ["0 0 0"]

    if score == 3:
        return ["0 0 1"]

    result = []

    def scoreIsValid(numTry, numConv, numKick):
        if numTry < numConv:
            return False
        return (
            (numTry * tryValue) +
            (numConv * convValue) +
            (numKick * kickValue) == score)

    for numTry in range(0, score//2):
        for numConv in range(0, score//2):
            for numKick in range(0, score//2):
                if scoreIsValid(numTry, numConv, numKick):
                    result.append("{} {} {}".format(numTry, numConv, numKick))

    return result
