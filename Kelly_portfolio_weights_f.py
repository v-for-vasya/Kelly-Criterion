import numpy as np
from scipy.optimize import minimize
import math


def objective(x, sign=-1.0):
    w1=x[0]
    w2=x[1]
    w3=x[2]
    a=np.array([0.3,-.15])
    b=np.array([-0.05,0.2])
    c=np.array([0.05,0.1])
    fx=math.log(np.prod(1+w1*a+w2*b+w3*c))
    return sign*(fx)

def weight_sum(x):
    return x[0]+x[1]+x[2]-1.0

b=(-1,1)
bounds=(b,b,b)

cons={'type': 'eq', 'fun': weight_sum}

x_default=np.zeros(3)
sol = minimize(objective, x_default,method='SLSQP', bounds=bounds, constraints=[cons])

print sol
print 'Kelly portfolio weights are as follows ' + str(sol.x*100)

a=np.array([0.3,-.15])
b=np.array([-0.05,0.2])
c=np.array([0.05,0.1])
w1=sol.x[0]
w2=sol.x[1]
w3=sol.x[2]

print w1+w2+w3
print math.log(np.prod(1+w1*a+w2*b+w3*c))