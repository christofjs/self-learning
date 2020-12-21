#include <stdio.h>
#include <string.h>

int main() {
    int grades[][5] = {
        {80,70,65,89,90},
        {85,80,80,82,87}
    };
    float avg;
    int i;
    int j;
    char *sub;
    for (i = 0; i < 2; i ++) {
        avg = 0;
        for (j = 0; j < 5; j++) {
            avg += grades[i][j];
        }
        avg /= 5;
        printf("The average of the %d grades is %.2f\n", i, avg);
    }
    return 0;
}