#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


struct Node
{
    double num=0;
    char op='\0';
    bool flag;
};
map<char,int> mp;

void initial_mp(map<char,int> &mp)
{
    mp['+']=0;
    mp['-']=0;
    mp['*']=1;
    mp['/']=1;
}

int main()
{
    initial_mp(mp);
    while(true)
    {
        char a[205];
        gets(a);
        string s=a;
        if(s=="0")
            break;
        for(string::iterator it=s.begin();it!=s.end();++it)
        {
            if(*it==' ')
                s.erase(it);
        }
        Node tmp=Node();
        queue<Node> q=queue<Node>();
        stack<Node> stk=stack<Node>();
        for(int i=0;i<s.length();)
        {
            if(s[i]>='0'&&s[i]<='9')
            {
                tmp.flag=true;
                tmp.num=0;
                while(i<s.length()&&s[i]>='0'&&s[i]<='9')
                {
                    tmp.num=tmp.num*10+(s[i]-'0');
                    ++i;
                }
                q.push(tmp);

            }
            else
            {
                tmp.flag=false;
                tmp.op=s[i];
                while(!stk.empty()&&mp[s[i]]<=mp[stk.top().op])
                {
                    q.push(stk.top());
                    stk.pop();
                }
                stk.push(tmp);
                ++i;
            }
        }
        while(!stk.empty())
        {
            q.push(stk.top());
            stk.pop();
        }
        Node cur;
        Node temp;
        double temp1,temp2;
        while(!q.empty())
        {
            cur=q.front();
            q.pop();
            if(cur.flag==true)
            {
                stk.push(cur);
            }
            else
            {
                temp2=stk.top().num;
                stk.pop();
                temp1=stk.top().num;
                stk.pop();
                temp.flag=true;
                if(cur.op=='+')
                    temp.num=temp1+temp2;
                else if(cur.op=='-')
                    temp.num=temp1-temp2;
                else if(cur.op=='*')
                    temp.num=temp1*temp2;
                else
                    temp.num=temp1/temp2;
                stk.push(temp);
            }
        }
        printf("%.2f\n",stk.top().num);
    }


}
