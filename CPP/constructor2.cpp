#include <iostream>
using namespace std;

class Rectangle {
private:
    int rectLength;
    int rectWidth;

public:
    Rectangle(int length, int width) {
        rectLength = length;
        rectWidth = width;
    }

    int getArea() {
        return rectLength * rectWidth;
    }

    int getPerimeter() {
        return 2 * (rectLength + rectWidth);
    }
};

int main() {
    Rectangle rect(10, 5);
    cout << "Area: " << rect.getArea() << endl;
    cout << "Perimeter: " << rect.getPerimeter() << endl;
    return 0;
}
