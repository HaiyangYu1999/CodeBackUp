#include<cstdio>
using namespace std;
const int QUEUE_INIT_SIZE=100;
const int QUEUEINCREMENT=10;

struct SqQueue{
int *elem;
int front;
int rear;
int queuesize;
int incrementsize; };

typedef struct LNode{
int data;
struct LNode *next;
} LNode,*LinkList;

typedef LinkList QueuePtr;
typedef struct {
QueuePtr front;
QueuePtr rear;} LinkQueue;
void InitQueue_L(LinkQueue &Q)
{
    Q.front=Q.rear=new LNode;
    Q.front->next=NULL;
}
void DestroyQueue_L(LinkQueue &Q)
{
    while(Q.front){
    Q.rear=Q.front->next;
    delete Q.front;
    Q.front=Q.rear;
    }
}
void EnQueue_L(LinkQueue &Q,int e)
{   LinkList p;
    p=new LNode;
    p->data=e; p->next=NULL;
    Q.rear->next=p;
    Q.rear=p;
}
bool DeQueue_L(LinkQueue &Q, int e)
{    LinkList p;
    if(Q.front==Q.rear) return false;
    p=Q.front->next;
    e=p->data;
    Q.front->next=p->next;
    if(Q.rear==p)Q.rear=Q.front;
    delete p;
    return true;
}
void showQueue_L(LinkQueue Q)
{   LNode *p;
    p=Q.front->next;
    while(p){
    printf("%d ",p->data);
    p=p->next; }
    printf("\n");
}
void InitQueue_Sq(SqQueue &Q, int maxsize=QUEUE_INIT_SIZE, int incresize=QUEUEINCREMENT)
{
    Q.elem=new int[maxsize+1];
    Q.queuesize=maxsize;
    Q.incrementsize= incresize;
    Q.front=Q.rear=0;
}
int QueueLength_Sq(SqQueue Q)
{
    return(Q.rear-Q.front+Q.queuesize)%Q.queuesize;
}
bool DeQueue_Sq(SqQueue &Q, int &e)
{
    if(Q.front==Q.rear)return false;
    e=Q.elem[Q.front];
    Q.front=(Q.front+1)%Q.queuesize;
    return true;
}
void EnQueue_Sq(SqQueue &Q,int e)
{
    Q.elem[Q.rear]=e;
    Q.rear=(Q.rear+1)%Q.queuesize;
}
void show_Sq(SqQueue &Q,int n)
{
    for(int i=0;i<n-1;i++)
        printf("%d ",Q.elem[(Q.front+i)%Q.queuesize]);
        printf("%d\n",Q.elem[Q.rear-1]);
}
int main()
{   int A[6];
    int k=6;
    for(int i=0;i<k;i++)
        A[i]=i*i;
        SqQueue Q;
    InitQueue_Sq(Q,QUEUE_INIT_SIZE,QUEUEINCREMENT);
    for (int i=0;i<k;i++)
        EnQueue_Sq(Q,A[i]);
   printf("queue£º\n");
   show_Sq(Q,k);
   int e;
   DeQueue_Sq(Q,e);
   printf("dequeue£º\n");
   show_Sq(Q,k-1);

}
