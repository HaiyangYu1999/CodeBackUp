#include<cstdio>
#include<cstring>

int strLen(const char* a)
{
    int i=0;
    while(a[i]!=0)
        ++i;
    return i;
}

char* strCat(char* a,const char* b)
{
    int lena=strLen(a);
    int lenb=strLen(b);
    int k=lena;
    for(int i=0;i<lenb;++i)
    {
        a[k++]=b[i];
    }
    a[k]='\0';
    return a;
}

char uppercase(char a)
{
    if('a'<=a&&'z'>=a)
        a=a-32;
    return a;
}

bool isWord(char a)
{
    if(a>='A'&&a<='Z'||a>='a'&&a<='z')
        return true;
    return false;
}

int main()
{
    char a[1000];
    char b[1000]={0};
    while(gets(a))
    {
        char c=getchar();
        int k=0;
        for(int i=0;i<strlen(a);++i)
        {
            if(a[i]!=c)
                b[k++]=a[i];
        }
        b[k]='\0';
        printf("%s",b);
        printf("\n");
    }


}
