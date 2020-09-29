import random
import math

class BinaryEightQueens:
    def __init__(self, populationSize):
        '''
        inicializa a classe. 
        @params populationSize o tamanho da população. 
        '''
        self.populationSize = populationSize
        self.population = [[random.random() > 0.5 for _ in range(8*3)] for _ in range(populationSize)]
        self.history = [self.population]

    def binToNum(self, lst):
        num = 0
        for n in lst:
            num << 1
            if n:
                num += 1
        return num

    def buildFenotype(self, gen):
        '''
        Constroi o fenotipo a partir do genoma (posição das rainhas).
        @params gen string o gene a ser calculado.
        '''
        fenotype = [self.binToNum(gen[i:i+3])
                    for i in range(0, len(gen), 3)]

        return fenotype
    
    def mutate(self, gen):
      mutationProbability = 0.4
      output = gen
      for i in range(0,len(gen)-1):
        if random.random() < mutationProbability:
          #mutate
          output[i] = bool(random.getrandbits(1))
      return output
    
    def crossOver(self, gen1, gen2):
        pos = random.randrange(len(gen1))
        child1 = gen1[:pos] + gen2[pos:]
        child2 = gen2[:pos] + gen1[pos:]
        return child1, child2
    
    
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
                values = [(self.fitness(gen), self.buildFenotype(gen)) for gen in self.population if self.fitness(gen) == 0]
                print(values)
                break
            
            fitElements = [(self.fitness(gen), gen) for gen in self.population]
            fitElements.sort(reverse=True)

            if i%100:
                print(fitElements[0][0])

            limit = math.floor(0.9*len(fitElements))
            newPopulation = []
            for i in range(limit, -1, -2):
                parents = self.selectParents(self.population)
                # aaa|bbbbbbb
                # bbb|aaaaaaa
                # print(parents)
                gens = self.crossOver(parents[0], parents[1])
                m1, m2 = self.mutate(gens[0]), self.mutate(gens[1])
                newPopulation.append(m1)
                newPopulation.append(m2)
            
            population = [gen for fitness,gen in fitElements]
            population = population[:len(population) - limit] + newPopulation
            self.population = population
        
        # print('finalizou com:', [self.buildFenotype(gen) for gen in self.population])
            
            
