import math

def get_matrix(order):
    """Function to read a matrix from user input."""
    result_matrix = []
    print(f"Enter the elements for a {order}x{order} matrix row by row:")
    for row_index in range(order):
        while True:
            try:
                row_values = list(map(float, input(f"Row {row_index + 1}: ").split()))
                if len(row_values) != order:
                    print(f"Please input exactly {order} numbers for this row.")
                    continue
                result_matrix.append(row_values)
                break
            except ValueError:
                print("Invalid input. Only numeric values are allowed.")
    return result_matrix

def multiply_matrices(mat1, mat2):
    """Function to perform matrix multiplication."""
    dimension = len(mat1)
    result = [[0.0] * dimension for _ in range(dimension)]
    for i in range(dimension):
        for j in range(dimension):
            for k in range(dimension):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def calculate_norm(vector):
    """Function to compute the Euclidean norm of a vector."""
    return math.sqrt(sum(val ** 2 for val in vector))

def generate_householder(matrix, col_index):
    """Function to construct the Householder reflection matrix."""
    size = len(matrix)
    vec_x = [matrix[i][col_index] for i in range(col_index, size)]
    
    norm_val = calculate_norm(vec_x)
    r_val = -norm_val if vec_x[0] < 0 else norm_val
    
    vec_v = [0.0] * len(vec_x)
    vec_v[0] = vec_x[0] + r_val
    for i in range(1, len(vec_x)):
        vec_v[i] = vec_x[i]
    
    norm_v = calculate_norm(vec_v)
    if norm_v < 1e-10:
        return None
    
    vec_v = [element / norm_v for element in vec_v]
    
    reflector = [[1.0 if row == col else 0.0 for col in range(size)] for row in range(size)]
    for i in range(col_index, size):
        for j in range(col_index, size):
            reflector[i][j] -= 2 * vec_v[i - col_index] * vec_v[j - col_index]
    
    return reflector

def qr_factorization(matrix):
    """Function to perform QR decomposition using Householder reflections."""
    dimension = len(matrix)
    upper_tri = [row[:] for row in matrix]
    orthogonal = [[1.0 if i == j else 0.0 for j in range(dimension)] for i in range(dimension)]

    for col in range(dimension - 1):
        reflection = generate_householder(upper_tri, col)
        if reflection is None:
            continue
        
        upper_tri = multiply_matrices(reflection, upper_tri)
        orthogonal = multiply_matrices(orthogonal, reflection)

    return orthogonal, upper_tri

def find_eigenvalues(matrix, max_iter=100, tol=1e-10):
    """Function to compute eigenvalues using the QR algorithm."""
    size = len(matrix)
    current = [row[:] for row in matrix]
    
    for iteration in range(max_iter):
        q_matrix, r_matrix = qr_factorization(current)
        current = multiply_matrices(r_matrix, q_matrix)
        
        is_converged = True
        for row in range(size):
            for col in range(row):
                if abs(current[row][col]) > tol:
                    is_converged = False
                    break
            if not is_converged:
                break

        if is_converged:
            break
    
    return [current[i][i] for i in range(size)]

def main():
    """Main function to execute the QR algorithm."""
    try:
        print("QR Algorithm for Eigenvalue Calculation")

        # Prompt for matrix size
        while True:
            try:
                matrix_size = int(input("Enter the size of the matrix: "))
                if matrix_size <= 0:
                    print("Matrix size must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a valid positive integer.")
        
        # Get the matrix
        user_matrix = get_matrix(matrix_size)
        
        # Calculate eigenvalues
        eigen_vals = find_eigenvalues(user_matrix)
        
        # Display the results
        print("\nEigenvalues of the matrix:")
        for idx, eigen_val in enumerate(eigen_vals, start=1):
            print(f"Eigenvalue {idx}: {eigen_val:.6f}")
            
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

if __name__ == "__main__":
    main()

