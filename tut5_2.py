#Create a dictionary
#Tutorial 5
#Christopher Maxwell
#Conmp phys

import numpy
import time

x={}
x[-1]='Starting'
x[1]=' ' 
x['system1'] = 'ignition and stablization'
x['system2'] = 'Engine on and lift off!'
x['system3'] = 'We have liftoff.'
x[2]= numpy.arange(0,5)

print type(x)
print x[-1] +x[1] + x['system1']
for i in range(6):
   t=-6
   x[t]= str(5-i)
   print 't- = ' + x[t] 
   time.sleep(1)

print x['system2']
time.sleep(2)
print x['system3']
