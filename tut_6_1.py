#Christopher Maxwell
#Tutorial 6_1-2 Particles
#May 2015


import numpy
from matplotlib import pyplot as plt
#Start with 2 particles
x0=0;y0=0;wx0=0;wy0=0.5
x1=1;y1=0;wx1=0;wy1=-0.5;

#Trivial case, assume Gravity, g, and mass, m, are equal to 1
dt=0.1
sample_size=4000
dtsample_size=dt/sample_size
tmax=5
nstep=numpy.ceil(tmax/dt)
potential=numpy.zeros(nstep)
kinetic=numpy.zeros(nstep)
rvalue=numpy.zeros(nstep)

plt.ion()
step=0
for t in numpy.arange(0,tmax,dt):
    for ii in range(0,sample_size):
        dx=x0-x1
        dy=y0-y1
        rsquare=dx*dx+dy*dy
        r=numpy.sqrt(rsquare)
        r3=r*r*r
#Force components of x and y
        fx0=dx/r3;
        fy0=dy/r3
#forces on particles must be opposite
        fx1=-fx0
        fy1=-fy0
#Positions of particles must be updated
        x0 +=dtsample_size*wx0
        y0 +=dtsample_size*wy0
        wx0 +=-dtsample_size*fy0
        wy0 +=-dtsample_size*fy0
        
        x1+=dtsample_size*wx1
        y1+=dtsample_size*wy1
        wy1 -=dtsample_size*fx1
        wy1 -=dtsample_size*fy1
    
#plot graphs
    plt.clf()
    plt.plot(x0,y0,'radius_x')
    plt.plot(x1,y1,'b*')
    plt.ylim(-1.6,-1.6)
    plt.xlim(-1.5,2)

    plt.draw()
#Finally, represent data:
    pot=-1.0/r
    kin=0.5*(wx0*wx0+wy0*wy0+wx1*wx1+wy1*wy1)
    new_potential[step]=pot
    new_kinetic[step]=kin
    rvalue[step]=r
    step+=1

    print 'Kinetic Energy:' + repr(kin) + '.' + 'Potential Energy:' + repr(pot) + '.' + 'Total Energy:' +repr(kin+pot) + ',' + 'R-squared:' + repr(rsquare)
