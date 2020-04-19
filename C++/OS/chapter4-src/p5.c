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
        int fake_wc=wait(NULL);
        printf("wait()=%d\n",fake_wc);
        printf("do something in child process\n");
    }
    else
    {
        int wc=wait(NULL);
        printf("wait()=%d\n",wc);
        printf("await child process\n");
    }
    
}