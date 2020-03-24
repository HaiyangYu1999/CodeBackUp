

//������ʵ�����Ա�

#include<stdio.h>
#include<stdlib.h>
typedef struct list
{
    int data;
    struct list* next;
}list;

list* Append(list*a,list*b)                     //������a�������b
{
    list*p=a->next;
    while(p->next)
    {
        p=p->next;
    }
    p->next=b->next;
    return a;
}


int IsEmpty (list *l)                        //��������Ƿ�Ϊ��
{
    return l->next==NULL;
}

list* Find(int a,list* l)                     //����Ԫ��a������a���������ָ�룬��a����������ʾError�������a��γ�����ֻ���ص�һ�γ��ֵ�λ�õ�ָ�룩
{
    list*p=l->next;
    while(p&&p->data!=a)
    {
        p=p->next;
    }
    if(p!=NULL)return p;
    else
    {
        printf("\nError! %d is not found!\n",a);
        return NULL;
    }
}
int FindPosition(int a,list* l)                     //����Ԫ��a������a���������λ�ã���a�������򷵻�-1�����a��γ�����ֻ���ص�һ�γ��ֵ�λ�ã�
{
    list*p=l->next;
    int k=0;
    while(p&&p->data!=a)
    {
        p=p->next;
        k++;
    }
    if(p!=NULL)return k;
    else
    {
        return -1;
    }
}
int IsLast(int a,list*l)                     //���Ԫ��a�Ƿ�Ϊ�����е����һ��Ԫ�أ����a���ֶ����ֻ����һ�γ��ֵ�a��
{
    list*p=Find(a,l);
    return p->next==0;
}
list* FindPrevious(int a,list *l)  //����ĳ��Ԫ��a������ĳ��Ԫ�ص�ǰ��Ԫ�ص�ָ�룬���a�������򷵻�NULL�����a��γ�����ֻ���ص�һ�γ��ֵ�ǰ��Ԫ�ص�ָ�룩
{
    list* p=l;
    while(p->next->data!=a&&p->next->next)
    {p=p->next;}
    if(p->next->next)
    {
        return p;
    }
    else return NULL;
}
void Insert(int x,int a,list*l)                    //��Ԫ��a�����Ԫ��x�����a��γ�����ֻ�ڵ�һ�γ���ʱ�����x��
{
    list*p=Find(a,l);
    list*c=malloc(sizeof(list));
    c->data=x;
    if(!IsLast(a,l))
    {c->next=p->next;
    p->next=c;}
    else
    {
        c->next=NULL;
        p->next=c;
    }
}

void Delete(int a,list*l)                          //ɾ��Ԫ��a,���û��Ԫ��a�򲻽����κβ��������a��γ�����ֻɾ����һ�γ��ֵ�a��
{
    list*p=FindPrevious(a,l);
    if(p==NULL);
    else
    {
    list*c=p->next->next;
    free(p->next);
    p->next=c;
    }
}
int ListLenth(list*l)                               //��������ĵ�Ԫ�ظ���
{
    list*p=l->next;
    int k=0;
    while(p)
       {
         k++;
         p=p->next;
       }
        return k;
}

void DeleteSame(list*l)                              //ɾ�������е���ͬ��Ԫ��
{
    list*p=l->next;
    list*q=l->next;
    int k=0,i;
    while(p)
    {

        for(i=0;i<k;i++)
        {
            if(q->data==p->data)
            {
                Delete(q->data,l);
                k=k-1;
            }
        }
        k++;
        p=p->next;
    }
}



void MakeEmpty(list* l)                                //ɾ������
{
    list *s,*p=l->next;
    while(p)
    {
        l->next=p->next;
        free(p);
        p=l->next;
    }
}

void Up (list*l)                                 //��������������
{
    list*p=l->next;
    int i=ListLenth(l),k;
    for(k=0;k<i;k++)
    {

    while(p->next)
    {
        if(p->data>p->next->data)
        {
            int c=p->next->data;
            p->next->data=p->data;
            p->data=c;
        }p=p->next;
    }p=l->next;

    }
}

void Low (list*l)                                 //������������
{
    list*p=l->next;
    int i=ListLenth(l),k;
    for(k=0;k<i;k++)
    {

    while(p->next)
    {
        if(p->data>p->next->data)
        {
            int c=p->next->data;
            p->next->data=p->data;
            p->data=c;
        }p=p->next;
    }p=l->next;

    }
}

list* Union(list*a,list*b)                              //����������Ĳ���
{
    if(!IsEmpty(a))
    {
        DeleteSame(a);
        DeleteSame(b);
        list*p=b->next;
        while(p)
        {
            int b=FindPosition(p->data,a);
            if(b==-1)
            {
                Insert(p->data,a->next->data,a);
            }
            p=p->next;
        }
        Up(a);

        return a;
    }
    else
    {Up(b);return b;}
}

list* Intersect(list*a,list*b)                              //����������Ľ���
{
    if(!IsEmpty(a))
    {
        DeleteSame(a);
        DeleteSame(b);
        list*p=a->next;
        list*h=malloc(sizeof(list));
        list*s=h;
        while(p)
        {
            if(FindPosition(p->data,b)!=-1)
            {
                list *q=malloc(sizeof(list));
                q->data=p->data;
                s->next=q;
                s=q;
            }
            p=p->next;
        }
        s->next=NULL;
        return h;
    }
}

int main()
{
    int i;
    struct list* h=malloc(sizeof(list));                       //����������,h��ͷָ��
    struct list* r=h;
    for(i=0;i<251;i++)
    {
        struct list*p=malloc(sizeof(list));
        p->data=i;
        r->next=p;
        r=p;
    }
    r->next=NULL;

    struct list* g=malloc(sizeof(list));                         //����������,g��ͷָ��
    struct list* r1=g;
    for(i=0;i<251;i++)
    {
        struct list*p=malloc(sizeof(list));
        p->data=250+i;
        r1->next=p;
        r1=p;
    }
    r1->next=NULL;

    struct list* p=h->next;
    for(i=0;p;i++)
    {
        printf(" %d",p->data);
        p=p->next;
    }

}
