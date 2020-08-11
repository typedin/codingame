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


def getIdentifier(firstLine):
    result = []
    for i in range(len(firstLine)):
        if firstLine[i] != " ":
            result.append({
                "char": firstLine[i],
                "index": i,
                "in": i,
                "stop": None
            })
    return result


def solution(readings):
    lines = getLines(readings)

    result = []
    for identifier in getIdentifier(lines[0]):
        identifier["stop"] = identifier["in"]
        for i in range(len(lines)):
            if mustGoLeft(lines[i], identifier["stop"]):
                identifier["stop"] = goLeft(lines[i], identifier["stop"])
                continue
            if mustGoRight(lines[i], identifier["stop"]):
                identifier["stop"] = goRight(lines[i], identifier["stop"])
                continue
        result.append("{}{}".format(
                    identifier["char"],
                    lines[i][identifier["stop"]]
                )
            )

    return " ".join(result)


solution(readings)
