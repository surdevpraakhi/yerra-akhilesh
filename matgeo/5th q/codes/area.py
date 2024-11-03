#Code by GVV Sharma
#Released under GNU GPL
#August 10, 2020
#Revised July 31, 2024

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/yerra/Desktop/assignments/matgeo/codes/CoordGeo')        #path to my scripts

#if using termux
import subprocess
import shlex
#end if

# Define the functions for the curves
def f1(x):
    return x**2 + 2  # y = x^2 + 2

def f2(x):
    return x  # y = x (the line)

# Integration limits
x_start = 0
x_end = 3

# Function to find the difference between the curves
def area_func(x):
    return f1(x) - f2(x)

# Calculate the area using definite integration
area, _ = quad(area_func, x_start, x_end)
print(f"The area of the region is: {area} square units")

# Plotting the curves and the region
x_vals = np.linspace(x_start, x_end, 1000)
y_vals_f1 = f1(x_vals)
y_vals_f2 = f2(x_vals)

# setting up the plot
fig = plt.figure(figsize=(8, 6))  # Larger figure size for better visibility
ax = fig.add_subplot(111)

# Plot the curves with thicker lines
plt.plot(x_vals, y_vals_f1, label='$y = x^2 + 2$', color='blue', linewidth=2)
plt.plot(x_vals, y_vals_f2, label='$y = x$', color='green', linestyle='-.', linewidth=2)

# Highlight x = 0 and x = 3 with vertical lines
plt.axvline(x=x_start, color='red', linestyle='--', label='$x=0$', linewidth=1.5)
plt.axvline(x=x_end, color='purple', linestyle='--', label='$x=3$', linewidth=1.5)

# Fill the area between the curves
plt.fill_between(x_vals, y_vals_f1, y_vals_f2, where=(y_vals_f1 > y_vals_f2), color='gray', alpha=0.3)

# Highlight the end points with scatter plot and annotate
end_points_x = [0, 3, 0, 3]
end_points_y = [0, 3, 2, 11]
plt.scatter(end_points_x, end_points_y, color='black', zorder=5)  # Highlight points

# Annotating the points
plt.text(0, 0, '$(0, 0)$', horizontalalignment='right', verticalalignment='top', fontsize=12)
plt.text(3, 3, '$(3, 3)$', horizontalalignment='left', verticalalignment='top', fontsize=12)
plt.text(0, 2, '$(0, 2)$', horizontalalignment='right', verticalalignment='bottom', fontsize=12)
plt.text(3, 11, '$(3, 11)$', horizontalalignment='left', verticalalignment='bottom', fontsize=12, color='red')  # Made (3, 11) text red for better visibility

# Enhancing the x and y axes
ax.spines['left'].set_position('zero')  # Moving y-axis to x=0
ax.spines['bottom'].set_position('zero')  # Moving x-axis to y=0
ax.spines['right'].set_color('none')  # Hide right spine
ax.spines['top'].set_color('none')    # Hide top spine
ax.xaxis.set_ticks_position('bottom')  # Tick marks for x-axis
ax.yaxis.set_ticks_position('left')    # Tick marks for y-axis

# Setting x and y limits for better framing
plt.xlim(-1, 4)  # Extra space around the x-axis for clarity
plt.ylim(-1, 14)  # Extended ylim to ensure (3,11) is clearly visible

# Set grid with lighter lines for a clearer plot
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Configure the plot
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.title('Area between curves $y = x^2 + 2$ and $y = x$', fontsize=16)
plt.legend(loc='best', fontsize=12)
plt.gca().set_aspect('equal', adjustable='box')  # Maintain equal aspect ratio

# if using termux
# plt.savefig('chapters/11/11/2/1/figs/area_fig_highlighted_points.pdf')
# subprocess.run(shlex.split("termux-open chapters/11/11/2/1/figs/area_fig_highlighted_points.pdf"))
# else
plt.show()

