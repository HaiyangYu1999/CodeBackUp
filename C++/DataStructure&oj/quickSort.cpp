#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

const int maxn=100000;
int a[maxn]={0};
int aux[maxn]={0};
void exch(int *a,int i,int j)
{
    int tmp=a[j];
    a[j]=a[i];
    a[i]=tmp;
}
int partition(int *a,int be,int en)
{
    int v=a[be];
    int i=be;
    int j=en+1;
    while(true)
    {
        while(a[++i]<v)
        {
            if(i==en)
                break;
        }
        while(a[--j]>v)
        {
            if(j==be)
                break;
        }
        if(i>=j)
            break;
        exch(a,i,j);
    }
    exch(a,be,j);
    return j;
}

void quickSort(int *a,int be,int en)
{
    if(be>=en)
        return;
    int j=partition(a,be,en);
    quickSort(a,be,j-1);
    quickSort(a,j+1,en);
}

int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=0;i<n;++i)
        {
            scanf("%d",&a[i]);
        }
        quickSort(a,0,n-1);
        for(int i=0;i<n;++i)
        {
            printf("%d\n",a[i]);
        }
    }
}
