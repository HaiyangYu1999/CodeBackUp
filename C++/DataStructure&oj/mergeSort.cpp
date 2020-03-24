#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

const int maxn=100000;
int a[maxn]={0};
int aux[maxn]={0};

void Merge(int *a,int be,int mid,int en);
void mergeSort(int *a,int be,int en)
{
    if(be>=en)
        return;
    int mid=be+(en-be)/2;
    mergeSort(a,be,mid);
    mergeSort(a,mid+1,en);
    Merge(a,be,mid,en);
}

void Merge(int *a,int be,int mid,int en)
{
    for(int i=be;i<en+1;++i)
        aux[i]=a[i];
    int i=be;
    int j=mid+1;
    int k=be;
    while(k<en+1)
    {
        if(i>mid)
        {
            a[k++]=aux[j++];
        }
        else if(j>en)
        {
            a[k++]=aux[i++];
        }
        else if(aux[i]<aux[j])
        {
            a[k++]=aux[i++];
        }
        else
        {
            a[k++]=aux[j++];
        }
    }
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        int m;
        scanf("%d",&m);
        for(int i=0;i<m;++i)
        {
            scanf("%d",&a[i]);
        }
        mergeSort(a,0,m-1);
        for(int i=0;i<m;++i)
        {
            printf("%d\n",a[i]);
        }
    }
}
