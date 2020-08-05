class Sign:

    def __init__(self, playerA, playerB):
        if playerA.sign != self.identifier():
            raise ValueError
        self.playerA = playerA
        self.playerB = playerB

    def get_winner(self):
        if self.can_win():
            return self.playerA
        if self.cannot_win():
            return self.playerB

    def get_loser(self):
        if self.can_win():
            return self.playerB
        if self.cannot_win():
            return self.playerA

    def can_win(self):
        return self.playerB.sign in self.stronger_than()

    def cannot_win(self):
        return self.playerB.sign in self.weaker_than()

    def identifier():
        raise NotImplementedError("This method must be implemented")

    def stronger_than():
        raise NotImplementedError("This method must be implemented")

    def weaker_than():
        raise NotImplementedError("This method must be implemented")
