#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 5 15:05:21 2024

@author: karasu
"""
########## 12 Steps to Navıer-Stokes - Step 1: Linear convection ##########
import numpy                      
from matplotlib import pyplot      #here we load matplotlib
import time, sys                   #and load some utilities

## Pre-defined initial conditions 
# nx = 41  # try changing this number from 41 to 81 and Run All ... what happens?  The signal gets more rectangular, the CFL condition is satisfied.
# dx = 2 / (nx-1)
# nt = 25    #nt is the number of timesteps we want to calculate
# dt = .025  #dt is the amount of time each timestep covers (delta t)
# c = 1      #assume wavespeed of c = 1

## Self-defined initial conditions 

nx = 181  # number of points, thus minus 1 elements 
dx = 2 / (nx-1) # 2 is the length that is gonna be discretizied, dx is the local spacing, space increment
nt = 90    #nt is the number of timesteps we want to calculate
dt = .0025  #dt is the amount of time each timestep covers (delta t)
c = 1.9      #assume wavespeed of c = 1

## Wave definition

u = numpy.ones(nx)      #numpy function ones() defining the wave
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print(u)

pyplot.plot(numpy.linspace(0, 2, nx), u); # initial hat function wave 

un = numpy.ones(nx) # initialize a temporary array

for n in range(nt):  # loop for values of n from 0 to nt, so it will run nt times, first loop for the time
     un = u.copy() # copy the existing values of u into un
     pyplot.plot(numpy.linspace(0, 2, nx), u); # hat function wave in nth tıme step
     #for i in range(1, nx): ## you can try commenting this line and...
     for i in range(nx): ## ... uncommenting this line and see what happens! second loop for the space
         u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
         
         
pyplot.plot(numpy.linspace(0, 2, nx), u); # hat function wave at the last time step 