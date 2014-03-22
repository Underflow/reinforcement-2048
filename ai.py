import copy
import sys
from decision_tree import DecisionTree
import feature_reader

class AI:
    def __init__(self):
        self.score = 0
        self.count = 0
        sys.stdout.write("[")

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

        (features, features_limits) = feature_reader.extract_features(board)

        dt = DecisionTree(3, features_limits)
        return dt.decide(features)
