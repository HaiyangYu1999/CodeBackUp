#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>

int main(int argc,char* argv[],char* envp[])
{
    if(!fork())
    {
        const char* path="/bin/ls";
        char* args[4];
        args[0]="This is execl()";
        args[1]="./";
        args[2]="-l";
        args[3]=NULL;
        if(execl(path,"","./","-l",NULL))
        {
            fprintf(stderr,"exec failed");
        }
    }
    else if(!fork())
    {
        const char* path="/bin/ls";
        char* args[4];
        args[0]="This is execv()";
        args[1]="./";
        args[2]="-l";
        args[3]=NULL;
        if(execv(path,args))
        {
            fprintf(stderr,"exec failed");
        }
    }
    else if(!fork())
    {
        const char* path="ls";
        char* args[4];
        args[0]="This is execlp()";
        args[1]="./";
        args[2]="-l";
        args[3]=NULL;
        if(execlp(path,"","./","-l",NULL))
        {
            fprintf(stderr,"exec failed");
        }
    }
    else if(!fork())
    {
        const char* path="ls";
        char* args[4];
        args[0]="This is execvp()";
        args[1]="./";
        args[2]="-l";
        args[3]=NULL;
        if(execvp(path,args))
        {
            fprintf(stderr,"exec failed");
        }
    }
    else if(!fork())
    {
        const char* path="/bin/ps";
        char* args[4];
        args[0]="This is execle()";
        args[1]=NULL;
        args[2]=NULL;
        args[3]=NULL;
        if(execle(path,args[0],NULL,envp))
        {
            fprintf(stderr,"exec failed");
        }
    }
    else if(!fork())
    {
        const char* path="ps";
        char* args[4];
        args[0]="This is execvpe()";
        args[1]=NULL;
        args[2]=NULL;
        args[3]=NULL;
        if(execvpe(path,args,envp))
        {
            fprintf(stderr,"exec failed");
        }
    }
    while(wait(NULL)!=-1)
    {
        ;
    }
    
    
}