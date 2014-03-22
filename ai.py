import copy
import sys
import feature_reader
from genome import Genome

class AI:
    def __init__(self):
        self.score = 0
        self.count = 0
        sys.stdout.write("[")
        self.genome = Genome(30)

    def __del__(self):
        sys.stdout.write("]\n")

    def restart_game(self):
        if self.score > 0:
            if self.count > 0:
                sys.stdout.write(", ")
            sys.stdout.write(str(self.score))
            self.count += 1

    def get_move(self, score, board):
        self.score = score
        features = feature_reader.extract_features(board)
        return self.genome.decide(features)
