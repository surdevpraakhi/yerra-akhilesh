import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
lib = ctypes.CDLL('./distances.so')

# Define argument and return types of the functions in the .so file
lib.createMat.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
lib.Matnorm.restype = ctypes.c_double
lib.Matsub.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

# Create matrices for points P, Q, and R
def create_point(x, y):
    point = lib.createMat(2, 1)
    point[0][0] = ctypes.c_double(x)
    point[1][0] = ctypes.c_double(y)
    return point

P = create_point(5, -3)
Q = create_point(0, 1)
R = create_point(4, 6)  # For x = 4

# Calculate the distances
PQ = lib.Matsub(P, Q, 2, 1)
QR = lib.Matsub(Q, R, 2, 1)

dist_PQ = lib.Matnorm(PQ, 2)
dist_QR = lib.Matnorm(QR, 2)

print(f"Distance PQ: {dist_PQ}")
print(f"Distance QR: {dist_QR}")

# Plot the points
x_vals = [5, 0, 4]
y_vals = [-3, 1, 6]

plt.plot(x_vals, y_vals, marker='o')
plt.text(5, -3, 'P(5, -3)', fontsize=12)
plt.text(0, 1, 'Q(0, 1)', fontsize=12)
plt.text(4, 6, 'R(4, 6)', fontsize=12)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Points P, Q, and R')
plt.grid(True)
plt.show()

