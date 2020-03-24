#include<iostream>
using namespace std;

int gcd(int a,int b)
{
    int c=a%b;
    return (c==0)?b:gcd(b,c);
}

int main()
{
    cout<<"Enter 2 numbers: "<<endl;
    int a,b;
    cin>>a>>b;
    int res=gcd(a,b);
    cout<<"gcd of "<<a<<" and "<<b<<" is "<<res<<endl;
    return 0;
}
