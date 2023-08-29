#include <iostream>
using namespace std;
class Sample{
    public:
        int x;
};
int main(){
    Sample obj;
    obj.x = 100;
    cout << "x = " << obj.x;
    return 0;
}