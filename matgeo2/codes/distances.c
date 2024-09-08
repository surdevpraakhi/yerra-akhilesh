#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Function declarations (as provided in the original code)
double **createMat(int m, int n);
double Matnorm(double **a, int m);
double **Matsub(double **a, double **b, int m, int n);

// Main function
int main() {
    // Define points P, Q, and R as matrices
    double **P = createMat(2, 1);
    P[0][0] = 5;
    P[1][0] = -3;
    
    double **Q = createMat(2, 1);
    Q[0][0] = 0;
    Q[1][0] = 1;
    
    double **R = createMat(2, 1);
    R[0][0] = 4;  // Assume x = 4 for first case
    R[1][0] = 6;
    
    // Calculate the distances
    double **PQ = Matsub(P, Q, 2, 1);
    double **QR = Matsub(Q, R, 2, 1);
    
    double dist_PQ = Matnorm(PQ, 2);
    double dist_QR = Matnorm(QR, 2);
    
    // Print the distances
    printf("Distance PQ: %lf\n", dist_PQ);
    printf("Distance QR: %lf\n", dist_QR);
    
    // Clean up memory
    free(P);
    free(Q);
    free(R);
    free(PQ);
    free(QR);
    
    return 0;
}

// Function definitions
double **createMat(int m, int n) {
    double **a = (double **)malloc(m * sizeof(double *));
    for (int i = 0; i < m; i++) {
        a[i] = (double *)malloc(n * sizeof(double));
    }
    return a;
}

double **Matsub(double **a, double **b, int m, int n) {
    double **c = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            c[i][j] = a[i][j] - b[i][j];
        }
    }
    return c;
}

double Matnorm(double **a, int m) {
    double sum = 0;
    for (int i = 0; i < m; i++) {
        sum += a[i][0] * a[i][0];
    }
    return sqrt(sum);
}

