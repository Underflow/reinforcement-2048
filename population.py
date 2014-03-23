from genome import Genome
import random

class Population:
    def __init__(self, size):
        self.size = size
        self.cur = 0
        self.individuals = []
        for _ in range(self.size):
            g = Genome(10)
            g.randomize()
            self.individuals.append(g)

    def go_next(self):
        self.cur += 1
        if self.cur >= self.size:
            aver = sum(ind.score for ind in self.individuals) / len(self.individuals)
            print(aver)
            self.cur = 0
            self.crossover()
            self.mutate()

    def select(self):
        for i in range(self.size):
            if random.randint(0, 2) == 0:
                return self.individuals[i]
        return self.individuals[0]

    def crossover(self):
        new = []
        self.individuals = sorted(self.individuals,
                key = lambda ind: ind.score,
                reverse = True)

        for _ in range(self.size):
            p1 = self.select()
            p2 = self.select()
            g = Genome(10)
            g.crossover(p1, p2)
            new.append(g)

        self.individuals = new

    def mutate(self):
        for individual in self.individuals:
            individual.mutate()

    def get_cur(self):
        return self.individuals[self.cur]
