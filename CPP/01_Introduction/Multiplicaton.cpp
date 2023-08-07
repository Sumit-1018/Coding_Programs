#include <iostream>
using namespace std;
int multiply(int num1, int num2){
    return num1 * num2;
}
int main() {
    int num1, num2;
    cout<<"Enter the first number: ";
    cin>>num1;
    
    cout<<"Enter the second number: ";
    cin>>num2;
    
    int result = multiply(num1, num2);
    
    cout<<"Product: "<<result<<endl;
    
    return 0;
}


