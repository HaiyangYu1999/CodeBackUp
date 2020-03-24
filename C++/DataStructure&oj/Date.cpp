#include<cstdio>
#include<cstring>
using namespace std;

bool isLeap(int n)
{
    return (n%4==0&&n%100!=0)||(n%400==0);
}

int main()
{
    int md[13][2]={0,0,31,31,28,29,31,31,30,30,31,31,30,30,31,31,31,31,30,30,31,31,30,30,31,31};
    int date1=0;
    int date2=0;
    while(scanf("%d%d",&date1,&date2)!=EOF)
    {
         if(date1>date2)
        {
            int tmp=date1;
            date1=date2;
            date2=tmp;
        }
        int year1=date1/10000;
        int year2=date2/10000;
        int month1=(date1-year1*10000)/100;
        int month2=(date2-year2*10000)/100;
        int day1=(date1-year1*10000-month1*100);
        int day2=(date2-year2*10000-month2*100);
        int interval=1;
        while(year1<year2||month1<month2||day1<day2)
        {
            ++interval;
            ++day1;
            if(day1>md[month1][isLeap(year1)])
            {
                ++month1;
                day1=1;
            }
            if(month1>12)
            {
                ++year1;
                month1=1;
            }
        }
        printf("%d\n",interval);
    }
}
