//Define a class Rectangle with private attributes length and width. 
//Create a friend function named calculateArea that calculates the area of the rectangle.

#include <iostream>
using namespace std;

class Rectangle;

class Rectangle {
private:
    int length;
    int width;

public:
    Rectangle(int l, int w) : length(l), width(w) {}

    friend int calculateArea(const Rectangle & rect);
};

int calculateArea(const Rectangle& rect) {
    return rect.length * rect.width;
}

int main() {
    int length, width;
    cout << "Enter length: ";
    cin >> length;
    cout << "Enter width: ";
    cin >> width;

    Rectangle rect(length, width);
    int area = calculateArea(rect);

    cout << "Area of the rectangle: " << area << endl;

    return 0;
}
