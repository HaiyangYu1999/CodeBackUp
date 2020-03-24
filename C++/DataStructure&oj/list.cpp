#include<iostream>
#include<string>
#include<sstream>
using namespace std;

template<typename T> class ArrayList
{
private:
    T *a;
    int length;
    int N;
    void reSize(int newsize)
    {
        T *tmp=new T[newsize];
        N=newsize;
        for(int i=0;i<length;++i)
        {
            tmp[i]=a[i];
        }
        delete[] a;
        a=tmp;
    }
public:
    ArrayList()
    {
        a=new T[1];
        length=0;
        N=1;
    }
    explicit ArrayList(int capacity)
    {
        a=new T[capacity];
        length=0;
        N=2*capacity;
    }
    ArrayList(const ArrayList<T> &that)
    {
        length=that.length;
        N=that.N;
        a=new T[N];
        for(int i=0;i<length;++i)
        {
            a[i]=that.a[i];
        }
    }
    ~ArrayList()
    {
        delete[] a;
    }
    ArrayList<T>& operator=(const ArrayList<T>& that)
    {
        if(a!=nullptr)
            delete[] a;
        a=new T[that.N];
        N=that.N;
        length=that.length;
        for(int i=0;i<length;++i)
        {
            a[i]=that.a[i];
        }
        return *this;
    }
    ArrayList<T> operator+(const ArrayList<T>& that)
    {
        auto a=*this;
        for(int i=0;i<that.len();++i)
        {
            a.add_back(that.a[i]);
        }
        return a;
    }
    ArrayList<T> reverse()
    {
        ArrayList<T> tmp(N);
        for(int i=length-1;i!=-1;--i)
        {
            tmp.add_back(a[i]);
        }
        return tmp;
    }
    int len() const
    {
        return length;
    }
    void display()
    {
        for(int i=0;i<length;++i)
        {
            cout<<a[i]<<"  ";
        }
        cout<<endl;
    }
    void add(const T &s,int index)
    {
        if(index<-1||index>length-1)
        {
            cout<<"Invalid Index! In ArrayList::add()"<<endl;
            exit(1);
        }
        if(length==N)
            reSize(2*N);
        for(int i=length-1;i>index;--i)
        {
            a[i+1]=a[i];
        }
        a[index+1]=s;
        ++length;
    }
    void add_front(const T &s)
    {
        add(s,-1);
    }
    void add_back(const T &s)
    {
        add(s,length-1);
    }
    T remove(int index)
    {
        if(length==0)
        {
            cout<<"Empty List! In ArrayList::remove()"<<endl;
            exit(1);
        }
        if(index<-1||index>length-2)
        {
            cout<<"Invalid Index! In ArrayList::remove()"<<endl;
            exit(1);
        }
        T tmp=a[index+1];
        for(int i=index+1;i<length-1;++i)
        {
            a[i]=a[i+1];
        }
        --length;
        if(length<N/4)
        {
            reSize(N/2);
        }
        return tmp;
    }
    T remove_front()
    {
        return remove(-1);
    }
    T remove_back()
    {
        return remove(length-2);
    }
    T& At(int index)
    {
        if(index<0||index>length-1)
        {
            cout<<"Invalid Index! In ArrayList::At()"<<endl;
            exit(1);
        }
        return a[index];
    }

};

template<typename T> class LinkedList
{
private:
    T value;
    LinkedList<T> *next;
    int length;

    LinkedList<T>* add(LinkedList<T>* node,const T &s,int index)
    {
        if(index==-1)
        {
            LinkedList<T> *tmp=node->next;
            LinkedList<T> *inser=new LinkedList<T>;
            inser->value=s;
            node->next=inser;
            inser->next=tmp;
            ++length;
            return node;
        }
        else
        {
            return add(node->next,s,index-1);
        }

    }
    T remove(LinkedList<T> *node,int index)
    {
        if(index==-1)
        {
            LinkedList<T> *tmp=node->next;
            node->next=tmp->next;
            T tmpr=tmp->value;
            --length;
            tmp->next=nullptr;
            delete tmp;
            return tmpr;
        }
        else
            return remove(node->next,index-1);
    }
    T& At(LinkedList<T>* node,int index)
    {
        if(index=-1)
            return node->value;
        else
            return At(node->next,index-1);
    }
public:
    LinkedList()
    {
        next=nullptr;
        length=0;
    }
    LinkedList(const LinkedList<T> &that)
    {
        int n=that.length;
        next=nullptr;
        length=0;
        for(auto p=that.next;p!=nullptr;p=p->next)
        {
            (*this).add_back(p->value);
        }
    }
    ~LinkedList()
    {
        if(next)
            delete next;
    }
    LinkedList<T>& operator=(const LinkedList<T> &that)
    {
        delete this->next;
        this->next=nullptr;
        this->length=0;
        for(auto p=that.next;p!=nullptr;p=p->next)
        {
            (*this).add_back(p->value);
        }
        return *this;
    }
    LinkedList<T> operator+(const LinkedList<T> &that)
    {
        auto a=*this;
        LinkedList<T>* p=that.next;
        while(p!=nullptr)
        {
            a.add_back(p->value);
            p=p->next;
        }
        return a;
    }
    friend ostream& operator<<(ostream &out,const LinkedList<T> &lis)
    {
        for(auto p=lis.next;p!=nullptr;p=p->next)
        {
            out<<p->value;
            if(p->next)
                out<<"  ";
        }
        out<<endl;
        return out;
    }
    friend istream& operator>>(istream &in,LinkedList<T> &lis)
    {
        LinkedList<T> tmp=LinkedList<T>();
        T s;
        while(in>>s)
        {
            tmp.add_back(s);
            if(in.get()=='\n')
                break;
        }
        lis=tmp;
        return in;
    }
    int len() const
    {
        return length;
    }
    void display()
    {
        int i=0;
        for(auto p=this->next;p!=nullptr;p=p->next)
        {
            cout<<p->value<<"  ";
        }
        cout<<endl;
    }
    void add(const T &s,int index)
    {
        if(index<-1||index>length-1)
        {
            cout<<"Invalid Index! In LinkedList::add()"<<endl;
            exit(1);
        }
        add(this,s,index);
    }
    void add_front(const T &s)
    {
        add(s,-1);
    }
    void add_back(const T &s)
    {
        add(s,length-1);
    }
    T remove(int index)
    {
        if(length==0)
        {
            cout<<"Empty List! In LinkedList::remove()"<<endl;
            exit(1);
        }
        if(index<-1||index>length-2)
        {
            cout<<"Invalid Index! In LinkedList::remove()"<<endl;
            exit(1);
        }
        return remove(this,index);
    }
    T remove_front()
    {
        return remove(-1);
    }
    T remove_back()
    {
        return remove(length-2);
    }
    T& At(int index)
    {
        if(index<0||index>length-1)
        {
            cout<<"Invalid Index! In LinkedList::At()"<<endl;
            exit(1);
        }
        int i=0;
        for(auto p=this->next;p!=nullptr;p=p->next)
        {
            if(i==index)
            {
                return p->value;
            }
            ++i;
        }
    }
    LinkedList<T> reverse()
    {
        LinkedList<T> s;
        for(auto p=this->next;p!=nullptr;p=p->next)
        {
            s.add_front(p->value);
        }
        return s;
    }
};


