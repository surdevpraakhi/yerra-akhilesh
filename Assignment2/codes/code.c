

#include <math.h>
#include <stdlib.h>
// Define a structure for 3D points
typedef struct {
    double x;
    double y;
    double z;
} Point3D;


// Function to compute four outputs: distance, midpoint, vector, and squared distance
void thirdcentroid(Point3D* p1, Point3D* p2,Point3D* g, Point3D* c) {
    
    c->x = 3*(g->x) - p1->x - p2->x;
    c->y = 3*(g->y) - p1->y - p2->y;
    c->z = 3*(g->z) - p1->z - p2->z;
 
}

