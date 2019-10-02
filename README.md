# MangoTest
Submission for Mango Solution coding test.

## Author

Claire Blejean
claire.blejean@gmail.com

## Data analysis

>Read in the csv containing NBA free throws. Visualise some aspect of the data you find interesting, e.g., the average number of free throws per period for the regular season and the playoffs.

Submission: 
` mango_test_app.py`

The data analysed for this exercise is presented in the format of a dashboard. It relies on the installation of the dash package.
The dashboard is here in a development format and hosted locally. It can be seen by visiting http://127.0.0.1:8050/.
If operating windows, please enable 'Internet Information Services' from 'Turn Windows features on or off', to access localhost.
In the context of a client project such a dashboard could be deployed on a server for wide-spread access.

## Programming

#### Functions

> Write a function that will draw random numbers from a given distribution. The function should take one argument for the number of samples and a second argument which specifies the distribution (Normal, Poisson or Binomial). The function should be able to handle additional parameters depending on the distribution chosen, e.g., mean and sd for Normal samples.

Submission: 
` mango_programming_test_function.py`

The solution presented here relies on the random sampling function which is part of python.numpy.
A numerical solution can be coded which relies on mapping the inverse cumulative distribution function (cdf) of the chosen distibution onto a uniform sample.
The numerical solution can apply to any cdf which is invertible.
For common cdf, it can be found in python.stats, for unususal cdfs, the inverted function can be found with the pynverse package.

### Object-oriented programming

> Construct an alternative to the above solution by using one or more classes instead of a single function.
Instances of this distribution class should store the distribution parameters as attributes, and also contain a draw method, which draws a fresh set of random numbers according to the distributions parameters, and a summarise method, which prints the min, max, mean, and standard deviation of the newly drawn sample.

Submission: 
` mango_programming_test_classes.py`

As for the above, the solution presented here relies on the random sampling function which is part of python.numpy.

### Package Building

> Build a package containing the functions and classes above. Use any tools as necessary.
Include instructions on how the package can be installed.

The package has been uploaded to the Python Packaging Index PyP and as such can easily be installed with:
` pip install mango_programming_test`

Otherwise, the package is also submitted here in:
`mango_programming_test_pkg`
