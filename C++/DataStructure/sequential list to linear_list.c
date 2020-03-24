

//用动态数组实现线性表


#include<stdio.h>
#include<stdlib.h>
#define M 100

int length(char* l)                        //求顺序表的长度
{
    char*p=l;
    int k=0;
    while(*p)
    {
        k++;
        p++;
    }
    return k;
}

int Find(char a,char*l)                     //查找元素a第一次出现的位置，若a不存在则返回-1
{
    int k=0;
    char*p=l;
    while((*p)&&((*p)!=a))
    {
        k++;
        p++;
    }

     if(k!=length(l)) return k;
     else return -1;
}
void Insert(char x,char a,char*l)                     //在元素a后插入元素x，若元素a不存在则不进行操作并显示Error！
{
   char*p=l;
   int d=length(l);
   p=(char*)realloc(p,(d+1)*(sizeof(char)));
   int k=Find(a,p),i;
    int s=length(p);
    if(k==-1) printf("Error! '%c' is not found!\n",a);
    else {for(i=s;i>k;i--)
    {
        *(p+i)=*(p+i-1);
    }
    *(p+k+1)=x;}

}

void Delete(char a,char*l)                              //删除第一次出现的a的后面的元素
{
    char*p=l;
    int k=Find(a,p);
    int s=length(p),i;
    for(i=k+1;i<s;i++)
    {
        *(l+i)=*(l+i+1);
    }
}

int main()
{
    char*a=(char*)malloc(M*sizeof(char));                  //创建动态数组，等价于char a[M];
    int i;
    for(i=0;i<M;i++)
    {
       a[i]=0;
   }
    for(i=0;i<26;i++)
    {
       a[i]='a'+i;
   }
   a=(char*)realloc(a,2*(M)*sizeof(char));                 //将动态数组的大小扩大为2M，而原有的数据不变
   for(i=0;a[i];i++)
        printf("%c",a[i]);
}
