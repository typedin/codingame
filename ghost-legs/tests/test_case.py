from src.solution import solution
from src.solution import mustGoRight
from src.solution import mustGoLeft
from src.solution import goRight
from src.solution import goLeft
from src.solution import getLegs

readings1 = '''7 7
A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3'''


def test_must_go_right():
    line = "|--|  |"
    assert mustGoRight(line, 0) is True
    assert mustGoRight(line, 1) is True
    assert mustGoRight(line, 2) is True
    assert mustGoRight(line, 6) is False


def test_must_go_left():
    line = "|--|  |"
    assert mustGoLeft(line, 3) is True
    assert mustGoLeft(line, 2) is True
    assert mustGoLeft(line, 1) is True
    assert mustGoLeft(line, 0) is False
    assert mustGoLeft(line, 6) is False


def test_go_right_as_long_as_you_can():
    line = "|--|  |"
    currentIndex = 0
    assert goRight(line, currentIndex) == 3
    assert goRight(line, 3) == 3
    assert goRight(line, 6) == 6


def test_go_left_as_long_as_you_can():
    line = "|--|  |"
    currentIndex = 3
    assert goLeft(line, currentIndex) == 0
    assert goLeft(line, 0) == 0
    assert goLeft(line, 6) == 6


def test_reads_starting_identifier():
    firstLine = "A  B  C"
    assert getLegs(firstLine) == [
        {
            "char": "A",
            "index": 0,
        },
        {
            "char": "B",
            "index": 3,
        },
        {
            "char": "C",
            "index": 6,
        },
    ]


def test_A():
    assert solution(readings1) == "A2 B1 C3"
