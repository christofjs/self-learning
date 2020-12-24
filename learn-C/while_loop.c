#include <stdio.h>
int main() {
    int array[11] = { 1, 7, 4, 5, 9, 3, 5, 11, 6, 3, 4 };
    int i = 0;
    while (i<10) {
        if (array[i] < 5) {
            i++;
            continue;
        } else if (array[i] > 10) {
            break;
        }
        printf("The number %d is not less than 5 or greater than 10.\n", array[i]);
        i++;
    }
}