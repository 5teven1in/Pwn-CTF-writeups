#include"stdio.h"
#include"stdlib.h"

void Billyshouse(){
  system("cat /home/ctf/flag");
}

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);

  char address[32];

  printf("Billy want to go home now.\n");
  printf("Do you know the address of his house ?");

  gets(address);

  return 0;
}
