# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:31:01 2021

@author: Shiron
"""

import random

queenGeneSet = [1, 2, 3, 4, 5, 6, 7, 8]
droneGeneSet = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
broodGeneSet = []
        
k = random.randint(0, 8)
print('Crossover Point:', k)
        
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
print(c1, c2, c3, c4, c5, c6, c7, c8)