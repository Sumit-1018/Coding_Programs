#include <iostream>
using namespace std;

int main() {
    int a;
    cout << "Enter the marks of the student: ";
    cin >> a;

    if (a < 0 || a > 100) {
        cout << "Invalid" << endl;
    } else {
        int grade = a / 10;

        switch (grade) {
            case 10:
            case 9:
                cout << "A grade" << endl;
                break;
            case 8:
                cout << "B grade" << endl;
                break;
            case 7:
                cout << "C grade" << endl;
                break;
            case 6:
                cout << "D grade" << endl;
                break;
            case 5:
                cout << "E grade" << endl;
                break;
            default:
                cout << "Fail" << endl;
        }
    }

    return 0;
}
