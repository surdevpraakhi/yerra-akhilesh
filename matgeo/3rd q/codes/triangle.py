# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# released under GNU GPL
# Point Vectors

import sys                                          # for path to external scripts
sys.path.insert(0, '/home/yerra/Desktop/assignments/matgeo/codes/CoordGeo')        # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


# end if

I = np.eye((2))
e1 = I[:, 0].reshape(-1, 1)

# Updated given points
A = np.array(([3, 5.196])).reshape(-1, 1)  # Coordinates of A
B = np.array(([0, 0])).reshape(-1, 1)      # Coordinates of B
C = np.array(([6, 0])).reshape(-1, 1)      # Coordinates of C

# Distances
d1 = LA.norm(A - C)

# Generating all lines
x_AC = line_gen(A, C)
x_CB = line_gen(C, B)
x_AB = line_gen(A, B)

# Plotting all lines
plt.plot(x_AC[0, :], x_AC[1, :], label='$AC$')
plt.plot(x_CB[0, :], x_CB[1, :], label='$CB$')
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')

# Labeling the coordinates
tri_coords = np.block([[A, B, C]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.3f}, {tri_coords[1,i]:.3f})',
                 (tri_coords[0, i], tri_coords[1, i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(20, 5),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right, or center

# Set axis properties
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')

# Display the plot
plt.show()

