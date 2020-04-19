#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>

int main(int argc,char* argv[])
{
    int fd=open("./doc_p2.txt",O_CREAT|O_WRONLY|O_TRUNC);
    int rc=fork();
    if(rc<0)
    {
        fprintf(stderr,"fork failed\n");
    }
    else if(rc==0)
    {
        const char child_write[]="child write the file.";
        int size=sizeof(child_write)/sizeof(char);
        write(fd,child_write,size-1);
    }
    else
    {
        const char parent_write[]="PARENT WRITE THE FILE.";
        int size=sizeof(parent_write)/sizeof(char);
        write(fd,parent_write,size-1);
    }
    close(fd);
}