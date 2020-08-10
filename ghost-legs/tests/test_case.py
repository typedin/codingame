from src.solution import solution
from tests.__fixtures__.readings import readings1, readings2, readings3, readings4, readings5

def myFormat(anArray):
    return "\n".join(anArray)

def test_A():
    assert myFormat(solution(readings1)) == "A2\nB1\nC3"


def test_B():
    assert myFormat(solution(readings2)) == "A3\nB5\nC1\nD2\nE4"


def test_C():
    assert myFormat(solution(readings3)) == "P3\nQ7\nR8\nS5\nT6\nU2\nV4\nW1"


def test_D():
    assert myFormat(solution(readings4)) == "A1\nB3\nC0\nD5\nE2\nF7\nG4\nH9\nI6\nJ8"


def test_E():
    expectation = "A1\nB3\nC0\nD5\nE2\nF7\nG4\nH9\nI6\nJ8"
    assert myFormat(solution(readings4)) == expectation
