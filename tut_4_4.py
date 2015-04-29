#Tutorial 4 part 4

import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft

#Function
def convolution(x,y):
   assert(x.size==y.size)
#Gen zeroes
   x2=numpy.zeros(2*x.size)
   x2[0:x.size]=x
   y2=numpy.zeros(2*y.size)
   y2[0:y.size]=y
#Fourier Tranforms
   x2fft=fft(x2)
   y2fft=fft(y2)
   vector=numpy.real(ifft(x2fft*y2fft))
   return vector[0:x.size]



if __name__=='__main__':
#Range
   x = numpy.arange(-30,30,0.1)
#Sigma
   s=2
#Guassian function
   y=numpy.exp(-0.5*x*2/s**2)
   y=y/y.sum()
#Plot functions
   convolution_y=convolution(y,y)
   plt.plot(x,convolution_y)
   plt.plot(x,y)
   plt.plot()
#Show plot on Graph
   plt.show()
