from src.player import Player
from src.signs import Draw, Lizard, Paper, Rock, Scissors, Spock


class solution():
    opponents = None

    def __init__(self, readings):
        if self.opponents is None:
            self.opponents = []
        for line in readings.splitlines():
            self.opponents.append(Player(*line.split()))

    def tournament(self):
        if len(self.opponents) == 1:
            return

        self.opponents = self.round()
        self.tournament()

    def round(self):
        aRound = []
        for i in range(0, len(self.opponents), 2):
            winner = self.fight(
                self.opponents[i],
                self.opponents[i+1]
            )
            aRound.append(winner)
        return aRound[:]

    def getWinner(self):
        return self.opponents[0]

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
