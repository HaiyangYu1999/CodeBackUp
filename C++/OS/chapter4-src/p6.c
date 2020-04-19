#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>

int main(int argc,char* argv[])
{
    int rc=fork();
    int status=0;
    if(rc<0)
    {
        fprintf(stderr,"fork failed\n");
        exit(1);
    }
    else if(rc==0)
    {
        int fake_wc=waitpid(-1,&status,0);
        printf("wait()=%d\n",fake_wc);
        printf("do something in child process\n");
    }
    else
    {
        int wc=waitpid(rc,&status,0);
        printf("wait()=%d\n",wc);
        if(WIFEXITED(status))
        {
            printf("child process exit(%d)\n",(status));
        }
        printf("await child process\n");
    }
    
}