#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<fcntl.h>  //contains open()
#include<assert.h>
#include<string.h>
#include<stdlib.h>//contains malloc()
int main(int argc, char* argv[])
{
    int n;
    char* path=NULL;
    if(argc>3)
    {
        fprintf(stderr,"too many arguments\n");
        exit(1);
    }
    else if(argc==1)
    {
        fprintf(stderr,"too few arguments\n");
        exit(1);
    }
    else if(argc==2)
    {
        path=argv[1];
        n=10;
    }
    else if(argc==3)
    {
        if(argv[1][0]='-')
        {
            n=atoi(argv[1]+1);
            path=argv[2];
        }
        else if(argv[2][0]='-')
        {
            n=atoi(argv[2]+1);
            path=argv[1];
        }
        else 
        {
            fprintf(stderr,"you must assign -n option!\n");
            exit(1);
        }
    }
    
    if(n<=0)
    {
        fprintf(stderr,"-n option should be a positive integer!\n");
        exit(1);
    }
    int fd =open(path,O_RDONLY);
    if(fd==-1)
    {
        fprintf(stderr,"Bad File Address!\n");
        exit(1);
    }
    off_t i=lseek(fd,0,SEEK_END);   //i is file size. make cursor at the end
    assert(i!=-1);
    
    char* str=(char*)malloc(i*sizeof(char));
    size_t index=0;
    size_t readline=0;
    int tmp=1000;

    //read the last character
    off_t status=lseek(fd,-1,SEEK_CUR);
    assert(status!=-1);
    char buf[1];
    int readsize=read(fd,buf,1);
    if(buf[0]=='\n')
    {
        ++readline;
    }
    str[index++]=buf[0];
    while(readline<n)
    {   
        char buf[1];
        off_t i=lseek(fd,-2,SEEK_CUR);
        assert(i!=-1);
        if(i==0)
        {
            int readsize=read(fd,buf,1);
            if(buf[0]=='\n')
            {
                ++readline;
            }
            str[index++]=buf[0];
            break;
        }
        else
        {
            int readsize=read(fd,buf,1);
            if(buf[0]=='\n')
            {
                ++readline;
            }
            str[index++]=buf[0];
        }
        
    }
    if(readline==n)
    {
        --index;
    }
    str[index]='\0';
    

    long long len=strlen(str)-1;
    while(len!=-1)
    {
        printf("%c",str[len]);
        --len;
    }

    printf("\n");
    free(str);
}