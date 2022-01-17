"""
    Generate the initial solutions.
"""

__author__ = 'Shiron'

from sortedcontainers import SortedSet  # http://www.grantjenks.com/docs/sortedcontainers/sortedset.html
from Solution import Solution
import random

prices = {
    1: 2, 
    2: 5,
    3: 8,
    4: 11,
    5: 16,
    6: 23,
    7: 32,
    8: 50,
    9: 60,
    10: 90,
    11: 130,
    12: 170,
    13:300,
    14: 550,
    }


# MIN = -5
# MAX = 5
NR_INITAL_SOLUTIONS = 303


def generateInitialSolutions():
    """
        Generate Initial Solutions
    """
    solutions = SortedSet()
    for i in range(NR_INITAL_SOLUTIONS - 1):
        c1 = prices[random.randint(1, 14)]
        c2 = prices[random.randint(1, 14)]
        c3 = prices[random.randint(1, 14)]
        c4 = prices[random.randint(1, 14)]
        c5 = prices[random.randint(1, 14)]
        c6 = prices[random.randint(1, 14)]
        c7 = prices[random.randint(1, 14)]
        c8 = prices[random.randint(1, 14)]
        solutions.add(Solution(c1, c2, c3, c4, c5, c6, c7, c8))
    return solutions


def getSolutions():
    return generateInitialSolutions()

generateInitialSolutions()