import feature_reader
import random
from decision_tree import DecisionTree


class Genome:
    def __init__(self, size):
        self.genes = []
        self.size = size
        self.score = 0

    def randomize(self):
        limits = feature_reader.get_features_limits()
        for i in range(0, self.size):
            self.genes.append(DecisionTree(3, limits))

    def crossover(self, p1, p2):
        for _ in range(self.size):
            if random.randint(0, 1) == 0:
                self.genes.append(p1.genes[random.randint(0, self.size - 1)])
            else:
                self.genes.append(p2.genes[random.randint(0, self.size - 1)])

    def decide(self, X, allowed):
        choices = [0, 0, 0, 0]
        for i in range(0, self.size):
            choices[self.genes[i].decide(X)] += 1
        for i in range(0, 4):
            if not allowed[i]:
                choices[i] = -1
        return choices.index(max(choices))
