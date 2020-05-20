#include<unistd.h>
#include<sys/stat.h>   //stat() required
#include<string.h>
#include<stdio.h>
#include"mode.h"

void getMod(struct stat *buf, char* protection, char* mod, char* fileType)
{
    if(protection==NULL)
    {
        char p[256];
        protection=p;
    }
    if(mod==NULL)
    {
        char m[256];
        mod=m;
    }
    if(fileType==NULL)
    {
        char f[256];
        fileType=f;
    }
    if(buf==NULL)
    {
        fprintf(stderr,"struct stat* is invalid!\n");
    }
    mod[0]='0';
    mod[1]='0';
    mod[2]='0';
    mod[3]='0';
    mod[4]='\0';
    if((buf->st_mode & S_IFSOCK) == S_IFSOCK)
    {
        strcpy(fileType,"socket");
        protection[0]='-';
    }
    else if((buf->st_mode & S_IFLNK) == S_IFLNK)
    {
        strcpy(fileType,"symbol link");
        protection[0]='l';
    }
    else if((buf->st_mode & S_IFREG) == S_IFREG)
    {
        strcpy(fileType,"regular file");
        protection[0]='-';
    }
    else if((buf->st_mode & S_IFDIR) == S_IFDIR)
    {
        strcpy(fileType,"directory");
        protection[0]='d';
    }
    else if((buf->st_mode & S_IFBLK) == S_IFBLK)
    {
        strcpy(fileType,"block device");
        protection[0]='b';
    }
    else if((buf->st_mode & S_IFCHR) == S_IFCHR)
    {
        strcpy(fileType,"char device");
        protection[0]='c';
    }

    if((buf->st_mode & S_IRUSR) == S_IRUSR)
    {
        protection[1]='r';
        mod[1]+=4;
    }
    else protection[1]='-';
    if((buf->st_mode & S_IWUSR) == S_IWUSR)
    {
        protection[2]='w';
        mod[1]+=2;
    }
    else protection[2]='-';
    if((buf->st_mode & S_IXUSR) == S_IXUSR)
    {
        protection[3]='x';
        mod[1]+=1;
    }
    else protection[3]='-';
    if((buf->st_mode & S_IRGRP) == S_IRGRP)
    {
        protection[4]='r';
        mod[2]+=4;
    }
    else protection[4]='-';
    if((buf->st_mode & S_IWGRP) == S_IWGRP)
    {
        protection[5]='w';
        mod[2]+=2;
    }
    else protection[5]='-';
    if((buf->st_mode & S_IXGRP) == S_IXGRP)
    {
        protection[6]='x';
        mod[2]+=1;
    }
    else protection[6]='-';
    if((buf->st_mode & S_IROTH) == S_IROTH)
    {
        protection[7]='r';
        mod[3]+=4;
    }
    else protection[7]='-';
    if((buf->st_mode & S_IWOTH) == S_IWOTH)
    {
        protection[8]='w';
        mod[3]+=2;
    }
    else protection[8]='-';
    if((buf->st_mode & S_IXOTH) == S_IXOTH)
    {
        protection[9]='x';
        mod[3]+=1;
    }
    else protection[9]='-';
    protection[10]='\0';
}