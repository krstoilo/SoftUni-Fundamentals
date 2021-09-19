#include <iostream>
#include <cmath>

using namespace std;



class Coordinates {
    class Points{
    public:
        int coordinateX;
        int coordinateY;
        void setPoint(int x, int y) {
            this->coordinateX = x;
            this->coordinateY = y;
        }
    };

    Points point1;
    Points point2;
    double distance;

public:
    void getInfo() {
        int num1, num2;
        cin >> num1 >> num2;
        point1.setPoint(num1, num2);
        int num3, num4;
        cin >> num3 >> num4;
        point2.setPoint(num3, num4);

    }
    void calculateDistance() {
        distance = sqrt(pow((point2.coordinateX - point1.coordinateX), 2) + pow((point2.coordinateY - point1.coordinateY), 2));
        cout.setf(ios::fixed, ios::floatfield);
        cout.precision(3);
        cout << distance << endl;
    }
};

int main()
{
    Coordinates system;
    system.getInfo();
    system.calculateDistance();

    return 0;
}