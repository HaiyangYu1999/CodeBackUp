

//链队列的操作


#include<stdio.h>
#include<stdlib.h>
typedef struct qlist
{
    char data;
    struct qlist* next;
}qlist;

typedef struct head
{
    struct qlist* front;
    struct qlist* rear;
}head;

int IsEmpty(head*l)                                          //检查链队列是否为空
{
    return (l->front==NULL&&l->rear==NULL);
}

char GetFront(head*l)                                            //若队列非空则返回队首元素
{
    if(IsEmpty(l))  {printf("\nThe queue is empty!\n");exit(0);}
    else{return l->front->data;}
}

char GetRear(head*l)                                             //若队列非空则返回队尾元素
{
    if(IsEmpty(l))  {printf("\nThe stack is empty!\n");exit(0);}
    else{return l->rear->data;}
}

int length(head*l)                                      //返回队列的元素个数
{
    if(IsEmpty(l)) return 0;
    else
    {qlist*p=l->front;
    int k=0;
    while(p)
    {
        k++;
        p=p->next;
    }
    return k;}
}

void Insert(char a,head*l)                                 //将元素a加入队尾
{
    if(!length(l))
    {
        qlist*p=malloc(sizeof(qlist));
        p->data=a;
        p->next=NULL;
        l->front=p;
        l->rear=p;
    }
    else
        {
            qlist*p=malloc(sizeof(qlist));
            l->rear->next=p;
            p->data=a;
            p->next=NULL;
            l->rear=p;
        }

}

char Delete(head*l)                                                    //从队列中删除队首元素并返回删除的元素
{
    if(IsEmpty(l)){ printf("\nNo pop! The stack is empty!\n");exit(0);}
    else if(length(l)==1)
    {
        qlist*p=l->front;
        char a=p->data;
        free(p);
        l->front=NULL;
        l->rear=NULL;
        return a;
    }
    else
    {
        qlist*p=l->front;
        qlist*q=l->front->next;
        char b=p->data;
        free(p);
        l->front=q;
        return b;
    }
}

void clearqueue(head*l)                                       //清空队列
{
    while(l->front||l->rear)
    {
        Delete(l);
    }

}

int main()
{
    head*h=malloc(sizeof(head));                         //建立空队列h
    h->front=0;
    h->rear=0;
    Insert('a',h);
    Insert('a'+1,h);
    Insert('a'+2,h);
    Insert('a'+3,h);
    Insert('a'+4,h);
    Insert('a'+5,h);
    qlist*p=h->front;
    while(p)
        {
            printf("%c ",p->data);
            p=p->next;
        }
}


