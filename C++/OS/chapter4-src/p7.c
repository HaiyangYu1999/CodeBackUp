#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>

int main(int argc,char* argv[])
{
    int rc=fork();
    if(rc<0)
    {
        fprintf(stderr,"fork failed\n");
        exit(1);
    }
    else if(rc==0)
    {
        printf(" before close stdout %d\n",getpid());  //This will not be printed if it does not have "\n"
                                                       //because the buffer will be disabled immediately.
        close(STDOUT_FILENO);
        printf("after close stdout %d\n",getpid());
    }
    else
    {
        wait(NULL);
        printf("This is parent process %d\n",getpid());
    }
    
}