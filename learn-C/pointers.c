/*
pointers are simple integer variables with a memory address pointing to a value, instead of the value itself
*/

/*
char * name = "John";
    - allocates local (stack) var called name, pointer to single char
    - causes string "John" to appear somewhere in memory with null terminator (\0)
    - initializes name arg to point to where J is
int * pointer_to_a = &a
    - create pointer to address of int a
*/

/*
dereferencing - refer to where pointer points rather than mem address
    - done using asterisk operator
*/
#include <stdio.h>
int main() {
    int n = 1;
    int * pointer_to_n = &n;
    *pointer_to_n += 1;
    printf("The value of n is %d.", n);
    char * name_pointer = "John";
    printf("The second letter of John is %c", name_pointer[1]);
}