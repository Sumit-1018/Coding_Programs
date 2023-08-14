#include <iostream>
using namespace std;
int main() {
    int arr[5];
    cout << "Enter numbers:" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Enter number " << i + 1 << ": ";
        cin >> arr[i];
    }
    cout << "The numbers are: ";
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += arr[i];
    }
    cout << "Sum of the numbers: " << sum << endl;
    
    return 0;
}
