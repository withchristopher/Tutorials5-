# Advection problem
#Tutorial , lecture 7
#Christopher Maxwell
#11 May 2015

import numpy
import time
from matplotlib import pyplot as plt

#Setup parameters
#sample number
n = 500
rho=numpy.zeros(n)
rho[n/3:(2*n/3)]=1
#3 significant figures
v=-1.00
dx=1.00
x=numpy.arange(n)*dx

#Plotting
plt.ion()
plt.clf()
plt.axis([0,n,0,1.1])
plt.plot(x,rho)
plt.draw()
#New command to save the file
plt.savefig('tut7_1.png')

dt=1.00
#I have used a t=time.time() to mark a timed iteration, I am unsure whether this #is the correct way to do this. Is there a different call function.
#The model grows with time.
t= time.time()
#loop
for i in range(0,50):
    drho=rho[1:]-rho[0:-1]
    rho[1:]=rho[1:]-v*dt/dx*drho
    #plot
    plt.clf()
    plt.axis([0,n,0,t])
    plt.plot(x,rho)
    plt.draw()

