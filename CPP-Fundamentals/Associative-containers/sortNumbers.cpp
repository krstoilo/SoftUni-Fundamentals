#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <sstream>

using namespace std;

int main()
{
    string numbersLine;
    getline(cin, numbersLine);
    int number;
    set<int> numbers;
    istringstream ssNums(numbersLine);
    while (ssNums >> number) {
        numbers.insert(number);
    }

    for (auto n : numbers) {
        if (numbers.find(n) == numbers.begin()) {
            cout << n;
        }
        else {
            cout << " <= " << n;
        }
    }
    return 0;
}


