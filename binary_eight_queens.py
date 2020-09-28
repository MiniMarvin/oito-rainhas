from random import random


class BinaryEightQueens:
    def __init__(self):
        self.genotype = [random.random() > 0.5 for _ in range(8*3)]

    def binToNum(self, lst):
        num = 0
        for n in lst:
            num *= 10
            if n:
                num += 1
        return num

    def buildFenotype(self):
        fenotype = [self.binToNum(self.genotype[i:i+3])
                    for i in range(0, len(self.genotype), 3)]

        return fenotype
    
