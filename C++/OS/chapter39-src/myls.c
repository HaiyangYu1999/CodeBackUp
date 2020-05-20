#include<unistd.h>
#include<stdio.h>
#include<dirent.h>   //includes struct DIR and struct dirent
#include<string.h>
#include"mode.h"  //includes function void getMod(struct stat *buf, char* protection, char* mod, char* fileType);
#include<assert.h>
#include<time.h>

int main(int argc, char* argv[])
{
    //check whether arguments have "-l"
    //generate a new path list without options
    int isList=0;
    char* pathList[argc+1];
    int k=0;
    for(int j=1;j!=argc;++j)
    {
        if(!strcmp(argv[j],"-l"))
        {
            isList++;
        }
        else if(argv[j][0]=='-')
        {
            ;
        }
        else
        {
            pathList[k++]=argv[j];
        }
    }
    pathList[k]=NULL;

    
    if(!isList)
    {
        int j=0;
        while(pathList[j])
        {
            char* path=pathList[j++];
            printf("%s:\n",path);
            DIR* dp=opendir(path);
            assert(dp);
            struct dirent *d;
            while((d = readdir(dp)) != NULL)       //read the file orderly. 
            {
                printf("%s\t",d->d_name);
            }
            printf("\n");
            if(j!=k)
            {
                printf("\n");
            }
            closedir(dp);
        }
    }
    else
    {
        int j=0;
        while(pathList[j])
        {
            char* path=pathList[j++];
            printf("%s:\n",path);
            DIR* dp=opendir(path);
            assert(dp);
            struct dirent *d;
            while(d = readdir(dp))
            {
                if(!strcmp(d->d_name,".")||!strcmp(d->d_name,".."))   //exclude "../" and "./"
                {
                    continue;
                }
                char filepath[512]="";
                strcpy(filepath,path);
                if(filepath[strlen(filepath)-1]!='/')   //if a directory does not end with '/', add the '/'
                {
                    strcat(filepath,"/");
                }
                
                strcat(filepath,d->d_name);      //construct the file path
                struct stat buf;
                int status = stat(filepath,&buf);
                assert(!status);

                char protection[256]="";
                char filename[256]="";
                getMod(&buf,protection,NULL,filename);
                printf("%s ",protection);
                printf("%2ld ",buf.st_nlink);
                printf("%6ld  ",buf.st_size);
                struct timespec ms=buf.st_mtim;
                char* time=ctime(&ms.tv_sec);
                time[strlen(time)-1]='\0'; //cancel the \n
                printf("%s ",time);
                printf(" %s\n",d->d_name);
            }
            if(j!=k)
            {
                printf("\n");
            }
            closedir(dp);
        }
    }
}
