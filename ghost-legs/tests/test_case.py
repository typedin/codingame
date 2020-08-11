from src.solution import solution
from tests.__fixtures__.readings import readings1, readings2, readings3


def test_A():
    assert solution(readings1) == "A2 B1 C3"


def test_B():
    assert solution(readings2) == "A3 B5 C1 D2 E4"


def test_C():
    assert solution(readings3) == "P3 Q7 R8 S5 T6 U2 V4 W1"

def test_D():
    assert solution(readings3) == "P3 Q7 R8 S5 T6 U2 V4 W1"
