

//串的堆分配表示


#include<stdio.h>
#include<stdlib.h>
typedef struct String
{
    char * data;
    int len;
}String;

String* createstring(int m)                             //创建一个长为m的空串
{
    String*h=malloc(sizeof(String));
    char *s=malloc(m*sizeof(char));
    h->data=s;
    h->len=m;
    char*d=s;
    int i;
    for(i=0;i<m;i++)
        s[i]=0;
    return h;
}

void clearstring(String*a)                                 //清空串a
{
    int i=0;
    for(i=0;i<a->len;i++)
    {
        a->data[i]=0;
    }
    a->len=0;
}
int IsEmpty(String*a)                                      //检查串是否为空
{
    return a->len==0;
}
int Stringlen(String*a)                                    //返回串a的长度
{
    return a->len;
}
void Strcpy(String*a,String*b)                             //将串b复制到a
{
    clearstring(a);
        char*s=malloc((b->len)*sizeof(char));
        a->data=s;
        int i;
        for(i=0;i<30;i++)
            a->data[i]=b->data[i];
        a->len=b->len;
}
int StrCompare(String*a,String*b)                          //若a大返回1 b大返回-1 相等返回0
{
    if(a->len==0&&b->len==0)
        return 0;
    else if(a->len>0&&b->len==0)
        return 1;
    else if(a->len==0&&b->len>0)
        return -1;

    else {int min=a->len;
    if(a->len>b->len)
        min=b->len;
    int i;
    for(i=0;i<min;i++)
    {
        if(a->data[i]<b->data[i])
        {

            return -1;break;
        }
        else if(a->data[i]>b->data[i])
        {

            return 1;break;
        }
        else
        {

            if(i==a->len-1&&i<b->len-1)
            {

                return -1;break;
            }
            else if(i<a->len-1&&i==b->len-1)
            {

                return 1;break;
            }
            else if(i==a->len-1&&i==b->len-1)
            {

                return 0;break;
            }
        }

    }}

}

String* Concat(String*a,String*b)                                  //将串b接在串a后
{

    String*h=malloc(sizeof(String));
    h->len=a->len+b->len;
    char*dat=realloc(a->data,(a->len+b->len)*sizeof(char));
    h->data=dat;
    int i;
    for(i=0;i<a->len;i++)
        h->data[i]=a->data[i];
    for(i=a->len;i<b->len+a->len;i++)
    {
        h->data[i]=b->data[i-a->len];
    }
    return h;
}
String* SubString(int p,int l,String*a)                           //返回串a自第p个字符开始长为l的字串，若p大于串长则不做操作，若p后没有l个字符则返回
{                                                                 //p后所有的字符

    if(p<=a->len)
    {
        String*h=malloc(sizeof(String));
        if(l<=a->len-p+1)
        {char*dat=malloc(l*sizeof(char));
            h->data=dat;
            h->len=l;
            int i;
            for(i=0;i<l;i++)
            h->data[i]=a->data[p-1+i];
            return h;

        }
        else if(l>a->len-p+1)
        {char*dat=malloc((a->len-p+1)*sizeof(char));
            h->data=dat;
            h->len=(a->len-p+1);
            int i;
            for(i=0;i<(a->len-p+1);i++)
            h->data[i]=a->data[p-1+i];
            return h;

        }

    }
else
{
    printf("\n%d is out of size!\n",p);exit(0);
}
}

int Index(String*b,String*a)                             //查找串b在串a中第一次出现的位置，若不存在则返回-1
{
    if(a->len==0||b->len==0) {printf("\nString cannot be empty!\n");exit(0);}
    else if(a->len<b->len) return -1;
    else
    {
        int d=a->len-b->len,e=b->len,i,j;
        for(i=0;i<d+1;i++)
        {
            for(j=0;j<b->len;j++)
            {
                if(a->data[i+j]!=b->data[j])
                    break;
            }
            if(j==e) {break;}
        }
        if(i==d+1) return -1;
        else return i+1;
    }

}
void Insert(int p,String*a,String*b)                     //在串a第p个位置后插入串b
{
    if(p>a->len);
    else
    {
        a->data=realloc(a->data,(a->len+b->len)*sizeof(char));
        a->len=a->len+b->len;
        int i;
        for(i=a->len-1;i>p-1+b->len;i--)
            a->data[i]=a->data[i-b->len];
        for(i=p-1+b->len;i>p-1;i--)
            a->data[i]=b->data[i-p];
    }
}
void Delete(int p,int l,String*a)                         //在串a第p个位置后删除l个字符
{
    if(p>a->len);
    else if(p+l>=a->len)
    {
        int i=0;
        for(i=p;i>a->len;i++)
            a->data[i]=0;
        a->len=p;
    }
    else
    {
        int i;
        for(i=p;i<a->len-l;i++)
            a->data[i]=a->data[i+l];
        for(i=a->len-l;i<a->len;i++)
            a->data[i]=0;
        a->len-=l;
    }
}

void Replace(String* c,String* b,String*a)                              //用串c替代出现在串a中的全部字串b
{
    int i,j,k;
    for(i=0;i<a->len-b->len+1;i++)
    {
        for(j=0;j<b->len;j++)
        {
            if(a->data[i+j]!=b->data[j])
                break;

        }
        if(j==b->len)
        {
            Delete(i,b->len,a);
            Insert(i,a,c);
        }
    }
}

int* getnext(char*c,int size_c)                               //获得KMP算法中的next数组
{
    int l=size_c;
    int *b=malloc(l*sizeof(int));
    char*a=c;
    b[0]=-1;
    int i,j,k;
    for(j=1;j<l;j++)
    {
        for(k=j-1;k>0;k--)
        {
            for(i=0;i<k;i++)
            {if(a[i]!=a[j-k+i]) break;}
            if(i==k) break;
        }
        b[j]=k;
    }

    return b;
}

int KMP(String*b,String*a)                                       //寻找字串b在串a中第一次出现的位置，若不存在则返回-1
{
    if(a->len==0||b->len==0) {printf("\nString cannot be empty!\n");exit(0);}
    else if(a->len<b->len) return -1;
    else
    {
        int *next=getnext(b->data,b->len);
        int i=0,j=0,k;
        while(i<a->len&&j<b->len)
        {
            if(a->data[i]==b->data[j])
            {
                i++;
                j++;
            }
            else if(j==-1)
            {
                i++;
                j++;
            }
            else
            {
                j=next[j];
            }
        }
        if(j==b->len)
            return i-b->len+1;
        else return -1;
    }
}
int main()
{
    String*h=createstring(100);                                  //创建两个空串并赋值
    String*g=createstring(50);
    String*s=createstring(50);
    int i;
    for(i=0;i<5;i++)
        h->data[i]='a'+i-35;
    h->len=5;
    for(i=0;i<5;i++)
        s->data[i]='a'+i;
    s->len=5;
    for(i=0;i<39;i++)
        g->data[i]='0'+i;
    g->len=39;


    for(i=0;i<s->len;i++)
        printf("%c ",s->data[i]);
        printf("\n");

    for(i=0;i<h->len;i++)
        printf("%c ",h->data[i]);
        printf("\n");
    for(i=0;i<g->len;i++)
        printf("%c ",g->data[i]);
    printf("%d",KMP(h,g));

}




