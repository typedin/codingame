from src.spock import Spock
from src.scissors import Scissors


class solution():
    def __init__(self, readings):
        pass

    def fight(self, playerA, playerB):
        if playerA.sign == "C":
            sign = Scissors(playerA, playerB)

        if playerA.sign == "S":
            sign = Spock(playerA, playerB)

        winner = sign.get_winner()
        winner.addOpponent(sign.get_loser().id)

        return winner


"""
Scissors > Paper
Scissors > Lizard
Rock > Scissors

Spock > Scissors
Spock > Rock
Paper > Spock
Lizard > Spock


Rock > Lizard
Lizard > Paper
"""
