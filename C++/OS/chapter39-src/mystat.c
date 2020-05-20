#include<unistd.h>
#include<stdio.h>
#include<sys/stat.h>   //stat() required
#include<assert.h>
#include<string.h>
#include<time.h>
#include"mode.h"


int main(int argc, char* argv[])
{
    if(argc==1)
    {
        fprintf(stderr,"stat: missing operand.\n");
    }
    else
    {
        for(int j = 1;j!=argc;++j)
        {
            const char* path=argv[j];
            struct stat buf;
            int status=stat(path,&buf);
            assert(!status);
            char filetype[256]="";
            char protection[256]="";
            char mod[256]="";
            getMod(&buf, protection,mod, filetype);
            printf("File: %s\n",path);
            printf("Size: %ld\t",buf.st_size);
            printf("Blocks: %ld\t",buf.st_blocks);
            printf("IO Blocks: %ld\t",buf.st_blksize);
            printf("File Type: %s\n",filetype);
            printf("Device: %ld\t",buf.st_dev);
            printf("inode: %ld\t",buf.st_ino);
            printf("Links: %ld\n",buf.st_nlink);
            printf("Access: (%s/%s)\t",mod,protection);
            printf("Uid: %d\t",buf.st_uid);
            printf("Gid: %d\n",buf.st_gid);
            struct timespec as=buf.st_atim;
            struct timespec ms=buf.st_mtim;
            struct timespec cs=buf.st_ctim;
            printf("Accessed: %s",ctime(&as.tv_sec));
            printf("Modified: %s",ctime(&ms.tv_sec));
            printf("Changed: %s\n",ctime(&cs.tv_sec));
        }
        
    }
    
}


