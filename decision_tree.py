import random

class DecisionTest:
    def __init__(self, features_limits):
        self.feature = random.randint(0, len(features_limits) - 1)
        feat_min = features_limits[self.feature][0]
        feat_max = features_limits[self.feature][1]
        self.cmp_with = random.randint(feat_min, feat_max)
        self.test = random.randint(0, 1)

    def __call__(self, X):
        if self.test == 1:
            return X[self.feature] >= self.cmp_with
        else:
            return X[self.feature] <= self.cmp_with


class DecisionTree:
    def __init__(self, height, features_limits):
        if height == 0:
            self.value = random.randint(0, 3)
            self.left = None
            self.right = None
            self.test = None
            self.height = height
        else:
            self.left = DecisionTree(height - 1, features_limits)
            self.right = DecisionTree(height - 1, features_limits)
            self.value = None
            self.test = DecisionTest(features_limits)
            self.height = height

    def decide(self, X):
        if self.test != None:
            if self.test(X):
                return self.left.decide(X)
            else:
                return self.right.decide(X)
        else:
            return self.value
