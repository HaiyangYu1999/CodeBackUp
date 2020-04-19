#include<cstdio>

int main()
{
    long long a;
    long long b;
    int m;
    while(scanf("%d",&m)!=EOF,m!=0)
    {
        scanf("%lld %lld",&a,&b);
        unsigned long long sum=a+b;
        int z[100]={0};
        int siz=0;
        while(sum!=0)
        {
            z[siz++]=sum%m;
            sum=sum/m;
        }
        if(siz==0)
        {
            z[0]=0;
            siz=1;
        }
        for(int i=siz-1;i>=0;--i)
        {
            printf("%d",z[i]);
        }
        printf("\n");
    }
}
