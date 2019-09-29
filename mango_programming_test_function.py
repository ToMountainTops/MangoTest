"""
Created on Sun Sep 28
For Mango Solutions Python test
For any questions please contact Claire Blejean: claire.blejean@gmail.com

The solution presented here relies on the random sampling function which is part of python.numpy.
A numerical solution can be coded which relies on mapping the inverse cumulative distribution function (cdf) of the chosen distibution onto a uniform sample.
The numerical solution can apply to any cdf which is invertible.
For common pdf, it can be found in python.stats, for unususal cdfs, the inverted function can be found with the pynverse package.

"""
#%%

from numpy import random

"""
he function below takes two arguments: the size of the sample and the distribution to be used
#The distribution is expected to take the following possible forms:
    - For normal: (0, mu, std), with mu the mean and std the standard deviation.
    - For poisson: (1, lambda), with lambda the average rate of success
    - For binomial: (2, n, p), with n the number of trials and p the probability of success (with p between 0 and 1).

"""

def random_sample(size, pdf):
    if pdf[0]==0:
        return random.normal(pdf[1], pdf[2], size)
    elif pdf[0]==1:
        return random.poisson(pdf[1], size)
    elif pdf[0]==2:
        return random.binomial(pdf[1], pdf[2], size)


#%%

"""

To test the results of the function, you can plot the sample distribution as follow:

"""        
        
import matplotlib.pyplot as plt

plt.hist(random_sample(300, (0, 0, 1)))


