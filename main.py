"""
    Implementation of HBMO for minimizing a mathematical function with 8 parameters.
"""

__author__ = 'Shiron'

import cProfile
import InitialSolutionsGenerator
from Solution import Solution
from Solution import FUNCTIA

def runHBMO():

    # Generate the initial set of solutions.
    solutions = InitialSolutionsGenerator.generateInitialSolutions()
    print(solutions)

    # Select the queen.
    queen = solutions[0]
    print(str(queen) + ".fitness = " + str(queen.getFitness()))

    bestSolution = Solution()
    while queen.storage >= 0:
        for (index, drone) in enumerate(solutions):
            if index == 0:  # this the queen actually
                continue

            if queen.probabilityToMateDrone(drone) > queen.probabilityToMateDroneThreshold:
                broods = queen.createBroods(drone)
                if len(broods) == 0:
                    continue

                bestBrood = broods[0]
                # Improve broods here # Check
                if bestBrood.getFitness() < bestSolution.getFitness():
                    bestSolution = bestBrood
                    print("Found better!")
                    print(str(bestSolution) + " =  " + str(FUNCTIA(bestSolution.c1, bestSolution.c2, bestSolution.c3, bestSolution.c4, bestSolution.c5, bestSolution.c6, bestSolution.c7, bestSolution.c8)) +
                          "\nfitness = " + str(bestSolution.getFitness()))

            else:
                pass

        queen = bestSolution  
        queen.nextIteration()

    print(str(bestSolution) + " =  " + str(FUNCTIA(bestSolution.c1, bestSolution.c2, bestSolution.c3, bestSolution.c4, bestSolution.c5, bestSolution.c6, bestSolution.c7, bestSolution.c8)) +
          "\nfitness = " + str(bestSolution.getFitness()))
    
cProfile.run('runHBMO()', sort='tottime')

