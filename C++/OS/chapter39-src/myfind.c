#include<stdio.h>
#include<unistd.h>
#include<sys/stat.h>
#include<string.h>
#include<dirent.h>   //includes struct DIR and struct dirent
#include<stdlib.h>
#include<assert.h>

const static int M = 1024;

void printRecursively(char* root);
int isDir(struct stat *buf);

int main(int argc, char* argv[])
{
    if(argc==1)
    {
        fprintf(stderr,"too few arguments\n");
        exit(1);
    }
    else if(argc>2)
    {
        fprintf(stderr,"too few arguments\n");
        exit(1);
    }
    else
    {
        char path[M];
        strcpy(path,argv[1]);
        printRecursively(path);  
    }  
}

int isDir(struct stat *buf) 
{
    if((buf->st_mode & S_IFDIR) == S_IFDIR)
    {
        return 1;
    }
    else return 0;
}

void printRecursively(char* root)
{
    struct stat buf;
    int status = stat(root,&buf);
    if(status)
    {
        fprintf(stderr,"Bad Address!\n");
        exit(1);
    }

    if(isDir(&buf))
    {
        if(root[strlen(root)-1]!='/')
        {
            strcat(root,"/");
        }
        printf("%s\n",root);

        //open the dir
        DIR* dp=opendir(root);
        assert(dp);

        struct dirent* d;
        while((d = readdir(dp)) != NULL)
        {
            if(!strcmp(d->d_name,".")||!strcmp(d->d_name,".."))
            {
                continue;
            }
            char newroot[M];
            strcpy(newroot,root);
            strcat(newroot,d->d_name);
            printRecursively(newroot);
        }
    }
    else
    {
        printf("%s\n",root);
    }
}