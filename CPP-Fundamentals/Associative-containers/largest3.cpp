#include <iostream>
#include <set>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    string inputLine;
    getline(cin, inputLine);
    set<double> setOfNum;
    double num;
    istringstream ssLine(inputLine);
    while (ssLine >> num) {
        setOfNum.insert(num);
    }

    if (setOfNum.size() < 3) {
        for (auto n:setOfNum){
            cout << n << " ";
        }
    }
    else {
        int count = 3;
        while (count > 0) {
            for (auto m : setOfNum) {
                cout << m << " ";
            }
            count--;
        }
    }
    return 0;
}

