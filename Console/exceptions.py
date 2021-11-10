class BattleEnd(Exception):
    def __init__(self, winner):
        self.winner = winner
