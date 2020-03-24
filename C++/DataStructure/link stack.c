

//��ջ�Ĳ���


#include<stdio.h>
#include<stdlib.h>
typedef struct Stack
{
    char data;
    struct Stack* next;
}Stack;

int IsEmpty(Stack*l)                           //�����ջ�Ƿ�Ϊ��
{
    Stack*p=l;
    return p->next==NULL;
}


char GetTop(Stack*l)                                            //��ջ�ǿ��򷵻�ջ��Ԫ��
{
    if(IsEmpty(l))  {printf("\nThe stack is empty!\n");exit(0);}
    else{return l->next->data;}
}

void clearstack(Stack*l)                                       //���ջl
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

int length(Stack*l)                                      //����ջ��Ԫ�ظ���
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

void push(char a,Stack*l)                                 //��Ԫ��aѹ��ջ
{
    Stack*p=malloc(sizeof(Stack));
    p->data=a;
    p->next=l->next;
    l->next=p;
}

char pop(Stack*l)                                            //��ջ�е���һ��Ԫ�ز����ص�����Ԫ��
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
    Stack*h=malloc(sizeof(Stack));                              //������ջ
    h->next=NULL;
    Stack*q=h->next;

    int i;                                                      //��ջѹ��Ԫ��
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








