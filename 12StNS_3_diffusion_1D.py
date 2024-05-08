#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:34:39 2024

@author: karasu
"""

import numpy              			   
from matplotlib import pyplot as plt 

########## 12 Steps to Navıer-Stokes - Step 3: diffusion_1D ##########

# The one-dimensional diffusion equation —unlike the previous two simple equations we have studied— has a second-order derivative. 

# Initial Conditions
# nx = 41
# dx = 2 / (nx - 1)
# nt = 20    #the number of timesteps we want to calculate
# nu = 0.3   #the value of viscosity
# sigma = .2 #sigma is a parameter, we'll learn more about it later

nx = 161
dx = 2 / (nx - 1)
nt = 20   #the number of timesteps we want to calculate
nu = 0.3   #the value of viscosity
sigma = .2 #sigma is a parameter, we'll learn more about it later
dt = sigma * dx**2 /nu #dt  time step is defined after nu and sigma and dx
print(dt)

u = numpy.ones(nx)      #a numpy array with nx elements all equal to 1.
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s

# Calculation
un = numpy.ones(nx) #our placeholder array, un, to advance the solution in time
for n in range(nt):  #iterate through time
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])
        
    plt.plot(numpy.linspace(0, 2, nx), u);
plt.show();