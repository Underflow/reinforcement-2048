import random
import copy

class AI:
    def __init__(self):
        self.score = 0

    def restart_game(self):
        print("Score: " + str(self.score))

    def get_move(self, score, board):
        self.score = score
        return random.randint(0, 3)
