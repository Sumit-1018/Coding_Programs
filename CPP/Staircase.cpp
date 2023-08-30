#include <iostream>
using namespace std;

int waystoclimb(int n) {
    if(n<=1) return 1;
    return waystoclimb(n-1) + waystoclimb(n-2);
}

int main() {
    int n;
    cout<<"Enter the number of steps: ";
    cin>>n;
    cout<<"Number of distinct ways to climb a staircase of "<<n<<" steps: "<<waystoclimb(n)<<endl;
}
