import feature_reader
from decision_tree import DecisionTree


class Genome:
    def __init__(self, size):
        self.genes = []
        self.size = size
        limits = feature_reader.get_features_limits()
        for i in range(0, size):
            self.genes.append(DecisionTree(3, limits))

    def decide(self, X, allowed):
        choices = [0, 0, 0, 0]
        for i in range(0, self.size):
            choices[self.genes[i].decide(X)] += 1
        for i in range(0, 4):
            if not allowed[i]:
                choices[i] = -1
        return choices.index(max(choices))
