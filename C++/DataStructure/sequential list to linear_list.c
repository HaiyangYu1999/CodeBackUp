

//�ö�̬����ʵ�����Ա�


#include<stdio.h>
#include<stdlib.h>
#define M 100

int length(char* l)                        //��˳���ĳ���
{
    char*p=l;
    int k=0;
    while(*p)
    {
        k++;
        p++;
    }
    return k;
}

int Find(char a,char*l)                     //����Ԫ��a��һ�γ��ֵ�λ�ã���a�������򷵻�-1
{
    int k=0;
    char*p=l;
    while((*p)&&((*p)!=a))
    {
        k++;
        p++;
    }

     if(k!=length(l)) return k;
     else return -1;
}
void Insert(char x,char a,char*l)                     //��Ԫ��a�����Ԫ��x����Ԫ��a�������򲻽��в�������ʾError��
{
   char*p=l;
   int d=length(l);
   p=(char*)realloc(p,(d+1)*(sizeof(char)));
   int k=Find(a,p),i;
    int s=length(p);
    if(k==-1) printf("Error! '%c' is not found!\n",a);
    else {for(i=s;i>k;i--)
    {
        *(p+i)=*(p+i-1);
    }
    *(p+k+1)=x;}

}

void Delete(char a,char*l)                              //ɾ����һ�γ��ֵ�a�ĺ����Ԫ��
{
    char*p=l;
    int k=Find(a,p);
    int s=length(p),i;
    for(i=k+1;i<s;i++)
    {
        *(l+i)=*(l+i+1);
    }
}

int main()
{
    char*a=(char*)malloc(M*sizeof(char));                  //������̬���飬�ȼ���char a[M];
    int i;
    for(i=0;i<M;i++)
    {
       a[i]=0;
   }
    for(i=0;i<26;i++)
    {
       a[i]='a'+i;
   }
   a=(char*)realloc(a,2*(M)*sizeof(char));                 //����̬����Ĵ�С����Ϊ2M����ԭ�е����ݲ���
   for(i=0;a[i];i++)
        printf("%c",a[i]);
}
