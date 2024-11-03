#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

// Function for y = x^2 + 2
double f1(double x) {
    return x * x + 2;
}

// Function for y = x
double f2(double x) {
    return x;
}

// Function to calculate the difference between f2(x) and f1(x)
double area_difference(double x) {
    return f2(x) - f1(x);
}

// Trapezoidal rule for numerical integration
double trapezoidal_rule(double a, double b, int n) {
    double h = (b - a) / n; // Width of each small interval
    double area = 0.0;
    
    // Calculate the area using the trapezoidal rule
    for (int i = 0; i < n; i++) {
        double x1 = a + i * h;        // Left endpoint
        double x2 = a + (i + 1) * h;  // Right endpoint
        area += (area_difference(x1) + area_difference(x2)) * h / 2; // Area of trapezoid
    }
    
    return fabs(area); // Return the absolute value since area cannot be negative
}

int main() {
    double a = 0.0; // Lower bound
    double b = 3.0; // Upper bound
    int n = 1000;   // Number of subintervals

    double area = trapezoidal_rule(a, b, n);

    // Write the result to a .tex file
    FILE *file = fopen("values.tex", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the area result to the file in the same format
    fprintf(file, "The area of the region bounded by the curves $y = x^2 + 2$, the lines $y = x$, $x = 0$, and $x = 3$ is: A\n");

    fprintf(file, "A = %.4f\n", area);

    fclose(file);

    printf("Area calculated: %.4f\n", area);
    printf("Result written to values.tex\n");

    return 0;
}

