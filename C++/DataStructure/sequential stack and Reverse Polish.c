

//顺序栈的操作


#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct Stack
{
    char *data;
    int top;
}Stack;


Stack* createstack(int m)                                    //建立一个大小为m的空栈
{
    Stack*h=malloc(sizeof(Stack));
    char* dat=malloc(m*sizeof(char));
    int i;
    for(i=0;i<m;i++) dat[i]=0;
    h->data=dat;
    h->top=-1;
    return h;

}

int IsEmpty(Stack* l)                                      //检查栈是否为空
{
    if(l->top==-1)
        return 1;
    else return 0;
}

char GetTop(Stack*l)                                       //若栈非空则返回栈顶元素
{
    if(IsEmpty(l))
    {
        printf("\nNo top! The stack is empty!\n");
        exit(0);
    }
    else return l->data[l->top];
}

void clearstack(Stack*l)                                   //清空栈l
{
    for(;l->top!=-1;l->top--)
    {
        l->data[l->top]=0;
    }
}

int length(Stack*l)                                      //返回栈的元素个数
{
    return l->top+1;
}

void push(char a,Stack*l)                                 //将元素a压入栈
{
    l->data=realloc(l->data,(l->top+2)*sizeof(char));
    l->data[l->top+1]=a;
    l->top+=1;
}

char pop(Stack*l)                                            //从栈中弹出一个元素并返回弹出的元素
{
    if(IsEmpty(l)){ printf("\nNo pop! The stack is empty!\n");exit(0);}
    else {char a=l->data[l->top];
    l->data[l->top]=0;
    l->top-=1;
    return a;}
}

char* ReversePolish(char* a)                                   //用栈实现中缀表达式转化为后缀表达式
{
    int l=strlen(a);
    Stack*b=createstack(l);
    int i,j,k=0;
    char*c=malloc(l*sizeof(char));
    Stack*d=createstack(l);
    push(0,d);
    for(i=0;i<l;i++)
    {

        if((a[i]>='0'&&a[i]<='9')||(a[i]>='a'&&a[i]<='z')||(a[i]>='A'&&a[i]<='Z'))
        {
            push(a[i],b);
            c[k++]=pop(b);
        }
        else if((a[i]=='+'||a[i]=='-'))
        {
            int s=0;
            while(d->data[d->top]>=1&&d->data[d->top]!=-1)
                {pop(d);s++;}
            push(1,d);
            for(j=0;j<s;j++)
            {
                c[k++]=pop(b);
            }
            push(a[i],b);
        }
        else if(a[i]=='*'||a[i]=='/')
        {
            int s=0;
            while(d->data[d->top]>=2&&d->data[d->top]!=-1)
                {pop(d);s++;}
            push(2,d);
            for(j=0;j<s;j++)
            {
                c[k++]=pop(b);
            }
            push(a[i],b);
        }
        else if(a[i]=='(')
                   {
                        push(-1,d);
                        push(a[i],b);
                   }
        else if(a[i]==')')
        {
            int s=0;
            while(length(d)!=1&&d->data[d->top]!=-1)
                {pop(d);s++;}
                if(length(d)==1) {printf("Error!");exit(0);}
            pop(d);
            for(j=0;j<s;j++)
            {
                c[k++]=pop(b);
            }
            pop(b);
        }
        else if(a[i]==' ');
    }
    while(!IsEmpty(b))
     {
         if(b->data[b->top]!=')'&&b->data[b->top]!='(')
         c[k++]=pop(b);
         else if(b->data[b->top]='(')
         {
             printf("Error!");
             exit(0);
         }

     }
    c[k]='\0';
    return c;

}

int main()
{
    Stack* a=createstack(1000);                          //建立一个空栈,栈的指针为a
    int i;
    for(i=0;i<20;i++)
    {
        push('a'+i,a);
    }
    char *d="4+2*(x-a/5)";
    char*c=ReversePolish(d);

    for(i=0;c[i]!='\0';i++)
        printf("%c ",c[i]);
}
