# Mango Programming Test Package

README file created by Claire Blejean on Sun Sep 29 2019, for Mango Solutions.
For any further queries, you can contact me at: claire.blejean@gmail.com

### Context

This package has been developped for Mango Solutions Programming Test. 
It encompasses some classes and methods around the random sampling of three types of common distributions:
* Normal
* Poisson
* Binomial

From the Test instructions:

>**Functions**
>Write a function that will draw random numbers from a given distribution. The function should take one argument for the number of samples and a second argument which specifies the distribution (Normal, Poisson or Binomial). The function should be able to handle additional parameters depending on the distribution chosen, e.g., mean and sd for Normal samples.
>
>**Object-oriented programming**
>Construct an alternative to the above solution by using one or more classes instead of a single function.
>Instances of this distribution class should store the distribution parameters as attributes, and also contain a draw method, which draws a fresh set of random numbers according to the distributions parameters, and a summarise method, which prints the min, max, mean, and standard deviation of the newly drawn sample.
>
>**Package Building**
>Build a package containing the functions and classes above. Use any tools as necessary.
>Include instructions on how the package can be installed.

## Getting Started

### Compatibility

This package has been developed for python 3.0 and above. It relies on the numpy library.

### Instructions 

This package has been developped to be used with any python distribution and IDE. It has been uploaded to PyPI, the Python Packaging Index repository and can be installed with the pip command.

` pip install mango_programming_test`

This package can also be downloaded from its git repository:
https://github.com/ToMountainTops/mango_programming_test

## How to use

This package defines the distribution class and associated methods.

#### Normal
` Normal(mean, standard_deviation, size) `
Returns an array of *size*-elements, randomly drawn from a normal distribution definied by *mean* and *standard_deviation*.

#### Poisson
` Poisson(lamb, size) `
Returns an array of *size*-elements, randomly drawn from a poisson distribution definied by *lamb*, the average rate of success.

#### Binomial
` Binomial(n, p, size) `
Returns an array of *size*-elements, randomly drawn from a binomial distribution definied by *n*, the number of trials and *p*, the probability of success. 
If *p* is not between 0 and 1, an exception is raised.

### Summarize
` Summarize(A) `
For any array A, including the arrays defined above, prints the maximum, minimum, mean and standard deviation.

### Plot
` Plot(A) `
For any array A, including the arrays defined above, graphs a histogram of the distribution.

## Author
Claire Blejean
claire.blejean@gmail.com