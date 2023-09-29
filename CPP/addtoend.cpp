#include <iostream>
#include <stack>

using namespace std;

// Function to add a new element to the end of a stack
void addToEnd(stack<int> &s, int newElement) {
    stack<int> tempStack;

    // Step 1: Reverse the original stack
    while (!s.empty()) {
        tempStack.push(s.top());
        s.pop();
    }

    // Step 2: Push the new element onto the tempStack
    tempStack.push(newElement);

    // Step 3: Reverse the tempStack and push elements back to the original stack
    while (!tempStack.empty()) {
        s.push(tempStack.top());
        tempStack.pop();
    }
}

int main() {
    stack<int> myStack;

    // Push elements into the stack
    myStack.push(1);
    myStack.push(2);
    myStack.push(3);

    cout << "Original Stack: ";
    stack<int> originalStack = myStack; // Create a copy
    while (!originalStack.empty()) {
        cout << originalStack.top() << " ";
        originalStack.pop();
    }
    cout << endl;

    // Add a new element to the end
    int newElement = 4;
    addToEnd(myStack, newElement);

    cout << "Stack after adding " << newElement << " to the end: ";
    while (!myStack.empty()) {
        cout << myStack.top() << " ";
        myStack.pop();
    }
    cout << endl;

    return 0;
}
