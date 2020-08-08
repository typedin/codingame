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


class Lizard(Sign):

    def identifier(self):
        return "L"

    def stronger_than(self):
        return ["P", "S"]

    def weaker_than(self):
        return ["R", "C"]


class Paper(Sign):

    def identifier(self):
        return "P"

    def stronger_than(self):
        return ["R", "S"]

    def weaker_than(self):
        return ["C", "L"]


class Rock(Sign):

    def identifier(self):
        return "R"

    def stronger_than(self):
        return ["L", "C"]

    def weaker_than(self):
        return ["P", "S"]


class Scissors(Sign):

    def identifier(self):
        return "C"

    def stronger_than(self):
        return ["P", "L"]

    def weaker_than(self):
        return ["R", "S"]


class Spock(Sign):

    def identifier(self):
        return "S"

    def stronger_than(self):
        return ["C", "R"]

    def weaker_than(self):
        return ["P", "L"]
