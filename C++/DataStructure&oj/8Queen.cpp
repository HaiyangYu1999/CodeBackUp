#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
using namespace std;
vector<string> s;
int P[10]={0};
bool inQueue[10]={false};
int count=0;
void EightQueen(int index)
{
    if(index==9)
    {
        string a="";
        for(int i=1;i<9;++i)
        {
            char b=P[i]+'0';
            a+=b;
        }
        s.push_back(a);
        return;
    }
    else
    {
        for(int x=1;x<9;++x)
        {
            if(!inQueue[x])
            {
                int flag=0;
                for(int i=1;i<index;++i)
                {
                    if(abs(i-index)==abs(P[i]-x))
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                    continue;
                else
                {
                    P[index]=x;
                    inQueue[x]=true;
                    EightQueen(index+1);
                    inQueue[x]=false;
                }
            }
        }
    }
}


int main()
{
    EightQueen(8);
    for(auto &i:s)
        cout<<i<<endl;
}
