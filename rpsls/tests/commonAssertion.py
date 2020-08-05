class CommonAssertion():
    def instanciatedClass(self):
        return self.sut(self.playerA, self.playerB)

    def assert_playerA_wins(self):
        return ((self.instanciatedClass().get_winner().id == self.playerA.id)
                and (self.instanciatedClass().get_loser().id == self.playerB.id))

    def assert_playerB_wins(self):
        return ((self.instanciatedClass().get_winner().id == self.playerB.id)
                and (self.instanciatedClass().get_loser().id == self.playerA.id))
