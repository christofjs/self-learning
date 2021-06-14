/*
store data without having to know size first
    - need pointer for new location memory
*/
// normal for defining structure
// #include <stdio.h>
// #include <stdlib.h>
// typedef struct {
//     char * name;
//     int age;
// } person;

// int main() {
// // new allocation method
//     person * myperson = (person *)malloc(sizeof(person));
//     myperson->name = "John";
//     myperson->age = 27;
//     // releases memory allocation - not var itself, just data being pointed to
//     free(myperson);
// }

#include <stdlib.h>
#include <stdio.h>
