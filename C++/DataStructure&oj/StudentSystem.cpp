#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

class Student
{
private:
    string sid;
    string name;
    string dep;
    int age;
    double score;
    istream& read(istream &is,Student &s)
    {
        cout<<"Enter studentID, name, department, age and score:"<<endl;
        is>>this->sid>>this->name>>this->dep>>this->age>>this->score;
        return is;
    }
public:
    Student()=default;
    Student(const string &sid,const string& name,const string &dep,int age,double score)
    {
        this->sid=sid;
        this->name=name;
        this->dep=dep;
        this->age=age;
        this->score=score;
    }
    Student(istream &is)
    {
        read(is,*this);
    }
    const string& getName() const
    {
        return this->name;
    }
    double getScore() const
    {
        return this->score;
    }
    bool operator<(const Student& that)const
    {
        if(this->score<that.score)
            return true;
        else
            return false;
    }
    bool operator>(const Student& that)const
    {
        if(this->score>that.score)
            return true;
        else
            return false;
    }
    void print() const
    {
        cout<<"StudentID: "<<sid<<",Name: "<<this->name<<",Department:  "<<dep<<"Age:  "<<age<<",  Score: "<<score<<endl;
    }
};

class StudentSystem
{
private:
    vector<Student> students;
    bool static desc_cmp(const Student &a,const Student &b)
    {
        return a>b;
    }
public:
    void add(const Student &a)
    {
        if(a.getName()=="")
            return;
        students.push_back(a);
    }

    void ascSort()
    {
        sort(students.begin(),students.end());
    }
    void descSort()
    {
        sort(students.begin(),students.end(),desc_cmp);
    }
    const vector<Student>& getStudents()
    {
        return students;
    }
};



int main()
{
    StudentSystem ss;
    ss.add(Student("001","Jackal","Foehn",1,800));
    ss.add(Student("002","Tarchia","Foehn",1,1800));
    ss.add(Student("003","Megalodon","Foehn",1,1800));
    ss.add(Student("004","Alanqa","Foehn",1,2400));
    ss.add(Student("005","Bison","Foehn",1,950));
    ss.add(Student("006","Buzzard","Foehn",1,1350));
    ss.add(Student("007","Pteranodon","Foehn",1,2000));
    ss.add(Student("008","Mastodon","Foehn",1,2400));
    ss.add(Student("009","Leviathan","Foehn",1,2800));
    ss.add(Student("010","Mobula","Foehn",1,1350));
    ss.add(Student("011","Raccoon","Foehn",1,900));
    ss.add(Student("012","Argentavis","Foehn",1,800));
    ss.add(Student("013","Gharial","Foehn",1,2000));

    while(cin)
    {
        ss.add(Student(cin));
    }
    for(auto &i:ss.getStudents())
        i.print();
    cout<<endl;
    ss.descSort();
    for(auto &i:ss.getStudents())
        i.print();
    return 0;
}
