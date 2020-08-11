from src.solution import solution

readings1 = '''7 7
A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3'''

readings2 = '''13 8
A  B  C  D  E
|  |  |  |  |
|  |--|  |  |
|--|  |  |  |
|  |  |--|  |
|  |--|  |--|
|  |  |  |  |
1  2  3  4  5
'''


def test_A():
    assert solution(readings1) == "A2 B1 C3"


def test_B():
    assert solution(readings2) == "A3 B5 C1 D2 E4"
