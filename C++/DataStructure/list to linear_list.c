

//用链表实现线性表

#include<stdio.h>
#include<stdlib.h>
typedef struct list
{
    int data;
    struct list* next;
}list;

list* Append(list*a,list*b)                     //在链表a后加链表b
{
    list*p=a->next;
    while(p->next)
    {
        p=p->next;
    }
    p->next=b->next;
    return a;
}


int IsEmpty (list *l)                        //检查链表是否为空
{
    return l->next==NULL;
}

list* Find(int a,list* l)                     //查找元素a并返回a在链表里的指针，若a不存在则显示Error！（如果a多次出现则只返回第一次出现的位置的指针）
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
int FindPosition(int a,list* l)                     //查找元素a并返回a在链表里的位置，若a不存在则返回-1（如果a多次出现则只返回第一次出现的位置）
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
int IsLast(int a,list*l)                     //检查元素a是否为链表中的最后一个元素（如果a出现多次则只检查第一次出现的a）
{
    list*p=Find(a,l);
    return p->next==0;
}
list* FindPrevious(int a,list *l)  //输入某个元素a，返回某个元素的前驱元素的指针，如果a不存在则返回NULL（如果a多次出现则只返回第一次出现的前驱元素的指针）
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
void Insert(int x,int a,list*l)                    //在元素a后插入元素x（如果a多次出现则只在第一次出现时后插入x）
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

void Delete(int a,list*l)                          //删除元素a,如果没有元素a则不进行任何操作（如果a多次出现则只删除第一次出现的a）
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
int ListLenth(list*l)                               //计算链表的的元素个数
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

void DeleteSame(list*l)                              //删除链表中的相同的元素
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



void MakeEmpty(list* l)                                //删除链表
{
    list *s,*p=l->next;
    while(p)
    {
        l->next=p->next;
        free(p);
        p=l->next;
    }
}

void Up (list*l)                                 //将链表升序排列
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

void Low (list*l)                                 //将链表降序排列
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

list* Union(list*a,list*b)                              //求两个链表的并集
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

list* Intersect(list*a,list*b)                              //求两个链表的交集
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
    struct list* h=malloc(sizeof(list));                       //创建新链表,h是头指针
    struct list* r=h;
    for(i=0;i<251;i++)
    {
        struct list*p=malloc(sizeof(list));
        p->data=i;
        r->next=p;
        r=p;
    }
    r->next=NULL;

    struct list* g=malloc(sizeof(list));                         //创建新链表,g是头指针
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
