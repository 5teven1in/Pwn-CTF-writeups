#include"stdio.h"
#include"stdlib.h"

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  int token = 0xabcd;
  char key[16];
  char check;

  while(1){
    printf("Please input your key :");
    scanf("%s", key);

    printf("Your key is ");
    printf(key);
    printf("\n");

    printf("Are you sure ? (Y/N)");
    getchar();
    scanf("%c", &check);
    if(check == 'Y')break;
  }

  if((int)token == 0xab37){
    printf("Door open. OwO\n");
    system("cat /home/ctf/flag");
  }else{
    printf("Cannot open door. QwQ\n");
  }

  return 0;
}
