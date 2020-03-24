



#include<stdio.h>
#include<math.h>
#include<stdlib.h>
typedef struct poly
{
    double coe;
    int exp;
    struct poly* next;
}poly;

void Print(poly*l)
{
    poly*p=l->next;
    int k=0;
    while(p)
    {
        if(p->coe==1)
        {
            if(p->exp==0)
                printf("1"),k++;
            else if(p->exp==1)
                printf("x"),k++;
            else
                printf("x^%d",p->exp),k++;
        }
        else if(p->coe==-1)
        {
            if(p->exp==0)
                printf("-1"),k++;
            else if(p->exp==1)
                printf("-x"),k++;
            else
                printf("-x^%d",p->exp),k++;
        }
        else if(p->coe==0);
        else
        {
            if(p->exp==0)
                printf("%g",p->coe),k++;
            else if(p->exp==1)
                printf("%g*x",p->coe),k++;
            else
                printf("%g*x^%d",p->coe,p->exp),k++;
        }

        if(p->next&&(p->next->coe>0))
        {
            if(p!=l->next)printf("+"),k++;
            else if(p==l->next&&l->next->coe!=0)
                printf("+"),k++;
        }
        p=p->next;
    }
    if(k==0) printf("0");
    printf("\n");
}


int polylenth(poly*l)
{
    poly *p=l->next;
    int k=0;
    while(p)
    {
        k++;
        p=p->next;
    }
    return k;
}
void Up(poly*l)
{
    int c;double s;
    poly*p=l->next;
    int m=polylenth(l),i;
    for(i=0;i<m;i++)
    {
            while(p->next)
        {
            if(p->exp>p->next->exp)
                {
                    s=p->coe;
                    p->coe=p->next->coe;
                    p->next->coe=s;
                    c=p->exp;
                    p->exp=p->next->exp;
                    p->next->exp=c;
                    p=p->next;
                }
            else if(p->exp==p->next->exp)
            {
                p->coe=p->coe+p->next->coe;
                poly* t=p->next->next;
                free(p->next);
                p->next=t;
            }
            else p=p->next;

        }p=l->next;
    }


}

void Low(poly*l)
{
    int c;double s;
    poly*p=l->next;
    int m=polylenth(l),i;
    for(i=0;i<m;i++)
    {
            while(p->next)
        {
            if(p->exp<p->next->exp)
                {
                    s=p->coe;
                    p->coe=p->next->coe;
                    p->next->coe=s;
                    c=p->exp;
                    p->exp=p->next->exp;
                    p->next->exp=c;
                    p=p->next;
                }
            else if(p->exp==p->next->exp)
            {
                p->coe=p->coe+p->next->coe;
                poly* t=p->next->next;
                free(p->next);
                p->next=t;
            }
            else p=p->next;
        }
            p=l->next;
    }


}

poly* plus(poly*a,poly*b)
{
   poly*p=b->next;
   poly*s=a->next;
   while(p)
   {
       poly*d=malloc(sizeof(poly));
       d->coe=p->coe;
       d->exp=p->exp;
       d->next=s;
       a->next=d;
       s=a->next;
       p=p->next;
   }
   Low(a);
    return a;

}

poly* multi(poly* l,double a)
{
    poly*p=l->next;
    while(p)
    {
        p->coe=a*p->coe;
        p=p->next;
    }
    Low(l);
    return l;
}
poly* multix(poly* l,double a,int b)
{
    poly*p=l->next;
    while(p)
    {
        p->coe=a*(p->coe);
        p->exp=(p->exp)+b;
        p=p->next;
    }
    Low(l);
    return l;
}
double value(poly*l,double a)
{
    poly*p=l->next;
    double sum=0.0;
    while(p)
    {
        sum=sum+(p->coe)*(pow(a,p->exp));
        p=p->next;
    }
    return sum;
}

poly* multiple(poly*a,poly*b)
{
    int k=0;
    poly*p1=a->next;
    poly*p2=b->next;
    poly*s=malloc(sizeof(poly));
    poly*s1=malloc(sizeof(poly));
    s->next=s1;
    s1->coe=0;
    s1->exp=1;
    s1->next=NULL;
        for(;p1;p1=p1->next,k++)
        {
            poly* t=malloc(sizeof(poly));
            poly* q=t;
            while(p2)
            {
                poly*t1=malloc(sizeof(poly));
                t1->coe=p2->coe;
                t1->exp=p2->exp;
                q->next=t1;
                q=t1;
                p2=p2->next;

            }
            p2=b->next;
            q->next=NULL;
            s=plus(multix(t,p1->coe,p1->exp),s);

        }

    return s;
}

int main()
{
    poly*h=malloc(sizeof(poly));
    poly*q=h;
    int i;
    for(i=5;i>=0;i--)
    {
        poly*p=malloc(sizeof(poly));
        p->coe=i;
        p->exp=i;
        q->next=p;
        q=p;
    }
    q->next=NULL;
    printf("h="),Print(h);


     poly*g=malloc(sizeof(poly));
    q=g;
    for(i=8;i>=5;i--)
    {
        poly*p=malloc(sizeof(poly));
        p->coe=1;
        p->exp=i;
        q->next=p;
        q=p;
    }
    q->next=NULL;
    printf("g="),Print(g);
    printf("h*g="),Print(multiple(g,h));
}
