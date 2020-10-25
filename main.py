from binary_eight_queens import BinaryEightQueens
from binary_eight_queens_enhanced_num import BinaryEightQueensEnhancedNum
import statistics

def statisticsCommonBoard():
    finishCount = 0
    generationsList = []
    finalPopulationFitness = []
    numberOfConvergents = []
    for i in range(30):
        # board = BinaryEightQueensEnhancedNum(100,2,1,1, True)
        board = BinaryEightQueens(100, True)
        didFinish, countGenerations, populationFitness, convergentNumber = board.fit()

        if didFinish:
            finishCount += 1
            generationsList.append(countGenerations)
            finalPopulationFitness += populationFitness
            numberOfConvergents.append(convergentNumber)
    
    print('numero de convergencias', finishCount)
    print('media de iterações', statistics.mean(generationsList))
    print('desvio padrão de iterações', statistics.stdev(generationsList))
    print('fitness medio', statistics.mean(finalPopulationFitness))
    print('desvio padrão fitness', statistics.stdev(finalPopulationFitness))
    print('media individuos convergentes', statistics.mean(numberOfConvergents))
    print('desvio padrão individuos convergentes', statistics.stdev(numberOfConvergents))

# board = BinaryEightQueens(100)
# data = board.fit()
# print(data)

# board = BinaryEightQueensEnhancedNum(100,2,1)
# board.fit()
statisticsCommonBoard()