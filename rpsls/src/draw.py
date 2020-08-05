from src.sign import Sign


class Draw(Sign):
    def __init__(self, playerA, playerB):
        if playerA.sign != playerB.sign:
            raise ValueError("The players must have the same sign")
        self.playerA = playerA
        self.playerB = playerB

    def get_winner(self):
        if self.playerA.id < self.playerB.id:
            return self.playerA
        else:
            return self.playerB

    def get_loser(self):
        if self.playerA.id < self.playerB.id:
            return self.playerB
        else:
            return self.playerA
