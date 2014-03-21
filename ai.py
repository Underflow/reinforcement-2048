import copy
from decision_tree import DecisionTree
import feature_reader

class AI:
    def __init__(self):
        self.score = 0

    def restart_game(self):
        print(self.score)

    def get_move(self, score, board):
        self.score = score

        features = feature_reader.extract_features(board)

        dt = DecisionTree()
        return dt.decide(features)
