#include <stdio.h>
/*  - variables are local to the scope in which they're defined
    - functions have global scope by default
    - static changes scope to the file containing them (up or down) */

int sum (int num) {
    static int total = 0;
    total += num;
    return total;
}

int main() {
    printf("%d ",sum(55));
    printf("%d ",sum(45));
    printf("%d ",sum(50));
    return 0;
}