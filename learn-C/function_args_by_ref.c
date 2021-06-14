/*
Passing variables by reference allows the function to manipulate them, passing the variable itself passes a copy of it
*/

// #include <stdio.h>
// int main() {
//     // passing via n here would not result in an update
//     void addone(int * n) {
//         (*n)++;
//     }
//     int n = 0;
//     printf("Before: %d\n", n);
//     // same - make sure to pass address to address, rather than variable to address
//     addone(&n);
//     printf("After: %d\n", n);
// }

/*
Pointers to structures
    - instead of sending pointers to structure elements individually
*/
// #include <stdio.h>
// int main() {
//     typedef struct {
//         int x;
//         int y;
//     } point;
//     point p;
//     p.x = 0;
//     p.y = 0;
//     printf("X = %d, Y = %d\n", p.x, p.y);

//     // receives structure pointer - modifies structure vars
//     void move(point * p) {
//         (*p).x++; // or p->x++;
//         (*p).y++; // or p->y++;
//     }
//     // reference point by address
//     move(&p);
//     printf("X = %d, Y = %d\n", p.x, p.y);
// }

#include <stdio.h>
typedef struct {
    char * name;
    int age;
} person;

void birthday(person * blah) {
    blah->age++;
}

int main() {
    person john;
    john.name = "John";
    john.age = 20;
    printf("Before age: %d\n", john.age);
    birthday(&john);
    printf("After age: %d\n", john.age);
}