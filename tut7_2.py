#Tutorials 7_2
#Christopher Maxwell

#Today's date: 11 May 2015
import numpy
from matplotlib import pyplot as plt

n=300
rho=numpy.zeros(n)
rho[n/3:(2*n/3)]=1
v=1.0
dx=1.0
x=numpy.arange(n)*dx

plt.ion()
plt.clf()
plt.axis([0,n,0,1.5])
plt.plot(x,rho)
plt.draw()
plt.savefig('advection_picture.jpg')

dt=1.0
large_rho=numpy.zeros(n+1)
large_rho[1:]=rho
del rho
sample=10
dtt=dt/sample
for step in range(0,150):

    large_rho[0]=0
    for substep in range(0,sample):
        drho=large_rho[1:]-large_rho[0:-1]
        large_rho[1:]=large_rho[1:]-v*dtt/dx*drho

    plt.clf()
    plt.axis([0,n,0,1.1])
    plt.plot(x,large_rho[1:])
    plt.draw()
