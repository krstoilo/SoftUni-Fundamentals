#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

void insertNumber(vector<int>& numbers, string & num) {

    int number;
    istringstream ssNum(num);
    while (ssNum >> number) {
        numbers.push_back(number);
    }
}

void sumNumbers(vector<int> & numbers) {

    int number1, number2;
    int sum;
    int lenVec = numbers.size();
    number1 = numbers[lenVec - 1];
    number2 = numbers[lenVec - 2];
    sum = number1 + number2;
    numbers.erase(numbers.end()-1);
    numbers.erase(numbers.end()-1);
    numbers.push_back(sum);

}

void subtractNumbers(vector<int>& numbers) {

    int a, b;
    int result;
    int lenVec = numbers.size();
    a = numbers[lenVec - 1];
    b = numbers[lenVec - 2];
    result = a - b;
    numbers.erase(numbers.end() - 1);
    numbers.erase(numbers.end() - 1);
    numbers.push_back(result);
}

void concatNumbers(vector<int>& numbers) {

    string a, b;
    string result;
    int lenVec = numbers.size();
    a = to_string(numbers[lenVec - 1]);
    b = to_string(numbers[lenVec - 2]);
    result = b + a;
    numbers.erase(numbers.end() - 1);
    numbers.erase(numbers.end() - 1);
    numbers.push_back(stoi(result));

}

int main()
{
    string command;
    cin >> command;
    vector<int> numberArray;

    while (command != "end") {
        if (isdigit(command[0]) || command[0] == '-') {
            insertNumber(numberArray, command);
        }
        else if (command == "sum") {

            sumNumbers(numberArray);
        }
        else if (command == "subtract") {

            subtractNumbers(numberArray);
        }

        else if (command == "concat") {

            concatNumbers(numberArray);
        }
        else if (command == "discard") {

            numberArray.erase(numberArray.end() - 1);
        }
        
        cin >> command;

    }
   
    for (auto n : numberArray) {
        cout << n << endl;
    }

    return 0;
}

