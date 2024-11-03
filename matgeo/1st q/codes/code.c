#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Define a structure for 3D points
typedef struct {
    double x;
    double y;
    double z;
} Point3D;

// Function to compute the third centroid point
void thirdcentroid(Point3D* p1, Point3D* p2, Point3D* g, Point3D* c) {
    c->x = 3 * (g->x) - p1->x - p2->x;
    c->y = 3 * (g->y) - p1->y - p2->y;
    c->z = 3 * (g->z) - p1->z - p2->z;
}

int main() {
    // Define some sample points
    Point3D p1 = {3.0, -5.0, 7.0};
    Point3D p2 = {-1.0, 7.0, -6.0};
    Point3D g = {1.0, 1.0, 1.0};
    Point3D c;

    // Call the function
    thirdcentroid(&p1, &p2, &g, &c);
    FILE *file = fopen("values.tex", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
	fprintf(file, "C: (%.2f, %.2f, %.2f)\n", c.x, c.y, c.z);
    // Print the result
    printf("Third centroid point: (%.2f, %.2f, %.2f)\n", c.x, c.y, c.z);

    return 0;
}

