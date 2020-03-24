#include<cstdio>

int content[25]={0};


int P(int n,int items_num,bool isBag[])
{
    if(n<0)
        return 0;
    else if(n==0)
        return 1;
    else
    {
        int sum=0;
        bool tmp[25]={false};
        for(int i=0;i<25;++i)
        {
            tmp[i]=isBag[i];
        }
        for(int i=0;i<items_num;++i)
        {
            if(!tmp[i])
            {
                tmp[i]=true;
                sum+=P(n-content[i],items_num,tmp);
            }
        }
        return sum;
    }
}

int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=0;i<n;++i)
        {
            scanf("%d",&content[i]);
        }
        bool inBag[25]={false};
        printf("%d\n",P(40,n,inBag));
    }
}
