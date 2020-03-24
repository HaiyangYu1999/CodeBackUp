#include<iostream>
#include<cstdio>
#include<string>
#include<map>
using namespace std;

bool isword(char a)
{
    if((a>='a'&&a<='z')||(a>='A'&&a<='Z')||(a>='0'&&a<='9'))
        return true;
    return false;
}

string lowcase(string s)
{
    for(auto &i:s)
    {
        if(i>='A'&&i<='Z')
            i+=32;
    }
    return s;
}

int main()
{
    char a[1048580];
    while(gets(a))
    {
        map<string,int> mp;
        string s=a;
        string tmp="";
        for(string::iterator p=s.begin();p!=s.end();++p)
        {
            char a=*p;
            if(isword(a)&&s.end()-p!=1)
            {
                tmp+=a;
            }
            else if(isword(a)&&s.end()-p==1)
            {
                tmp+=a;
                if(tmp!="")
                {
                    tmp=lowcase(tmp);
                    if(mp.count(tmp))
                    {
                        mp[tmp]++;
                    }
                    else
                    {
                        mp[tmp]=1;
                    }
                    tmp="";
                }
            }
            else
            {
                if(tmp!="")
                {
                    tmp=lowcase(tmp);
                    if(mp.count(tmp))
                    {
                        mp[tmp]++;
                    }
                    else
                    {
                        mp[tmp]=1;
                    }
                    tmp="";
                }
            }
        }
        string res="";
        int cou=0;
        for(map<string,int>::iterator it=mp.begin();it!=mp.end();++it)
        {
            if(it->second>cou)
            {
                cou=it->second;
                res=it->first;
            }
        }
        cout<<res<<" "<<cou<<endl;
    }
}
