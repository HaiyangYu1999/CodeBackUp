


//˳����еĲ���


#include<stdio.h>
#include<stdlib.h>
#define M 250000
typedef struct squeue
{
    int front;
    int rear;
    char data[M];
}squeue;

int IsEmpty(squeue*l)                                                        //���˳������Ƿ�Ϊ��
{
    return (l->rear==l->front);
}

int IsFull(squeue*l)                                                          //���˳������Ƿ���
{
    return (l->rear==l->front-1||(l->front==0&&l->rear==M-1));
}

char GetFront(squeue*l)                                                         //�����зǿ��򷵻ض���Ԫ��
{
    if(IsEmpty(l))  {printf("\nThe queue is empty!\n");exit(0);}
    else{return l->data[l->front];}
}

char GetRear(squeue*l)                                                         //�����зǿ��򷵻ض�βԪ��
{
    if(IsEmpty(l))  {printf("\nThe queue is empty!\n");exit(0);}
    else if(l->rear==0) return l->data[M-1];
    else return l->data[l->rear-1];
}


int length(squeue*l)                                      //���ض��е�Ԫ�ظ���
{
    if(l->rear-l->front>=0)
    {return (l->rear-l->front);}
    else return l->rear-l->front+M;
}

void Insert(char a,squeue*l)                                 //��Ԫ��a�����β
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

char Delete(squeue*l)                                                    //�Ӷ�����ɾ������Ԫ�ز�����ɾ����Ԫ��
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

void clearqueue(squeue*l)                                       //��ն���
{
    int i=0;
    for(i=0;i<M;i++)
    {
        l->data[i]=0;
    }
    l->front=0;
    l->rear=0;
}

void Print(squeue*l)                                           //���մӶ��׵���β��˳�����
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
    squeue*h=malloc(sizeof(squeue));                 //�����ն��У�front��ʾ���׵�λ�ã�rear��ʾ��β�ĺ�һ��λ�ã����rear��Ҫ�������鳤�ȶ�����λ��
    clearqueue(h);
    h->front=5;                                      //��Ԫ���Ѿ������У����������Ԫ�ؿ��Է���������ǰ�����������������ΪM-1
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

