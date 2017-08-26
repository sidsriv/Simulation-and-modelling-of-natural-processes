import numpy as np
import math
import random
import matplotlib.pyplot as plt

maxPerPile = 10
numberOfPiles = 10
maxIter = 100
x = 0

piles_left = []

piles = np.empty(numberOfPiles)
piles.fill(10)
#print(piles)
totPiles = np.sum(piles)
#print(totPiles)
numPiles = np.array([piles.size])
while(True):
    if (piles.size > 1 and totPiles == np.sum(piles)):
        piles = piles[np.nonzero(piles)]
        if(piles.size == 1):
        	break
        #piles_left.append(piles.size)
        for i in np.arange(piles.size):
            piles[i] -= 1
            num = np.random.randint(piles.size)
            piles[num] += 1
        numPiles = np.append(numPiles,piles.size)
        x += 1

print(x)
#plt.plot(range(maxIter),piles_left)
#plt.title('Piles left vs No. of Iterations')
#plt.show()


