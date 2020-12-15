#include"stdio.h"
#include"time.h"
#include"stdlib.h"

int id_backup;

void systemAdmin(){
  system("/bin/sh");
}

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  
  srand(time(NULL));
  int id = rand()%100;
  id_backup = id;
  char name[16];
  char email[32];

  printf("Weclome to registration.\n");
  printf("Here is your id :%d\n", id);
  printf("Please filled in information below to complete registration.\n");

  printf("Name:");
  gets(name);

  printf("email:");
  gets(email);

  if(id != id_backup){
    printf("Oops! some error occured.\n");
    exit(0);
  }

  return 0;
}
