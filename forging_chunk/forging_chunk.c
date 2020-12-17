#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int input();


int main(int argc, char *argv[])
{
    int select;
    unsigned long long size = 0x20;
    unsigned long long victim;
    char *ary[4];
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("victim's address:%p\n", &victim);
    printf("size's address:%p\n", &size);
    printf("(0)free\n(1)malloc\n(2)write\n(3)show\ninput: ");
    while((select = input()) != EOF)
    {
        if(select == 1) // x = malloc
        {
            printf("ary[x] = malloc(8) // (0 <= x <= 3)\nx = ");
            if((select = input()) != EOF) ary[select] = (char *) malloc(8);
            else printf("invalid number\n");
            printf("adr:%p\n", ary[select]);
        }
        else if(select == 0) // free(x)
        {
            printf("free(ary[x]) // (0 <= x <= 3)\nx = ");
            if((select = input()) != EOF) free(ary[select]);
            else printf("invalid number\n");
        }
        else if(select == 2) // x = string
        {
            char *p;
            printf("*ary[x] = string // (0 <= x <= 3)\nx = ");
            while((select = input()) == EOF)
            {
                printf("invalid number\n");
                printf("*ary[x] = string // (0 <= x <= 3)\nx = ");
            }
            p = ary[select];
            printf("string = ");
            scanf("%s", p);
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
        system("cat flag.txt");
    }
    printf("Goodbye!\n");
    return 0;
}


int input()
{
    int select;
    if(scanf("%d", &select) != EOF)
    {
        return (select >= 0 && select <= 3) ? select : EOF;
    }
    else
    {
        return EOF;
    }
}
