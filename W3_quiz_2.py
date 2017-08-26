# Week3 Quiz 2 Solutions

#refer to page 65 of slide presented in week3 of the course

# ds/dt = -10*s(t)
# s = exp(-10*t)

# explicit euler scheme formula
# s(j+1) = s(j)(1 - 10*delta_t)

#implicit euler scheme formula
# s(j+1) = s(j)/(1 + 10*delta_t)
import numpy as np

def euler_integration(delta_t,n,method):
    s = [1.]
    if method == 'explicit':
        for i in range(1,n+1):
            res = s[i-1]*(1 - 10*delta_t)
            s.append(res)
        return s[n]
    elif method == 'implicit':
        for i in range(1,n+1):
            res = s[i-1]/(1 + 10*delta_t)
            s.append(res)
        return s[n]
    
#ques_1
#print(euler_integration(0.05,4,'explicit'))
       
#ques_2     
#print(euler_integration(0.05,4,'implicit'))     
        
#ques_3     
#print(euler_integration(0.1,4,'explicit'))
        
#ques_4    
#print(euler_integration(0.1,4,'implicit'))
        
#ques_5     
#print(euler_integration(0.2,4,'explicit'))

#ques_6     
#print(euler_integration(0.2,4,'implicit'))

#ques_7
#print(euler_integration(0.25,4,'explicit'))

#ques_8
#print(euler_integration(0.25,4,'implicit'))           
