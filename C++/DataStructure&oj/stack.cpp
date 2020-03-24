#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<process.h>
const int STACK_INIT_SIZE=100;
const int STACKINCREMENT=10;
typedef struct {
int *elem;
int top;
int stacksize;
int incrementsize;
 } SqStack;
 void InitStack_Sq(SqStack &S, int maxsize, int incresize)
 {
     S.elem= new int[maxsize];
     S.top=-1;
     S.stacksize=maxsize;
     S.incrementsize=incresize;
 }
 bool GetTOP_Sq(SqStack S)
 {
     if(S.top=-1)
        return false;
     else
        return true;
 }
 void incrementStacksize( SqStack &S)
 {
     int *a;
      a=new int[S.stacksize+S.incrementsize];
      for(int i=0;i<S.stacksize;i++)
          a[i]=S.elem[i];
          delete [] S.elem;
          S.elem=a;
          S.stacksize+=S.incrementsize;
 }
 void Push_Sq(SqStack &S, int e)
 {
     if(S.top=S.stacksize-1) incrementStacksize(S);
     S.elem[++S.top]=e;
 }
 bool Pop_Sq(SqStack &S, int &e)
 {
     if(S.top==-1) return false;
     e=S.elem[S.top--];
     return true;
 }
 void ShowStack(SqStack S)
 {
     for (int i=0;i<S.top;++i)
        printf("%d",S.elem[i]);
        printf("%d\n",S.elem[S.top]);
 }

 typedef struct LNode{
int data;
struct LNode *next;
}LNode, *LinkStack;
void InitStack_L(LinkStack &s,int k,int A[])
{
    s=NULL;
    for (int i=0;i<k;++i)
    {
        LNode *p=new LNode;
        p->data=A[i];
        p->next=s;
        s=p;
}
}
void Push_L(LinkStack &s, int e)
{
    LNode *p=new LNode;
    p->data=e;
    p->next=s;
    s=p;
}
int main()
{
    SqStack S;
    InitStack_Sq(S,STACK_INIT_SIZE,STACKINCREMENT);
    printf("������ջԪ�أ�\n");
    for (int i=1;i<=5;i++)
    {
        scanf("%d",&S.elem[i-1]);
    }
    S.stacksize=5;
    S.top=4;
    printf("�㴴����ջΪ��\n");
    ShowStack(S);
    Push_Sq(S,2);
    printf("����֮���ջΪ��\n");
    ShowStack(S);
    int e;
    Pop_Sq(S,e);
    printf("ɾ��֮���ջΪ\n");
    ShowStack(S);
    printf("stacktest\n",e);
    return 0;
}
