from src.draw import Draw
from src.lizard import Lizard
from src.paper import Paper
from src.player import Player
from src.rock import Rock
from src.scissors import Scissors
from src.spock import Spock


class solution():
    opponents = []
    winner = None

    def __init__(self, readings):
        for line in readings.splitlines():
            self.opponents.append(Player(*line.split()))

    def tournament(self):
        if len(self.opponents) == 1:
            self.winner = self.opponents[0]
            return

        round = []
        for i in range(0, len(self.opponents), 2):
            round.append(
                self.fight(
                    self.opponents[i],
                    self.opponents[i + 1]
                )
            )
        self.opponents = round
        self.tournament()

    def getWinner(self):
        return self.winner

    def fight(self, playerA, playerB):
        if playerA.sign == "L":
            sign = Lizard(playerA, playerB)

        if playerA.sign == "P":
            sign = Paper(playerA, playerB)

        if playerA.sign == "R":
            sign = Rock(playerA, playerB)

        if playerA.sign == "C":
            sign = Scissors(playerA, playerB)

        if playerA.sign == "S":
            sign = Spock(playerA, playerB)

        if playerA.sign == playerB.sign:
            sign = Draw(playerA, playerB)

        roundWinner = sign.get_winner()
        roundWinner.addOpponent(sign.get_loser().id)

        return roundWinner
