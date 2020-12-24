//#include <stdio.h>
//#include <string.h>
//int main() {
//    char first_name[] = "John";
//    char last_name[] = "Doe";
//    printf("Your name is %s %s.\n", first_name, last_name);
//    strncat(first_name,last_name,3);
//// strncat requires that dest be a char[] declaration, not char*
//    printf("Your concatenated name is %s.\n", first_name);
//}
#include <stdio.h>
#include <string.h>
int main() {
  char *first_name = "John";
  char last_name[] = "Doe";
  char name[100];

  last_name[0] = 'B';
  sprintf(name, "%s %s", first_name, last_name);
  if (strncmp(name, "John Boe", 100) == 0) {
      printf("Done!\n");
  }
  name[0]='\0';
  strncat(name,first_name,4);
  strncat(name,last_name,20);
  printf("%s\n",name);
  return 0;
}