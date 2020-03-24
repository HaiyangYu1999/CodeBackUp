#include <iostream>
#include<stack>
#include<string>
#include<cstring>
#include<stdio.h>
#include<stdlib.h>
#include"Zhan.h"
#include"z(1).h"
using namespace std;
void convertion(int N)
{
    SqStack S;
    InitStack_Sq(S, 100, 10);
    while(N)
    {
        Push_Sq(S,N%8);
        N=N/8;
    }
    while(GetTOP_Sq(S))
    {
        int e;
        Pop_Sq(S,e);
        cout<<e;
}
cout<<endl;
}
bool matching(string exp)
{
    stack<char> stk;
    stk.push(exp[0]);
    for(int i=1;i<exp.size();++i)
    {
        if(!stk.empty())
        {
            char tmp=stk.top();
        if(exp[i]==')'&&tmp=='(')
            stk.pop();
        else if(exp[i]==']'&&tmp=='[')
            stk.pop();
        else if(exp[i]=='}'&&tmp=='{')
            stk.pop();
        else
            stk.push(exp[i]);
        }
        else
        {
            stk.push(exp[i]);
        }
    }
    if(stk.empty())
    {
        return true;
    }

    return false;
}
void knapsack(int w[],int T, int n)
{
    SqStack S;
    InitStack_Sq(S, 100, 10);
    int k=0;
    int e;
    do
    {
        while (T>0&&k<n){
            if(T-w[k]>=0){
                Push_Sq(S,k);
                T-=w[k];}
        k++;}
           if(T==0) ShowStack(S);
           Pop_Sq(S,k);T+=w[k];
           k++;   }while (!StackEmpty(S)||k<n);
}
int value(int n,int x, int y)
{
    if(n==0) return(x+1);
    else switch(n){
        case 1:return x;
        case 2: return 0;
        case 3: return 1;
        default :return 2;
    }
}
int Ackerman(int n, int x, int y)
{
    sqStack S;
   InitStack_sq(S,100,10);
   Acker e;
   int u;
   e.nval=n; e.xval=x; e.yval=y; Push_sq(S,e);
   do {
        gettop(S ,e);
        while(e.nval!=0&&e.yval!=0)
            {
                e.yval--;
                Push_sq(S,e);
            }
            Pop_sq(S,e);
            u=value(e.nval,e.xval,e.yval);
            if(!Stackempty(S))
            {
                Pop_sq(S,e);
                e.nval--;
                e.yval=e.xval;
                e.xval=u;
                Push_sq(S,e);
            }
        }while (!Stackempty(S));
        return u;
}
int main()
{
    printf("十进制数:10,100,1000\n");
    printf("转变后的八进制数为：\n");
    convertion(10);
    convertion(100);
    convertion(1000);
    printf("\n");
    printf("括号序列：({}[]), ([](]), {[]()[}]\n");
    string s1="({}[])";
    string s2="([](])";
    string s3="{[]()[}]";
    if(matching(s1))
        printf("正确\n");
        else
        printf("错误\n");
    if(matching(s2))
        printf("正确\n");
        else
        printf("错误\n");
    if(matching(s3))
        printf("正确\n");
        else
        printf("错误\n");
    int n=6, T=10;
    int w[6]={1,8,4,3,5,2};
    printf("满足条件的解对应的编号为为：\n");
    knapsack(w,T,n);
    printf("A(3,1,1)=%d\n",Ackerman(3,1,1));
}
