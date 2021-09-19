#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

void readInput(vector<int>& numbers) {
    string line;
    getline(cin, line);
    int num;
    istringstream ssNums(line);
    while (ssNums >> num) {
        numbers.push_back(num);
    }
}

bool isSquare(int& num) {

    double sr;
    sr = sqrt(num);
    if (sr * sr == num) {
        return true;
    }
    else {
        return false;
    }
}

int main()
{
    vector<int> numbers;
    readInput(numbers);
    vector<int> squareNumbers;
    for (auto num : numbers) {
        if (isSquare(num)) {
            squareNumbers.push_back(num);
        }
    }

    sort(squareNumbers.begin(), squareNumbers.end(), greater<int>());

    for (auto n : squareNumbers) {
        cout << n << " ";
    }

    return 0;
}

