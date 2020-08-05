class Player():
    def __init__(self, anId, aSign):
        self.id = anId
        self.sign = aSign
        self.opponents = []

    def addOpponent(self, opponent_id):
        self.opponents.append(opponent_id)

    def get_opponents(self):
        return self.opponents
