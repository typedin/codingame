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
    if currentIndex + 1 == " ":
        return False
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


def solution(readings):
    lines = getLines(readings)

    result = []
    for leg in getLegs(lines[0]):
        for i in lines:
            if mustGoLeft(i, leg["index"]):
                leg["index"] = goLeft(i, leg["index"])
                continue
            if mustGoRight(i, leg["index"]):
                leg["index"] = goRight(i, leg["index"])
                continue
        result.append("{}{}".format(
                    leg["char"],
                    i[leg["index"]]
                )
            )

    return " ".join(result)


solution(readings)
