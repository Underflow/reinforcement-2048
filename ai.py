import copy
import sys
import feature_reader
from population import Population

class AI:
    def __init__(self):
        self.score = 0
        self.count = 0
        self.population = Population(10)

    def restart_game(self):
        if self.score > 0:
            self.count += 1
            self.population.get_cur().score = self.score
            self.population.go_next()

    def get_allowed_moves(self, board):
        allowed = [False, False, False, False]

        for x in range(0, 4):
            for y in range(0, 4):
                if board[y][x] != None:
                    if y < 3 and board[y + 1][x] in (None, board[y][x]):
                        allowed[0] = True # DOWN
                    if y > 0 and board[y - 1][x] in (None, board[y][x]):
                        allowed[1] = True # UP
                    if x > 0 and board[y][x - 1] in (None, board[y][x]):
                        allowed[2] = True # LEFT
                    if x < 3 and board[y][x + 1] in (None, board[y][x]):
                        allowed[3] = True # RIGHT

        return allowed

    def get_move(self, score, board):
        self.score = score
        features = feature_reader.extract_features(board)
        g = self.population.get_cur()
        return g.decide(features, self.get_allowed_moves(board))
