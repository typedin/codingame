class Player():
    def __init__(self, anId, aSign):
        self.id = int(anId)
        self.sign = aSign
        self.opponents = []

    def addOpponent(self, opponent_id):
        self.opponents.append(opponent_id)

    def idToString(self):
        return str(self.id)

    def opponentsToString(self):
        return [str(opponent) for opponent in self.opponents]
