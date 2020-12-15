#include"stdio.h"
#include"stdlib.h"

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  
  char text[16];

  printf("Give me your text :");
  gets(text);

  return 0;
}
