import math

def read_matrix(size):
    matrix = []
    print(f"Enter the elements row by row ({size}x{size} matrix):")
    for i in range(size):
        while True:
            try:
                row = list(map(float, input(f"Row {i + 1}: ").split()))
                if len(row) != size:
                    print(f"Please enter exactly {size} numbers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return matrix

def matrix_multiply(A, B):
    n = len(A)
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def vector_norm(v):
    return math.sqrt(sum(x * x for x in v))

def householder_reflection(A, k):
    n = len(A)
    x = [A[i][k] for i in range(k, n)]
    
    norm_x = vector_norm(x)
    r = -norm_x if x[0] < 0 else norm_x
    
    v = [0.0] * len(x)
    v[0] = x[0] + r
    for i in range(1, len(x)):
        v[i] = x[i]
    
    norm_v = vector_norm(v)
    if norm_v < 1e-10:
        return None
    
    v = [vi / norm_v for vi in v]
    
    H = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for i in range(k, n):
        for j in range(k, n):
            H[i][j] -= 2 * v[i-k] * v[j-k]
    
    return H

def qr_decomposition(A):
    n = len(A)
    R = [row[:] for row in A]
    Q = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for k in range(n-1):
        H = householder_reflection(R, k)
        if H is None:
            continue
        
        R = matrix_multiply(H, R)
        Q = matrix_multiply(Q, H)

    return Q, R

def qr_algorithm(A, max_iterations=100, tolerance=1e-10):
    n = len(A)
    current_A = [row[:] for row in A]
    
    for _ in range(max_iterations):
        Q, R = qr_decomposition(current_A)
        current_A = matrix_multiply(R, Q)
        
        # Check convergence
        converged = True
        for i in range(n):
            for j in range(i):
                if abs(current_A[i][j]) > tolerance:
                    converged = False
                    break
            if not converged:
                break

        if converged:
            break
    
    return [current_A[i][i] for i in range(n)]

def main():
    try:
        # Get matrix size
        while True:
            try:
                n = int(input("Enter the size of the matrix: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        
        # Read matrix
        A = read_matrix(n)
        
        # Compute eigenvalues
        eigenvalues = qr_algorithm(A)
        
        # Print results
        print("\nEigenvalues:")
        for i, eigenvalue in enumerate(eigenvalues, 1):
            print(f"Î»{i} = {eigenvalue:.6f}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
