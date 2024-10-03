# Program to plot the area bounded by the curves y = x^2 + 2 and y = x
# Code by GVV Sharma
# Released under GNU GPL
# August 10, 2020
# Revised July 31, 2024

import numpy as np
import matplotlib.pyplot as plt
import sys                                          # for path to external scripts
sys.path.insert(0, '/home/yerra/Desktop/assignments/matgeo/codes/CoordGeo')  # path to my scripts

# Setting up the plot
fig, ax = plt.subplots(figsize=(10, 6))  # Set figure size for better clarity
len = 100
x = np.linspace(-1, 4, len)

# Function definitions for the curves
def f1(x):
    return x**2 + 2  # y = x^2 + 2

def f2(x):
    return x  # y = x

# Generate the curve points
y1 = f1(x)
y2 = f2(x)

# Plotting the curves
ax.plot(x, y1, label=r'$y = x^2 + 2$', color='red', linewidth=2)
ax.plot(x, y2, label=r'$y = x$', color='green', linewidth=2)

# Add vertical lines at x = 0 and x = 3
x_line1 = 0
x_line2 = 3
ax.axvline(x=x_line1, color='blue', linestyle='--', linewidth=1.5, label='$x = 0$')
ax.axvline(x=x_line2, color='cyan', linestyle='--', linewidth=1.5, label='$x = 3$')

# Fill the region between the curves
x_fill = np.linspace(0, 3, len)
y1_fill = f1(x_fill)
y2_fill = f2(x_fill)
ax.fill_between(x_fill, y1_fill, y2_fill, where=(y1_fill > y2_fill), color='lightgray', alpha=0.5, label='Area between curves')

# Adjusting the plot aesthetics
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.legend(loc='upper left', fontsize=10)
ax.grid(True)  # Show grid

# Set limits for better visibility
ax.set_xlim(-1, 4)  # Extend x limits
ax.set_ylim(-3, 6)  # Adjust y limits to show y=x line below x-axis
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.set_title('Area Bounded by the Curves', fontsize=14)

# Adding the y=x line below the x-axis
ax.plot(x, f2(x), color='green', linewidth=1, linestyle='--', label=r'$y = x$ (Extended)$')

# Labeling the coordinates at the points of intersection
intersection_points = [(0, f1(0)), (3, f1(3))]
for point in intersection_points:
    ax.scatter(*point, c='black')
    ax.annotate(f'({point[0]}, {point[1]})', point, textcoords="offset points", xytext=(-15, 10), ha='center', fontsize=10)

# Save the plot to a file
plt.savefig('bounded_area_plot_with_y_equals_x.png')



# Show the plot (optional, uncomment if not using Termux)
plt.show()

