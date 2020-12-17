#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MALLOC_SIZE 0x80

int input();


int main(int argc, char *argv[])
{
    int select;
    unsigned long long size = 0x20;
    unsigned long long victim = 0x1337;
    char *ary[4];
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("victim's address:%p\n", &victim);
    printf("size's address:%p\n", &size);
    printf("ary's adr:%p\n", &ary[0]);
    printf("(0)free\n(1)malloc\n(2)write\n(3)show\ninput: ");
    while((select = input()) != EOF)
    {
        if(select == 1) // x = malloc
        {
            printf("ary[x] = malloc(%d) // (0 <= x <= 3)\nx = ", MALLOC_SIZE);
            if((select = input()) != EOF) ary[select] = (char *) malloc(MALLOC_SIZE);
            else printf("invalid number\n");
            printf("adr:%p\n", ary[select]);
        }
        else if(select == 0) // free(x)
        {
            printf("free(ary[x]) // (0 <= x <= 3)\nx = ");
            if((select = input()) != EOF)
            {
                free(ary[select]);
            }
            else printf("invalid number\n");
        }
        else if(select == 2) // x = string
        {
            printf("*ary[x] = string // (0 <= x <= 3)\nx = ");
            while((select = input()) == EOF)
            {
                printf("invalid number\n");
                printf("*ary[x] = string // (0 <= x <= 3)\nx = ");
            }
            printf("string = ");
            read(0, ary[select], 0xa0);
        }
        else if(select == 3) // show x
        {
            printf("print *ary[x] // (0 <= x <= 3)\nx = ");
            if((select = input()) != EOF) printf("your string:\n%s\n", ary[select]);
            else printf("invalid number\n");
        }
        printf("(0)free\n(1)malloc\n(2)write\n(3)show\ninput: ");
    }
    
    if(victim == 0xdeadbeef)
    {
        system("cat flag");
    }
    printf("Goodbye!\n");
    return 0;
}


int input()
{
    int select;
    if(scanf("%d", &select) != EOF)
    {
        printf("%d\n", select);
        return (select >= 0 && select <= 3) ? select : EOF;
    }
    else
    {
        return EOF;
    }
}
