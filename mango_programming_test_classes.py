"""
Created on Sun Sep 28
For Mango Solutions Python test
For any questions please contact Claire Blejean: claire.blejean@gmail.com

The solution presented here relies on the random sampling function which is part of python.numpy.
A numerical solution can be coded which relies on mapping the inverse cumulative distribution function (cdf) of the chosen distibution onto a uniform sample.
For common pdf, it can be found in python.stats. For unususal cdfs, the inverted function can be found with the pynverse package (provided it is invertible).

"""
#%%

from numpy import random

class Bound_exception(Exception):
    pass

class Random_distribution:

    def Normal(mean, standard_deviation, size):
        return random.normal(mean, standard_deviation, size)
        
    def Poisson(lamb, size): #with lamb the average rate of success
        return random.poisson(lamb, size)
    
    def Binomial(n, p, size): #with n the number of trials and p the probability of success (with p between 0 and 1)
        if p<0 or p>1:
            raise Bound_exception("p needs to be between 0 and 1.") #raised an error is p is out of bound
        else:
            return random.binomial(n, p, size)


#%%

"""

To test the results of the function, you can plot the sample distribution as follow:

"""        
        
import matplotlib.pyplot as plt

plt.hist(Random_distribution.Normal(0, 1, 300))

plt.hist(Random_distribution.Binomial(10, 2, 300))

