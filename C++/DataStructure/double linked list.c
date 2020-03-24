

//˫������ĺ�������


#include<stdio.h>
#include<stdlib.h>
#define M 100
typedef struct dlist
{
    int data;
    struct dlist* prior;
    struct dlist* next;
}dlist;

int length(dlist*l)                                      //����˫������ĳ���
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

dlist*Find(int a,dlist*l)                                //����Ԫ��a�״γ��ֵĵ�ַ����a�������򷵻�NULL
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

dlist*NextElem(int a,dlist*l)                              //���ص�һ�γ��ֵ�a����һ��Ԫ�صĵ�ַ
{
    if(Find(a,l)->next==0){printf("\nNo element after %d!\n",a);exit(0);}
    else return Find(a,l)->next;
}

dlist*PriorElem(int a,dlist*l)                              //���ص�һ�γ��ֵ�a����һ��Ԫ�صĵ�ַ
{
    if(Find(a,l)->prior==l){printf("\nNo element before %d!\n",a);exit(0);}
    else return Find(a,l)->prior;
}

void Insert(int x,int a,dlist*l)                           //�ڵ�һ�γ��ֵ�Ԫ��a�������Ԫ��x
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

void Delete(int a,dlist*l)                                  //ɾ����һ�γ��ֵ�a
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
    dlist* h=malloc(sizeof(dlist));                         //����˫������h,h��ͷ��㣬h1�����һ��Ԫ�صĵ�ַ
    dlist*h1=h;dlist*p=h1;                                                //�����������
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
    p=h->next;                                                          //�����������
    while(p)
    {
        printf("%d ",p->data);
        p=p->next;
    }

    p=h1;                                                               //�����������
    while(p!=h)
    {
        printf("%d ",p->data);
        p=p->prior;
    }

}


