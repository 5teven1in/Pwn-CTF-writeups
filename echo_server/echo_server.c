#include"stdio.h"
#include"stdlib.h"
#include"string.h"

char cmd[128];

void runCMD(){
  system(cmd);
  return;
}

void getString(){
  char input[32] = {0};
  for(int i=0; i<128; i++)cmd[i] = 0;
  printf("> ");
  gets(input);
  strcat(cmd, "echo \'");
  for(int i=0, j=6; i<32; i++){
    if(input[i] == '\''){
      strcat(cmd, "\'\\\'\'");
      j += 4;
    }else{
      cmd[j] = input[i];
      j++;
    }
  }
  strcat(cmd, "\'");
  return;
}

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  
  printf("========= echo server =========\n");
  printf("This is an echo server.\n");
  printf("It will echo whatever you type.\n");
  printf("But not something like:\n");
  printf("/bin/sh\n");
  printf("cat /home/ctf/flag\n");
  printf("===============================\n");
 
  while(1){
    getString();
    runCMD();
  }

  return 0;
}
