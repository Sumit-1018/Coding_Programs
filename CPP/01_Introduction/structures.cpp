#include <iostream>
using namespace std;

struct Students {
    string name;
    int rollNo;
    float marks;
};

int main() {
    Students student1; 
    Students student2;

    student1.name = "Shreya"; 
    student1.marks = 82.5;
    
    student2.name = "Alan";
    student2.marks = 81.5;
    student2.rollNo = 22222;

    cout << student1.name << "'s marks: " << student1.marks << endl;
    cout << "Student 2's roll number: " << student2.rollNo << endl;

    return 0; 
}
