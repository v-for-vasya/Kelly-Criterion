import numpy as np
import pandas as pd
from scipy.optimize import fmin

import timeit

start = timeit.default_timer()
"""
file=pd.read_csv('kelly_data.csv',header=None)
dat=pd.DataFrame(file) #to dataframe
dat=dat.values #convert to np.array
"""


file=pd.read_csv('vix_just_returns.csv')  #header=None
dat=pd.DataFrame(file) #to dataframe
dat=dat.dropna().pct_change() #get returns percentages
dat=dat.values #convert to np.array
dat=dat[1:] #remove header

def kelly(x):
    return np.prod(1+dat*x)

max_x = fmin(lambda x: -kelly(x), 0, maxiter=25) #maxiter=25, ftol=0.01, xtol=.01

print max_x[0]



stop = timeit.default_timer()
print('Simulation time: ', stop - start)