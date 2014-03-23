from genome import Genome
import random

class Population:
    def __init__(self, size):
        self.size = size
        self.cur = 0
        self.individuals = []
        for _ in range(self.size):
            g = Genome(30)
            g.randomize()
            self.individuals.append(g)

    def go_next(self):
        print('fitness(' + str(self.cur) + ') = ' +
                str(self.individuals[self.cur].score))
        self.cur += 1
        print("Firness evaluation ind: " + str(self.cur))
        if self.cur >= self.size:
            # This is a new generation
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
        # FIXME: Sort in invert order
        self.individuals = sorted(self.individuals,
                key = lambda ind: ind.score,
                reverse = True)

        for _ in range(self.size):
            p1 = self.select()
            p2 = self.select()
            g = Genome(30)
            g.crossover(p1, p2)
            new.append(g)

        self.individuals = new


    def mutate(self):
        print("Processing mutation")

    def get_cur(self):
        return self.individuals[self.cur]
