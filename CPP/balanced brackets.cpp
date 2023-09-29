#include <iostream>
#include <stack>
using namespace std;
bool isValid(string s) {
    stack<char> st;
    for (char ch=0; ch<s.size(); ch++) {
        if (ch == '(' || ch == '[' || ch == '{') {
            st.push(ch);
        } else if (ch == ')' || ch == ']' || ch == '}') {
            if (st.empty()) {
                return false; 
            }
            char top = st.top();
            st.pop();
            if ((ch == ')' && top != '(') ||
                (ch == ']' && top != '[') ||
                (ch == '}' && top != '{')) {
                return false; 
            }
        }
    }
    return st.empty(); 
}
int main() {
    string input;
    cout << "Enter the sequence: ";
    cin >> input;
    if (isValid(input)) {
        cout << "isvalid" << endl;
    } else {
        cout << "Invalid" << endl;
    }

    return 0;
}
