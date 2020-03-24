

//双向链表的函数操作


#include<stdio.h>
#include<stdlib.h>
#define M 100
typedef struct dlist
{
    int data;
    struct dlist* prior;
    struct dlist* next;
}dlist;

int length(dlist*l)                                      //返回双向链表的长度
{
    dlist*p=l->next;
    int k=0;
    while(p)
    {
        k++;
        p=p->next;
    }
    return k;
}

dlist*Find(int a,dlist*l)                                //查找元素a首次出现的地址，若a不存在则返回NULL
{
    dlist*p=l->next;
    int k=0;
    while(p&&p->data!=a)
    {
        p=p->next;
        k++;
    }
    if(k==length(l)) {printf("\n%d is not found!\n",a);exit(0);}
    else return p;
}

dlist*NextElem(int a,dlist*l)                              //返回第一次出现的a的下一个元素的地址
{
    if(Find(a,l)->next==0){printf("\nNo element after %d!\n",a);exit(0);}
    else return Find(a,l)->next;
}

dlist*PriorElem(int a,dlist*l)                              //返回第一次出现的a的上一个元素的地址
{
    if(Find(a,l)->prior==l){printf("\nNo element before %d!\n",a);exit(0);}
    else return Find(a,l)->prior;
}

void Insert(int x,int a,dlist*l)                           //在第一次出现的元素a后面插入元素x
{
    dlist*p=Find(a,l);
    dlist*q=p->next;
    dlist*o=malloc(sizeof(dlist));
    o->data=x;
    o->prior=p;
    o->next=q;
    p->next=o;
    q->prior=o;
}

void Delete(int a,dlist*l)                                  //删除第一次出现的a
{
    dlist*p=Find(a,l);
    dlist*o=p->prior;
    dlist*q=p->next;
    free(p);
    o->next=q;
    q->prior=o;
}
int main()
{
    dlist* h=malloc(sizeof(dlist));                         //创建双向链表h,h是头结点，h1是最后一个元素的地址
    dlist*h1=h;dlist*p=h1;                                                //倒向输出链表
    while(p!=h)
    {
        printf("%d ",p->data);
        p=p->prior;
    }
    int i;
    for(i=0;i<76;i++)
    {
        dlist*p=malloc(sizeof(dlist));
        p->data=i;
        p->prior=h1;
        h1->next=p;
        h1=p;
    }
    h1->next=NULL;
    p=h->next;                                                          //正向输出链表
    while(p)
    {
        printf("%d ",p->data);
        p=p->next;
    }

    p=h1;                                                               //倒向输出链表
    while(p!=h)
    {
        printf("%d ",p->data);
        p=p->prior;
    }

}


