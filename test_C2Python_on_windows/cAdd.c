#include "math.h"

void cos_(int size, double* x, double* y){

    int i;

    for (i=0;i<size;i++){
        y[i] = cos(x[i]);
    }
}
