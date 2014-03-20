import copy
from decisiontree import DecisionTree
import boardfeatures

class AI:
    def __init__(self):
        self.score = 0

    def restart_game(self):
        print("Score: " + str(self.score))

    def get_move(self, score, board):
        self.score = score
        features = []

        # Extracts a set of feature of the board using descriptive statistics
        # Dim(set) = 13


        # Vertical/horizontal density extraction
        # Dim = 8
        (xdensity, ydensity) = boardfeatures.get_histograms(board)
        for density in xdensity:
            features.append(density)
        for density in ydensity:
            features.append(density)

        # Number of close mergeable tiles for each direction
        # Dim = 4
        for direction in range(0, 4):
            features.append(boardfeatures.mergeable_tiles(board, direction))

        # Variance of the board
        # Dim = 1
        features.append(boardfeatures.get_variance(board))

        # Build the learning model, decision tree ?
        dt = DecisionTree()
        return dt.decide(features)
