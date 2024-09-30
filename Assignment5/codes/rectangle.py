#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/yerra/Desktop/assignments/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

# Given points
A = np.array(([0, 3.5, 0])).reshape(-1, 1) 
B = np.array(([5, 3.5, 0])).reshape(-1, 1)  
C = np.array(([5, 0, 0])).reshape(-1, 1)  
D = np.array(([0, 0, 0])).reshape(-1, 1)  # Additional point D

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Generating lines between points
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CD = line_gen(C, D)
x_DA = line_gen(D, A)

# Plotting all lines
ax.plot(x_AB[0, :], x_AB[1, :], x_AB[2, :], label='$AB$', color='blue')
ax.plot(x_BC[0, :], x_BC[1, :], x_BC[2, :], label='$BC$', color='orange')
ax.plot(x_CD[0, :], x_CD[1, :], x_CD[2, :], label='$CD$', color='green')
ax.plot(x_DA[0, :], x_DA[1, :], x_DA[2, :], label='$DA$', color='red')

# Scatter plot
colors = np.arange(1, 5)  # Updated colors for four points
tri_coords = np.block([A, B, C, D])  # Stack A, B, C, D vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['A', 'B', 'C', 'D']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i],
            f'{txt}\n({tri_coords[0, i]:.1f}, {tri_coords[1, i]:.1f}, {tri_coords[2, i]:.1f})',
            fontsize=12, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.grid()  # minor
plt.legend(loc='best')
plt.show()

