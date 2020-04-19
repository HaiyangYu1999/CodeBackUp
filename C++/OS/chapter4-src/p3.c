#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main(int argc,char* argv[],char* envp[])
{
    int rc=fork();
    if(rc<0)
    {
        fprintf(stderr,"fork failed!\n");
        exit(1);
    }
    else if (rc==0)
    {
        printf("hello, This is p3.c\n");
    }
    else
    {
        sleep(1); //use sleep() instead of wait()
        printf("Goodbye!\n");
    }
    
}