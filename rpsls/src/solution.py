from src.draw import Draw
from src.spock import Spock
from src.lizard import Lizard
from src.paper import Paper
from src.rock import Rock
from src.scissors import Scissors
from src.player import Player


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

        new_opponents = []
        for i in range(len(self.opponents)):
            if i % 2 == 0:
                new_opponents.append(
                    self.fight(self.opponents[i], self.opponents[i + 1])
                )
        self.opponents = new_opponents
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
