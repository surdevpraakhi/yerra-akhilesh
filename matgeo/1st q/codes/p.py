


#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/yerra/matgeo/codes/book')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import ctypes
from ctypes import Structure, c_double
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
# Define the Point3D and Results structures
class Point3D(Structure):
    _fields_ = [("x", c_double),
                ("y", c_double),
                ("z", c_double)]


# Load the shared library
lib = ctypes.CDLL('./centroid.so')

# Define the argument and return types of the function
lib.thirdcentroid.argtypes = [ctypes.POINTER(Point3D), ctypes.POINTER(Point3D), ctypes.POINTER(Point3D), ctypes.POINTER(Point3D)]
lib.thirdcentroid.restype = None

def thirdcentroid(np_point1, np_point2, np_point3):
    # Convert numpy arrays to Point3D structures
    point1 = Point3D(np_point1[0], np_point1[1], np_point1[2])
    point2 = Point3D(np_point2[0], np_point2[1], np_point2[2])
    point3 = Point3D(np_point3[0], np_point3[1], np_point3[2])
    
    # Create a Results structure to hold the output
    result = Point3D()
    
    # Call the C function
    lib.thirdcentroid(ctypes.byref(point1), ctypes.byref(point2), ctypes.byref(point3), ctypes.byref(result))
    
    return result

#Given points
A = np.array(([3, -5,7]), dtype = np.double).reshape(-1,1) 
B = np.array(([-1,7, -6]), dtype=np.double).reshape(-1,1)  

G = np.array(([1,1, 1]), dtype = np.double).reshape(-1,1)  
Cc = thirdcentroid(A,B,G)
C = np.array(([Cc.x,Cc.y,Cc.z])).reshape(-1,1)  
# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

#Generating all lines
x_BC = line_gen(B,C)
x_AB = line_gen(A,B)
x_AC = line_gen(A,C)


#Plotting all lines
ax.plot(x_BC[0,:],x_BC[1,:], x_BC[2,:],label='$BC$')
ax.plot(x_AC[0,:],x_AC[1,:], x_AC[2,:],label='$AC$')
ax.plot(x_AB[0,:],x_AB[1,:], x_AB[2,:],label='$AB$')

# Scatter plot
colors = np.arange(1, 5)  # Example colors
tri_coords = np.block([A, B, C, G])  # Stack A, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['A', 'B', 'C', 'G']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})',
             fontsize=9, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')

plt.show()

