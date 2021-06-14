// #include <stdio.h>
// int main() {
// /*
// Structures
//     - variables that contain variables
//     - foundation for objects and classes

// Point
//     - single entity that contains x and y
// */

//     struct point {
//         int x;
//         int y;
//     };
    
//     struct point p;
//     p.x = 10;
//     p.y = 5;

// /*
// Typedef
//     - define types with a different name
//         - useful for structs and ptrs
// */

//     typedef struct {
//         int x;
//         int y;
//     } point2;

//     point2 q;

// /*
// can also hold pointers to strings or other structures
// */
//     typedef struct {
//         char * brand;
//         int model;
//     } vehicle;

//     vehicle mycar;
//     mycar.brand = "Ford";
//     mycar.model = 2007;

// }

#include <stdio.h>
typedef struct {
    char * name;
    int age;
} person;

int main() {
    person john;
    john.name = "John";
    john.age = 27;
    printf("%s is %d years old.", john.name, john.age);
}