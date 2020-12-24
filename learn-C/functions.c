#include <stdio.h>
void print_big(int num);

void main() {
    print_big(3);
    print_big(9);
    print_big(39);
    print_big(93);
}

void print_big(int num) {
    if (num > 10) {
        printf("%d is big.\n", num);
    }
}