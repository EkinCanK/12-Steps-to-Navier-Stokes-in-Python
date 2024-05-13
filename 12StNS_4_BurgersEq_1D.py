#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:45:49 2024

@author: karasu
"""

########## 12 Steps to Navıer-Stokes - Step 4: Burgers' eq. 1D ##########

# The one-dimensional Burgers' equation - Forward difference in time and Backwards difference in time for the first derivative in space  . 
# central difference for the diffusion term (istoropic diffusion)

import numpy
import sympy
from sympy import init_printing
from sympy.utilities.lambdify import lambdify
from matplotlib import pyplot

### Analytical Solution
x, nu, t = sympy.symbols('x nu t')
phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
       sympy.exp(-(x - 4 * t - 2 * numpy.pi)**2 / (4 * nu * (t + 1))))

phiprime = phi.diff(x)
u = -2 * nu * (phiprime / phi) + 4
ufunc = lambdify((t, x, nu), u)

### Variable declarations - Numerical Solution Input time and local spacing
# nx = 101
# nt = 500
# nu = .07

nx = 121
nt = 15  #changing number of time steps, as we are closer to 1 computational approach is closer to analytical solution
nu = .1
dx = 2 * numpy.pi / (nx - 1) # length of the nodes and local spacing

dt = dx * nu # time step depending on local spacing - decent time step insurence due to CFL Condition

# Initialization

x = numpy.linspace(0, 2 * numpy.pi, nx)
un = numpy.empty(nx)
t = 0

#initial wave function solution
u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])

# Plot of the initial analztical function

pyplot.figure(figsize=(11, 7), dpi=100)
pyplot.plot(x, u, marker='o', lw=2)
pyplot.xlim([0, 2 * numpy.pi])
pyplot.ylim([0, 10]);

### Numerical calculation
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt / dx *(un[i] - un[i-1]) + nu * dt / dx**2 *\
                (un[i+1] - 2 * un[i] + un[i-1])
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 *\
                (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0] # periodic B.C - last point in your wave equals to first point in space
# which means if the wave propagetes the last point will come as the first point for the calculation        
    u_analytical = numpy.asarray([ufunc(nt * dt, xi, nu) for xi in x])

### Plotting
    pyplot.figure(figsize=(11, 7), dpi=100)
    pyplot.plot(x,u, marker='o', lw=2, label='Computational')
    pyplot.plot(x, u_analytical, label='Analytical')
    pyplot.xlim([0, 2 * numpy.pi])
    pyplot.ylim([0, 10])
    pyplot.legend();

pyplot.show()