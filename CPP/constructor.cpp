#include <iostream>
using namespace std;

class Employee {
private:
    string empName;
    double empSalary;
    int empCode;

public:
    // Default constructor
    Employee() {
        empName = "";
        empSalary = 0.0;
        empCode = 0;
    }
 
    Employee(string name, double salary, int code) {
        empName = name;
        empSalary = salary;
        empCode = code;
    }

    void displayInfo() {
        cout << "Name: " << empName << endl;
        cout << "Salary: " << empSalary << endl;
        cout << "Employee Code: " << empCode << endl;
    }
};

int main() {
    // Using the parameterized constructor
    Employee emp1("John Doe", 50000, 12345);
    emp1.displayInfo();

    // Using the default constructor
    Employee emp2;
    emp2.displayInfo();

    return 0;
}
