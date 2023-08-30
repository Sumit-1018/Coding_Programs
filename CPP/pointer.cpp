#include<iostream>
#include<iomanip>
using namespace std;
struct Time{
    int h;
    int m;
    int s;
};

void calcDifference(const Time&t1,const Time&t2,Time&result){
    result.h=t1.h-t2.h;
    result.m=t1.m-t2.m;
    result.s=t1.s-t2.s;
};

int main(){
    string x;
    Time t1,t2,dif;   
    getline(cin,x);
    sscanf(x.c_str(),"%d:%d:%d",&t1.h,&t1.m,&t1.s);
    getline(cin,x);
    sscanf(x.c_str(),"%d:%d:%d",&t2.h,&t2.m,&t2.s);
    calcDifference(t1,t2,dif);
    cout<<setw(2)<<setfill('0')<<dif.h<<":"<<setw(2)<<dif.m<<":"<<setw(2)<<dif.s;
    return 0;
}