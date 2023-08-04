#include<iostream>
using namespace std;
int main(){
    int a;
    cout<<"Enter the marks of the student: ";
    cin>>a;

    if (a<0 || a>100)
    {
        cout<< "Invalid"<<endl;
    }
    else if (a>=90 && a<=100)
    {
        cout<<"A grade"<<endl;
    }
    else if (a>=80 && a<=90)
    {
        cout<<"B grade"<<endl;
    }
    else if (a>=70 && a<=80)
    {
        cout<<"C grade"<<endl;
    }
    else if (a>=60 && a<=70)
    {
        cout<<"D grade"<<endl;
    }
    else if (a>=50 && a<=60)
    {
        cout<<"E grade"<<endl;
    }
    else
    {
    	cout<<"Fail"<<endl;
	}
	}