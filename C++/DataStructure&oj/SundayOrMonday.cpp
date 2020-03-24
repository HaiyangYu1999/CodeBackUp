#include<cstdio>
#include<cstring>
#include<string>
using namespace std;

int md[13][2]={0,0,31,31,28,29,31,31,30,30,31,31,30,30,31,31,31,31,30,30,31,31,30,30,31,31};

bool isLeap(int n)
{
    return ((n%4==0)&&(n%100!=0))||(n%400==0);
}

int  month2m(const char* a)
{
    string m=a;
    if(m=="January")
        return 1;
    if(m=="February")
        return 2;
    if(m=="March")
        return 3;
    if(m=="April")
        return 4;
    if(m=="May")
        return 5;
    if(m=="June")
        return 6;
    if(m=="July")
        return 7;
    if(m=="August")
        return 8;
    if(m=="September")
        return 9;
    if(m=="October")
        return 10;
    if(m=="November")
        return 11;
    if(m=="December")
        return 12;
    printf("Error in month2m()\n");
    exit(-1);

}

int dateCmp(int y1,int m1,int d1,int y2,int m2,int d2)
{
    if(y1>y2)
        return 1;
    else if(y1<y2)
        return -1;
    else
    {
        if(m1>m2)
            return 1;
        else if(m1<m2)
            return -1;
        else
        {
            if(d1>d2)
                return 1;
            else if(d1<d2)
                return -1;
            else{
                return 0;
            }
        }
    }
}

int dateMinus(int y1,int m1,int d1,int y2,int m2,int d2)
{
    int flag=dateCmp(y1,m1,d1,y2,m2,d2);
    int ybegin,mbegin,dbegin;
    int yend,mend,dend;
    int s=0;
    if(flag>=0)
    {
        ybegin=y2;
        mbegin=m2;
        dbegin=d2;
        yend=y1;
        mend=m1;
        dend=d1;
        while(ybegin!=yend||mbegin!=mend||dbegin!=dend)
        {
            ++s;
            ++dbegin;
            if(dbegin>md[mbegin][isLeap(ybegin)])
            {
                ++mbegin;
                dbegin=1;
            }
            if(mbegin>12)
            {
                ++ybegin;
                mbegin=1;
            }
        }
    }
    if(flag<0)
    {
        ybegin=y1;
        mbegin=m1;
        dbegin=d1;
        yend=y2;
        mend=m2;
        dend=d2;
        while(ybegin!=yend||mbegin!=mend||dbegin!=dend)
        {
            ++s;
            ++dbegin;
            if(dbegin>md[mbegin][isLeap(ybegin)])
            {
                ++mbegin;
                dbegin=1;
            }
            if(mbegin>12)
            {
                ++ybegin;
                mbegin=1;
            }
        }
        s=-s;
    }
    return s;
}

string d2day(int n)
{
    if(n==0)
        return "Sunday";
    if(n==1)
        return "Monday";
    if(n==2)
        return "Tuesday";
    if(n==3)
        return "Wednesday";
    if(n==4)
        return "Thursday";
    if(n==5)
        return "Friday";
    if(n==6)
        return "Saturday";
    printf("Error in d2day()\n");

}

int main()
{
    int y;
    int d;
    char month[100]={0};
    while(scanf("%d%s%d",&d,month,&y)!=EOF)
    {
        int m=month2m(month);
        int nowy=2019;
        int nowm=4;
        int nowd=14;
        int interv=dateMinus(y,m,d,nowy,nowm,nowd);
        interv=interv%7;
        if(interv<0)
            interv+=7;
        string res=d2day(interv);
        printf("%s\n",res.c_str());
    }

}
