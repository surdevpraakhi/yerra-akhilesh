# Code by Parv Chandola
# May 11, 2024
# Revised July 26, 2024
# by GVV Sharma
# released under GNU GPL
# Circle equation

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys  # for path to external scripts
sys.path.insert(0, '/home/yerra/Desktop/assignments/matgeo/codes/CoordGeo')  # path to my scripts

# local imports
from conics.funcs import circ_gen
from line.funcs import *

# if using termux
import subprocess
import shlex

# Define points P and R
P = np.array([5, -3]).reshape(-1, 1)  # Point P (5, -3)
R = np.array([4, 6]).reshape(-1, 1)  # Point R (4, 6)

# Line parameters (based on P)
n = np.array([5, -3]).reshape(-1, 1)  # The normal vector
c = 5  # constant c for line equation

# Entering equations in matrix form
A = np.block([[2*P, 2*R, n], [1, 1, 0]]).T  # Form the matrix A
b = -np.array([LA.norm(P)**2, LA.norm(R)**2, c]).reshape(-1, 1)  # vector b
x = LA.solve(A, b)  # Solve the system of equations

# Centre and radius of the circle
u = x[:2]  # Extract the center (Q)
Q = -u  # Center of the circle (negating u)
f = x[2][0]  # The last value is f
r = np.sqrt(LA.norm(u)**2 - f)  # Radius of the circle
print(Q, r)  # Print the center and radius

# Generating circle points
x_circ = circ_gen(Q, r)

# Generating lines
k1 = -2
k2 = 0
x_A = line_norm(n, c, k1, k2)

# Plotting all lines and circles
plt.plot(x_A[0, :], x_A[1, :], label='$(4 \quad 5)\mathbf{x}=5$')  # Plot line
plt.plot(x_circ[0, :], x_circ[1, :], label='$Circle$')  # Plot circle

colors = np.arange(1, 4)
# Labeling the coordinates
tri_coords = np.block([P, R, Q])  # Create block matrix for coordinates
plt.scatter(tri_coords[0, :], tri_coords[1, :], c=colors)
vert_labels = ['$\mathbf{P}$', '$\mathbf{R}$', '$\mathbf{Q}$']  # Labels for P, R, and Q
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f})',
                 (tri_coords[0, i], tri_coords[1, i]),  # position to label
                 textcoords="offset points",  # how to position the text
                 xytext=(-20, 5),  # distance from text to points (x, y)
                 ha='center')  # horizontal alignment

# Set axes styles and position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Show grid and legend
plt.legend(loc='best')
plt.grid()  # minor
plt.show()

