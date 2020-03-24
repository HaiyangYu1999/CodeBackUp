


//顺序队列的操作


#include<stdio.h>
#include<stdlib.h>
#define M 250000
typedef struct squeue
{
    int front;
    int rear;
    char data[M];
}squeue;

int IsEmpty(squeue*l)                                                        //检查顺序队列是否为空
{
    return (l->rear==l->front);
}

int IsFull(squeue*l)                                                          //检查顺序队列是否满
{
    return (l->rear==l->front-1||(l->front==0&&l->rear==M-1));
}

char GetFront(squeue*l)                                                         //若队列非空则返回队首元素
{
    if(IsEmpty(l))  {printf("\nThe queue is empty!\n");exit(0);}
    else{return l->data[l->front];}
}

char GetRear(squeue*l)                                                         //若队列非空则返回队尾元素
{
    if(IsEmpty(l))  {printf("\nThe queue is empty!\n");exit(0);}
    else if(l->rear==0) return l->data[M-1];
    else return l->data[l->rear-1];
}


int length(squeue*l)                                      //返回队列的元素个数
{
    if(l->rear-l->front>=0)
    {return (l->rear-l->front);}
    else return l->rear-l->front+M;
}

void Insert(char a,squeue*l)                                 //将元素a加入队尾
{
    if(!length(l))
    {
        if(l->rear!=M-1)
        {
            l->data[l->front]=a;
            l->rear+=1;
        }
        else
        {
            l->data[l->front]=a;
            l->rear=0;
        }
    }
    else
        {
            if(l->rear!=M-1)
            {
                l->data[l->rear]=a;
                l->rear+=1;
            }
            else
                {
                    l->data[l->rear]=a;
                    l->rear=0;
                }

        }

}

char Delete(squeue*l)                                                    //从队列中删除队首元素并返回删除的元素
{
    if(IsEmpty(l)){ printf("\nNo pop! The stack is empty!\n");exit(0);}
    else if(l->front==M-1)
    {
        char a=l->data[l->front];
        l->data[l->front]=0;
        l->front=0;
        return a;
    }
    else
    {
        char b=l->data[l->front];
        l->data[l->front]=0;
        l->front+=1;
        return b;
    }
}

void clearqueue(squeue*l)                                       //清空队列
{
    int i=0;
    for(i=0;i<M;i++)
    {
        l->data[i]=0;
    }
    l->front=0;
    l->rear=0;
}

void Print(squeue*l)                                           //按照从队首到队尾的顺序输出
{
    int i;
    if(l->front<=l->rear)
        for(i=l->front;i<l->rear;i++)
    {
        printf(" %c ",l->data[i]);
    }
    else
    {
        for(i=l->front;i<M;i++)
    {
        printf(" %c ",l->data[i]);
    }
    for(i=0;i<l->rear;i++)
    {
        printf(" %c ",l->data[i]);
    }
    }
}

int main()
{
    squeue*h=malloc(sizeof(squeue));                 //创建空队列，front表示队首的位置，rear表示队尾的后一个位置，如果rear将要超过数组长度而队首位置
    clearqueue(h);
    h->front=5;                                      //有元素已经出队列，则新入队列元素可以放置在数组前部，整个数组的容量为M-1
    h->rear=5;
    Insert('a',h);
    Insert('a'+1,h);
    Insert('a'+2,h);
    Insert('a'+3,h);
    Insert('a'+4,h);
    Insert('a'+5,h);
    Insert('a'+6,h);
    Insert('a'+7,h);
    Insert('a'+8,h);
    Print(h);

}

