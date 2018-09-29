import numpy as np
import pandas as pd
from scipy.optimize import fmin

file=pd.read_csv('your_time_series.csv')  #header=None
dat=pd.DataFrame(file) #to dataframe
dat=dat.dropna().pct_change() #get returns percentages
dat=dat.values #convert to np.array
dat=dat[1:] #remove header

def kelly(x):
    return np.prod(1+dat*x) #Kelly vector product of time series

max_x = fmin(lambda x: -kelly(x), 0, maxiter=25) #maxiter=25, ftol=0.01, xtol=.01 to solve for the maximum value (the Kelly bet)

print max_x[0] # returns the Kelly bet for imported time series
