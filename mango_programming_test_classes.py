"""
Created on Sun Sep 28
For Mango Solutions Python test
For any questions please contact Claire Blejean: claire.blejean@gmail.com

The solution presented here relies on the random sampling function which is part of python.numpy.
A numerical solution can be coded which relies on mapping the inverse cumulative distribution function (cdf) of the chosen distibution onto a uniform sample.
For common pdf, it can be found in python.stats. For unususal cdfs, the inverted function can be found with the pynverse package (provided it is invertible).

"""
#%%

import numpy as np
import matplotlib.pyplot as plt

class Bound_exception(Exception):
    pass

class Distribution:

    def Normal(mean, standard_deviation, size):
        return np.random.normal(mean, standard_deviation, size)
        
    def Poisson(lamb, size): #with lamb the average rate of success
        return np.random.poisson(lamb, size)
    
    def Binomial(n, p, size): #with n the number of trials and p the probability of success (with p between 0 and 1)
        if p<0 or p>1:
            raise Bound_exception("p needs to be between 0 and 1.") #raise an error if p is out of bound
        else:
            return np.random.binomial(n, p, size)

    def Summarize(self):
        print("Minimum:", np.min(self))
        print("Maximum:", np.max(self))
        print("Mean:", np.mean(self))
        print("Standard deviation:", np.std(self))
        
    def Plot(self):
        plt.hist(self)


#%%
        
"""

To test the results of the method, you can plot the sample distribution as follow:

"""        

sample = Distribution.Normal(0, 1, 100)

Distribution.Summarize(sample)

Distribution.Plot(sample)

