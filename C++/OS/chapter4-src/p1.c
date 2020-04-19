#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char* argv[])
{
    int x=100;              //variable x
    printf("This is parent process pid:%d\n",(int)getpid());
    int rc=fork();
    if(rc<0)
    {
        fprintf(stdout,"fork failed\n");
        exit(1);
    }
    else if(rc==0)       //child process
    {
        fprintf(stdout,"This is child process pid:%d, x:%d\n",(int)getpid(),x);
        x=99;  //change x in child process
        fprintf(stdout,"x=%d\n",x);
    }
    else           //parent process
    {
        fprintf(stdout,"This is parent process pid:%d, x:%d\n",(int)getpid(),x);
        x=101;
        fprintf(stdout,"x=%d\n",x);
    }
    printf("In pid %d, x=%d\n",(int)getpid(),x);
}