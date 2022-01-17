"""
Honey-Bee Mate Optimization Algorithm
"""
__author__ = 'Shiron'

from sortedcontainers import SortedSet  # http://www.grantjenks.com/docs/sortedcontainers/sortedset.html
import math
import random

def FUNCTIA(c1, c2, c3, c4, c5, c6, c7, c8):
    L = 1000

    
    return L * (c1 + c2 + c3 + c4 + c5+ c6 + c7 + c8)


class Solution:
    """
    The bee.
    """
    def __init__(self, c1=None, c2=None, c3=None, c4=None, c5=None, c6=None, c7=None, c8=None):
        self.c1 = c1 or 0
        self.c2 = c2 or 0
        self.c3 = c3 or 0
        self.c4 = c4 or 0
        self.c5 = c5 or 0
        self.c6 = c6 or 0
        self.c7 = c7 or 0
        self.c8 = c8 or 0

        self.speedReductionFactor = 0.95 
        self.storageReductionAmount = 1     

        self.speed = 0.6
        self.storage = 20  

        self.probabilityToMateDroneThreshold = 0.10     # Check

    def __lt__(self, other):
        if isinstance(other, Solution):
            return self.getFitness() < other.getFitness()
        else:
            raise Exception("Class Soultion compared with other class.")

    def getFitness(self):
        """
        :return:
            The fitness function of this solution.
    
        """
         
        return 1 / FUNCTIA(self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8)

    def probabilityToMateDrone(self, drone):
        """
        Computes to probability that this solution (the queen, hopefully) will pick
        the drone in the mating dance.
        :param drone:
        :return: a float in interval [0, 1] representing the probability.
        """
        if isinstance(drone, Solution):
            return math.exp(-abs(self.getFitness() - drone.getFitness()) / self.speed)
        else:
            raise Exception("Drone not of type Solution")

    def nextIteration(self):
        """
        Supposing this is the queen, the following parameters have to updated at each iteration:
            speed,
            energy
        :return:
        """
        self.speed *= self.speedReductionFactor
        self.storage -= self.storageReductionAmount

    # def numberOfBroodsWithDrone(self, drone): # Check
    #     """
    #     Computes the number of broods this queen makes with the drone based on:
    #         The queen's energy
    #         The drone's fitness value
    #         A random float number in interval [0, 1]
    #     :param drone:
    #     :return: An non-negative integer
    #     """
    #     return int(self.storage * drone.getFitness() * random.uniform(0, 1))

    def createBroods(self, drone):
        """
        Provides a set of solutions derived from this queen. Runs the genotypes combination
        algorithm for each new brood.
        :param drone:
        :return: A sorted set of solutions.
        """
        if not isinstance(drone, Solution):
            raise Exception("Drone not of type Solution")

        # nr_broods = self.numberOfBroodsWithDrone(drone)
        nr_broods = self.storage
        broods = SortedSet()

        for i in range(nr_broods-1):
            brood = self.combineGenotypes(drone)
            broods.add(brood)

        return broods

    def combineGenotypes(self, drone):
        """
        Runs Single-point cross over.
        :param drone:
        :return: A new solution (brood).
        """
        queenGeneSet = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8]
        droneGeneSet = [drone.c1, drone.c2, drone.c3, drone.c4, drone.c5, drone.c6, drone.c7, drone.c8]
        broodGeneSet = []
        
        k = random.randint(0, 8)
        
        if k == 0:
            broodGeneSet = droneGeneSet
        elif k == 8:
            broodGeneSet = queenGeneSet
        else:
            for m in range(0, k):
                broodGeneSet.insert(m, queenGeneSet[m])
            for n in range(k, 8):
                broodGeneSet.insert(n, droneGeneSet[n])
        
        
        
        [c1, c2, c3, c4, c5, c6, c7, c8] = broodGeneSet
        return Solution(c1, c2, c3, c4, c5, c6, c7, c8)

    def __str__(self):
        return "(" + str(self.c1) + ", " + str(self.c2) + ", " + str(self.c3) + ", " + str(self.c4) + ", " + str(self.c5) + ", " + str(self.c6) + ", " + str(self.c7) + ", " + str(self.c8) + ")"

