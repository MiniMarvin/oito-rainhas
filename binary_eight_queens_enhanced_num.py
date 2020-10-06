import random
import math
from collections import OrderedDict

class BinaryEightQueensEnhancedNum:
    def __init__(self, populationSize, crossOverMethod=1, selectMethod=1):
        '''
        inicializa a classe. 
        @params populationSize o tamanho da população. 
        '''
        self.populationSize = populationSize
        self.population = []
        self.crossOverMethod = self.crossOver
        if crossOverMethod == 2:
            self.crossOverMethod = self.crossOver2
        
        self.selectionMethod = self.selectParents
        if selectMethod == 2:
            self.selectionMethod = self.selectionMethod

        while len(self.population) < populationSize:
          gen = list(range(0,8))
          random.shuffle(gen)
          if gen not in self.population:
            self.population.append(gen)
        self.history = [self.population]

    def buildFenotype(self, gen):
        '''
        Constroi o fenotipo a partir do genoma (posição das rainhas).
        @params gen string o gene a ser calculado.
        '''

        return gen
    
    def mutate(self, gen):
        # swap
        # todo: verificar se vale trocar o fitness
        mutationProbability = 0.4
        if random.random() < mutationProbability:
            a = random.randrange(len(gen))
            b = random.randrange(len(gen))
            gen[a], gen[b] = gen[b], gen[a]
            
        output = gen

        return output

    def crossOver(self, gen1, gen2):
        pos = random.randrange(len(gen1))
        child1 = gen1[:pos] + gen2[pos:]
        child2 = gen2[:pos] + gen1[pos:]
        return child1, child2

    def crossOver2(self, gen1, gen2):
        pos = random.randrange(len(gen1))
        child1 = gen1[:pos] + gen2[pos:] + gen2[:pos]
        child2 = gen2[:pos] + gen1[pos:] + gen1[:pos]
        
        # remove repetitions
        child1 = list(OrderedDict.fromkeys(child1))
        child2 = list(OrderedDict.fromkeys(child2))

        return child1, child2
    
    def selectRoulette(self, population):
        fitnesses = [self.fitness(gen) for gen in population]
        total = sum(fitnesses)
        roulette = []
        for fit in fitnesses:
            roulette.append(fit/total)
        
        prob1 = random.random()
        prob2 = random.random()
        prev = 0
        parents = []
        for i in range(len(roulette)):
            if prev >= prob1 and prob1 <= roulette[i]:
                parents.append(population[i])
            if prev >= prob2 and prob2 <= roulette[i]:
                parents.append(population[i])
            prev = roulette[i]

        return parents

    def selectParents(self, population):
        gens = random.sample(population, 5)
        fenotypes = [(self.buildFenotype(gen), gen) for gen in gens]
        fitness = [(self.fitness(fen), gen) for fen, gen in fenotypes]
        fitness.sort(reverse=True)
        selectedGens = [gen for fitness, gen in fitness]
        return selectedGens[:2]
    
    def checkSolution(self, population):
        found = False
        ans = []
        for gen in population:
            if self.fitness(gen) == 28:
                found = True
                ans = gen
                break
        
        return found, ans
    
    def fitness(self, gen):
        maxHits = 8*(8-1)//2
        fenotypes = self.buildFenotype(gen)
        hits = 0
        for i in range(len(fenotypes)):
            for j in range(i):
                # print(fenotypes[i], fenotypes[j])
                if fenotypes[i] == fenotypes[j]:
                    hits += 1
                elif abs(fenotypes[i] - fenotypes[j]) == abs(i - j):
                    hits += 1
        
        return maxHits - hits

    def fit(self):
        for i in range(10000):
            found, gen = self.checkSolution(self.population)
            if found:
                print('alcançou a solução com ' + str(i) + ' iterações')
                # print(self.population)
                values = [(self.fitness(gen), self.buildFenotype(gen)) for gen in self.population if self.fitness(gen) == 28]
                print(values)
                break
            
            fitElements = [(self.fitness(gen), gen) for gen in self.population]
            fitElements.sort(reverse=True)

            if i%10 == 0:
                print(fitElements[0][0], self.buildFenotype(fitElements[0][1]))

            limit = math.floor(0.9*len(fitElements))
            newPopulation = []
            for i in range(limit, -1, -2):
                parents = self.selectionMethod(self.population)
                # aaa|bbbbbbb
                # bbb|aaaaaaa
                # print(parents)
                gens = self.crossOverMethod(parents[0], parents[1])
                m1, m2 = self.mutate(gens[0]), self.mutate(gens[1])
                newPopulation.append(m1)
                newPopulation.append(m2)
            
            population = [gen for fitness,gen in fitElements]
            population = population[:len(population) - limit] + newPopulation
            self.population = population
        
        # print('finalizou com:', [self.buildFenotype(gen) for gen in self.population])
            
            
