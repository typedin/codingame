from src.solution import solution, toString


def test_impossible_scores():
    assert solution(1) == ["0 0 0"]
    assert solution(2) == ["0 0 0"]
    assert solution(4) == ["0 0 0"]


def test_one_ways():
    assert solution(3) == ["0 0 1"]
    assert solution(5) == ["1 0 0"]
    assert solution(6) == ["0 0 2"]
    assert solution(7) == ["1 1 0"]
    assert solution(8) == ["1 0 1"]
    assert solution(9) == ["0 0 3"]
    assert solution(11) == ["1 0 2"]


def test_two_ways():
    assert solution(12) == ["0 0 4", "2 1 0"]
    assert solution(13) == ["1 1 2", "2 0 1"]
    assert solution(14) == ["1 0 3", "2 2 0"]


def test_n_ways():
    """
        see: https://oeis.org/A261155
    """
    sequence = [11, 16, 19, 23, 26, 29, 32,
                34, 37, 39, 41, 44, 46, 47,
                49, 51, 53, 54, 56, 58, 59,
                61, 62, 64, 65, 67, 68, 69,
                71, 72, 74, 74, 76, 77, 79,
                79, 81, 82, 83, 84, 86, 86,
                88, 89, 89, 91, 92, 93, 94]

    for i in range(len(sequence)):
        if sequence[i] == sequence[i-1]:
            assert len(solution(sequence[i])) == i
            continue
        assert len(solution(sequence[i])) == i + 1


def test_to_string():
    assert toString(solution(12)) == "0 0 4\n2 1 0"
