#Tutorial 9

#Question 1: Write a least squares code

import numpy
from scipy.optimize import leastsq
from matplotlib import pyplot as plt

#data points
N = 100
t = numpy.linspace(0, 4*numpy.pi, N)
data = 3.0*numpy.sin(t+0.001) + 0.5 + numpy.random.randn(N)

guess_mean = numpy.mean(data)
guess_std = 3*numpy.std(data)/(2**0.5)
guess_phase = 0

data_first_guess = guess_std*numpy.sin(t+guess_phase) + guess_mean

# Define the function to optimize, in this case, we want to minimize the difference
# between the actual data and our "guessed" parameters
optimize_func = lambda x: x[0]*numpy.sin(t+x[1]) + x[2] - data
est_std, est_phase, est_mean = leastsq(optimize_func, [guess_std, guess_phase, guess_mean])[0]

# recreate the fitted curve using the optimized parameters
data_fit = est_std*numpy.sin(t+est_phase) + est_mean

plt.plot(data, '.')
plt.plot(data_fit, label='after fitting')
plt.plot(data_first_guess, label='first guess')
plt.legend()
plt.show()
