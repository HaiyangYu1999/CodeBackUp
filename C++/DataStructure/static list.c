

//用静态链表实现线性表


#include<stdio.h>
#define M 250000
typedef struct slist
{
    char data;
    int cur;
}slist;


int length(slist*l)                               //静态链表的长度
{
    int i=l[M-1].cur,k=0;
    while(i)
    {
        k++;
        i=l[i].cur;
    }
    return k;
}

int Find(char a,slist*l)                          //查找第一次出现的元素a对应的下标，如果不存在则返回-1
{
    slist*p=l;
    int i;
    for(i=(l+M-1)->cur;(p+i)!=l&&p[i].data!=a;i=p[i].cur);
    if(i==0) return -1;
    else return i;

}

void Insert(char x,char a,slist*l)                   //在第一次出现的元素a后插入元素x
{
    int n=Find(a,l);
    if(n==-1) printf("\n%c is not found!\n",a);
    else if(length(l)==M-2) printf("\nThe static is full!\n");
    else
    {
        int p=(l+n)->cur;
        int o=l->cur;
        l->cur=(l+o)->cur;
        (l+o)->data=x;
        (l+o)->cur=p;
        (l+n)->cur=o;
    }
}

void Delete(char a,slist*l)                       //删除元素a后面的元素
{
    int c=Find(a,l);
    if(c==-1) printf("\n%c is not found!\n",a);
    else {int d=l[c].cur;
    int e=l[d].cur;
    l[c].cur=e;
    l[d].data=0;
    l[d].cur=l[0].cur;
    l[0].cur=d;}
}
int main()
{
    slist a[M];                                  //建立静态链表，第0个和第M-1个元素不存放数据，第0个的游标存放第一个空闲空间的位置，第M-1个的游标
    int i;                                       //存放第一个有数据的空间的位置，链表结束时最后一个元素的游标为0
    for(i=0;i<M;i++)
    {
        a[i].data=0;
        a[i].cur=i+1;
    }
    a[M-1].cur=1;
    a[M-2].cur=0;
    for(i=1;i<=26;i++)
    {
        a[i].data='a'+i-1;
        a[i].cur=i+1;
    }
    a[i-1].cur=0;
    a[0].cur=i;
    for(i=a[M-1].cur;a[i].data;i=a[i].cur)
    {
        printf("%c ",a[i].data);
    }
}
