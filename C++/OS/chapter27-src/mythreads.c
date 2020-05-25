#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>   //needed to enable -pthread   e.g.  $gcc -pthread FileName.c -o FileName
#include<assert.h>
#include<string.h>

typedef struct TestClass      //Use thread switch element in struct TestClass
{
    int first;
    int second;
    char status[10];
}TestClass;

void* cpy(void* pTestClass)           //get a copy of TestClass
{
    TestClass* p=(TestClass*)pTestClass;
    TestClass* newp=(TestClass*) malloc(sizeof(TestClass));
    newp->first=p->first;
    newp->second=p->second;
    strcpy(newp->status,"copy");
    return (void*)newp;
}

int main(int argc,char* argv[])
{
    TestClass test;
    test.first=1;
    test.second=2;
    strcpy(test.status,"origin");
    
    pthread_t p;
    int n1=pthread_create(&p,NULL,&cpy,(void*)&test);
    assert(!n1);   //if n1!=0, creating thread failed
    TestClass* result=NULL;

    //change the arguments in a function. If you use pthread_join(p,(void*)result), variable result will not be changed.
    //Like that void f(int a) never changes variable a, void f(int* a) does.
    int n2=pthread_join(p,(void**)&result);     
    assert(!n2);
    printf("%d %d %s\n",result->first,result->second,result->status);
}