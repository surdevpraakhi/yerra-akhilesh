// circle.c
#include <stdio.h>
#include <math.h>

void circle_equation(double P[], double R[], double *Q, double *r) {
    double A[3][3];
    double b[3];
    double x[3];

    // Line parameters (using point P as the normal vector)
    double n[2] = {P[0], P[1]};
    double c = 5;

    // Entering equations in matrix form
    A[0][0] = 2 * P[0];
    A[0][1] = 2 * R[0];
    A[0][2] = n[0];
    A[1][0] = 2 * P[1];
    A[1][1] = 2 * R[1];
    A[1][2] = n[1];
    A[2][0] = 1;
    A[2][1] = 1;
    A[2][2] = 0;

    b[0] = -pow(P[0], 2) - pow(P[1], 2);
    b[1] = -pow(R[0], 2) - pow(R[1], 2);
    b[2] = -c;

    // Solve the system of equations using Gaussian elimination (simplified here)
    // NOTE: Proper implementation would require a full solver for real use

    // Set Q and r (these would be calculated in a real implementation)
    Q[0] = -x[0];
    Q[1] = -x[1];
    *r = sqrt(pow(x[0], 2) + pow(x[1], 2) - x[2]);
}


