readings = '''7 7
A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3'''


def getLines(readings):
    return readings.splitlines()[1:]


def mustGoLeft(line, currentIndex):
    if currentIndex == 0:
        return False
    if line[currentIndex-1:currentIndex+1] == "|-":
        return True
    return line[currentIndex - 1] == "-"


def mustGoRight(line, currentIndex):
    # if currentIndex + 1 == " ":
        # return False
    if currentIndex + 1 == len(line):
        return False
    if line[currentIndex:currentIndex + 2] == "-|":
        return True
    return line[currentIndex + 1] == "-"


def goRight(line, currentIndex):
    result = currentIndex
    while mustGoRight(line, result):
        result += 1
    return result


def goLeft(line, currentIndex):
    result = currentIndex
    while mustGoLeft(line, result):
        result -= 1
    return result


def getLegs(firstLine):
    result = []
    for i in range(len(firstLine)):
        if firstLine[i] != " ":
            result.append({
                "char": firstLine[i],
                "index": i,
            })
    return result


def formatOutput(line, leg):
    return "{}{}".format(leg["char"], line[leg["index"]])


def solution(readings):
    result = []
    for leg in getLegs(getLines(readings)[0]):
        for line in getLines(readings):
            if mustGoLeft(line, leg["index"]):
                leg["index"] = goLeft(line, leg["index"])
                continue
            if mustGoRight(line, leg["index"]):
                leg["index"] = goRight(line, leg["index"])
                continue
        result.append(formatOutput(line, leg))

    return " ".join(result)
