""" Honey-Bee Mating Optimization Algorith
"""

__author__ = 'Shiron'

import math
from random import randint

# Initialization 

# Define basic parameters 
nQueens = 3;
nDrones = 200;
nWorkers = 100;
maxMatingFlights = 100;
spermStoreSize = 20;
initSpeed = 0.6;
speedReductionFactor = 0.95;

# Define the unit cost list with a unique ID
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

def objFunction(c1, c2, c3, c4, c5, c6, c7, c8):
    L = 1000
    return (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8)*L
        
def getFitness(self):
    return math.exp(-(objFunction(self.c1, self.c2)**2)/100)


queens = [];
workers = [];
drones = [];


print(prices[1])
# Initialize Queens, Drones and Workers gene values    

for i in range(nQueens):
    queens.append(objFunction(prices[randint(1, 14)], prices[randint(1, 14)], prices[randint(1, 14)], prices[randint(1, 14)], prices[randint(1, 14)], prices[randint(1, 14)], prices[randint(1, 14)], prices[randint(1, 14)]))
   
 
print(queens)
