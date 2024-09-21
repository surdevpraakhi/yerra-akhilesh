# Code by GVV Sharma
# December 7, 2019
# Revised July 15, 2020
# Revised October 21, 2023
# Released under GNU GPL

import numpy as np
import matplotlib.pyplot as plt

# Function to plot a line segment between two points
def plot_line(A, B):
    x_vals = [A[0], B[0]]
    y_vals = [A[1], B[1]]
    plt.plot(x_vals, y_vals, 'bo-', markersize=8)  # Plot with blue dots and lines

# Labeling points with coordinates
def label_pts_with_coords(G_v, vert_labels): 
    for i, txt in enumerate(vert_labels):
        plt.annotate(f'{txt} ({G_v[0, i]:.1f}, {G_v[1, i]:.1f})',  # Add coordinates
                     (G_v[0, i], G_v[1, i]),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(10, 10),  # distance from text to points (x,y)
                     ha='center', fontsize=12, color='blue')  # label style

# Defining rectangle vertices
A = np.array([0, 0])    # Vertex A at the origin
B = np.array([5, 0])    # Vertex B at (5, 0) (side length 5cm)
C = np.array([5, 3.5])  # Vertex C at (5, 3.5) (side length 3.5cm from B to C)
D = np.array([0, 3.5])  # Vertex D at (0, 3.5)

# Combine the points into a single matrix for easy plotting and labeling
G_v = np.array([A, B, C, D]).T

# Plot the rectangle without distance labels
plot_line(A, B)  # Side AB
plot_line(B, C)  # Side BC
plot_line(C, D)  # Side CD
plot_line(D, A)  # Side DA

# Label vertices with their coordinates
vert_labels = ['A', 'B', 'C', 'D']
label_pts_with_coords(G_v, vert_labels)

# Set the limits for the plot for better visibility
plt.xlim(-1, 6)
plt.ylim(-1, 5)

# Adding grid, axis equal for proportionate scaling
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Rectangle with sides 5cm and 3.5cm', fontsize=16)

# Show the plot
plt.show()