template<typename T> class DoubleLinkedList
{
private:
    T value;
    DoubleLinkedList<T> *next;
    DoubleLinkedList<T> *prev;
    int length;

    DoubleLinkedList<T>* add(DoubleLinkedList<T>* node,const T &s,int index)
    {
        if(index==-1)
        {
            DoubleLinkedList<T> *tmp=node->next;
            DoubleLinkedList<T> *inser=new DoubleLinkedList<T>;
            inser->value=s;
            node->next=inser;
            inser->next=tmp;
            if(tmp)
                tmp->prev=inser;
            inser->prev=node;
            ++length;
            return node;
        }
        else
        {
            return add(node->next,s,index-1);
        }
    }

    T remove(DoubleLinkedList<T> *node,int index)
    {
        if(index==-1)
        {
            DoubleLinkedList<T> *tmp=node->next;
            node->next=tmp->next;
            if(tmp->next)
                tmp->next->prev=node;
            T tmpr=tmp->value;
            --length;
            tmp->next=nullptr;
            tmp->prev=nullptr;
            delete tmp;
            return tmpr;
        }
        else
            return remove(node->next,index-1);
    }
public:
    DoubleLinkedList()
    {
        next=nullptr;
        prev=nullptr;
        length=0;
    }
    DoubleLinkedList(const DoubleLinkedList<T> &that)
    {
        int n=that.length;
        next=nullptr;
        prev=nullptr;
        length=0;
        for(auto p=that.next;p!=nullptr;p=p->next)
        {
            (*this).add_back(p->value);
        }
    }
    ~DoubleLinkedList()
    {
        if(next)
            delete next;
    }
    DoubleLinkedList<T>& operator=(const DoubleLinkedList<T> &that)
    {
        delete this->next;
        this->next=nullptr;
        this->length=0;
        for(auto p=that.next;p!=nullptr;p=p->next)
        {
            (*this).add_back(p->value);
        }
        return *this;
    }
    void add(const T &s,int index)
    {
        if(index<-1||index>length-1)
        {
            cout<<"Invalid Index! In LinkedList::add()"<<endl;
            exit(1);
        }
        add(this,s,index);
    }
    void add_front(const T &s)
    {
        add(s,-1);
    }
    void add_back(const T &s)
    {
        add(s,length-1);
    }
    T remove(int index)
    {
        if(length==0)
        {
            cout<<"Empty List! In LinkedList::remove()"<<endl;
            exit(1);
        }
        if(index<-1||index>length-2)
        {
            cout<<"Invalid Index! In LinkedList::remove()"<<endl;
            exit(1);
        }
        return remove(this,index);
    }
    T remove_front()
    {
        return remove(-1);
    }
    T remove_back()
    {
        return remove(length-2);
    }
    void display()
    {
        int i=0;
        for(auto p=this->next;p!=nullptr;p=p->next)
        {
            cout<<p->value<<"  ";
        }
        cout<<endl;
    }
    T& At(int index)
    {
        if(index<0||index>length-1)
        {
            cout<<"Invalid Index! In LinkedList::At()"<<endl;
            exit(1);
        }
        int i=0;
        for(auto p=this->next;p!=nullptr;p=p->next)
        {
            if(i==index)
            {
                return p->value;
            }
            ++i;
        }
    }
};



int main()
{
    DoubleLinkedList<string> a;
    for(int i=0;i<6;++i)
    {
        ostringstream oss;
        oss<<"String"<<i;
        a.add_back(oss.str());
    }
    auto b=a;
    b.remove(1);
    b.At(1)+="sss";
    b.display();
}
