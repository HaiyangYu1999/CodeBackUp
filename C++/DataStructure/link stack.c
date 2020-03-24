

//链栈的操作


#include<stdio.h>
#include<stdlib.h>
typedef struct Stack
{
    char data;
    struct Stack* next;
}Stack;

int IsEmpty(Stack*l)                           //检查链栈是否为空
{
    Stack*p=l;
    return p->next==NULL;
}


char GetTop(Stack*l)                                            //若栈非空则返回栈顶元素
{
    if(IsEmpty(l))  {printf("\nThe stack is empty!\n");exit(0);}
    else{return l->next->data;}
}

void clearstack(Stack*l)                                       //清空栈l
{
    while(l->next)
    {
        Stack*p=l;
        Stack*q=l->next;
        Stack*r=l->next->next;
        free(q);
        l->next=r;
    }

}

int length(Stack*l)                                      //返回栈的元素个数
{
    Stack*p=l->next;
    int k=0;
    while(p)
    {
        k++;
        p=p->next;
    }
    return k;
}

void push(char a,Stack*l)                                 //将元素a压入栈
{
    Stack*p=malloc(sizeof(Stack));
    p->data=a;
    p->next=l->next;
    l->next=p;
}

char pop(Stack*l)                                            //从栈中弹出一个元素并返回弹出的元素
{
    if(IsEmpty(l)){ printf("\nNo pop! The stack is empty!\n");exit(0);}
    else {char a=l->next->data;
    Stack*p=l->next;
    Stack*q=l->next->next;
    free(p);
    l->next=q;
    return a;}
}

int main()
{
    Stack*h=malloc(sizeof(Stack));                              //建立空栈
    h->next=NULL;
    Stack*q=h->next;

    int i;                                                      //给栈压入元素
    for(i=0;i<26;i++)
    {
        Stack*p=malloc(sizeof(Stack));
        p->data='a'+i;
        h->next=p;
        p->next=q;
        q=p;
    }

    for(q=h->next;q;q=q->next)
    printf("%c",q->data);




}








