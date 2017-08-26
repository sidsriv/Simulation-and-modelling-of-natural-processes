

import numpy as np
import math

class Integrator:
    def __init__(self, xMin, xMax, N):
        ################################
        self.xMin = xMin
        self.xMax = xMax
        self.N = N
    
            
    def integrate(self):       
        ##################################
        delta_x = (self.xMax - self.xMin)/(self.N-1)
        nums = np.arange(self.N-1)
        nums = nums*delta_x + self.xMin
        res = np.power(nums,2)*np.sin(nums)*np.exp(-1*nums)
        res = np.sum(res)*delta_x
        self.res = res
        
        
    def show(self):
        ##################################
        print(self.res)
        

examp = Integrator(1,3,200)
examp.integrate()
examp.show()