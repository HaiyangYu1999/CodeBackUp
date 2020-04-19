#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

int main(int argc,char* argv[])
{
    int fd[2];
    pipe(fd);
    int rc=fork();
    if(rc<0)
    {
        fprintf(stderr,"fork failed\n");
        exit(1);
    }
    else if(!rc)    //child process writes in the pipe
    {
        char* string="child process has written!";
        write(fd[1],string,strlen(string));
    }
    else           //parent process reads
    {
        char str[50];
        read(fd[0],str,sizeof(str));
        //printf("%s\n",str);
    }
    
}