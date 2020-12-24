#include <stdio.h>
int main() {
    int array[10] = { 1,2,3,4,5,6,7,8,9,10 };
    int product = 1;
    for (int i = 0; i < 10; i++) {
        product *= array[i];
    }
    printf("The factorial of the array is %d.", product);
}