#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:18:14 2024

@author: karasu
"""

########## 12 Steps to Navıer-Stokes - Step 2: nonlinear convection ##########

# Instead of c=const un[i] is given as the multiplier 

## Pre-defined initial conditions 


import numpy
from matplotlib import pyplot as plt

# Instead of a constant factor c multiplying the second term, now we have the solution u
# multiplying it. Thus, the second term of the equation is now nonlinear.
# We're going to use the same discretization as in Step 1 — forward difference in time and backward difference in space.

# nx = 40  # try changing this number from 41 to 81 and Run All ... what happens?
# dx = 2 / (nx-1)
# nt = 2    #nt is the number of timesteps we want to calculate
# dt = .02  #dt is the amount of time each timestep covers (delta t)
# c = 1      #assume wavespeed of c = 1

nx = 181  # number of points, thus minus 1 elements 
dx = 2 / (nx-1) # 2 is the length that is gonna be discretizied, dx is the local spacing, space increment
nt = 90    #nt is the number of timesteps we want to calculate
dt = .00125  #dt is the amount of time each timestep covers (delta t)
#c = 1.9      #assume wavespeed of c = 1

u = numpy.ones(nx)      #numpy function ones()
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print(u)
plt.plot(numpy.linspace(0, 2, nx), u);

un = numpy.ones(nx) #initialize a temporary array
for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx):
            u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])
    plt.plot(numpy.linspace(0, 2, nx), u);

print(u)
print(un)
plt.show()

CFL= u*dt/dx
print(CFL)