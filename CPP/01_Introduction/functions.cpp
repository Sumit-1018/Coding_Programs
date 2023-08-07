#include <iostream>
using namespace std;
void name(string name,int marks){
    cout<<"My name is "<<name<<" and i got "<< marks<<" marks in my 12th grade"<<endl;
}

int main() {
    string studentName;
    int studentMarks;

    cout << "Enter your name: ";
    cin >> studentName;

    cout << "Enter your marks in 12th grade: ";
    cin >> studentMarks;

    name(studentName, studentMarks);

    return 0;
}