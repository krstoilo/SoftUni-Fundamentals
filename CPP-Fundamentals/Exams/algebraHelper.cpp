#include <iostream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

double calculateResult(string& expression) {

    double result = 0;
    istringstream ssExp(expression);
    int first;
    char operation;
    int second;

    ssExp >> first;
    ssExp >> operation;
    ssExp >> second;

    if (operation == '+') {
        result = first + second;
    }
    else if (operation == '*') {
        result = first * second;
    }
    else if (operation == '-') {
        result = first - second;
    }
    else if (operation == '/') {
        if (second == 0) {
            cout << "Error!";
            return 1;
        }
        result = first / second;
    }

    else if (operation == '%') {
        if (second == 0) {
            cout << "Error!";
            return 1;
        }
        result = first % second;
    }

    return result;
}

int main()
{
    int n;
    cin >> n;
    cin.ignore();
    multimap<double, string, greater<double>> expressions;

    for (int i = 0; i < n; i++) {
        string expression;
        getline(cin, expression);
        double result = calculateResult(expression);
        expressions.insert(pair<double, string>(result, expression));
    }

    for (auto element : expressions) {
        cout << element.second << endl;
    }

    return 0;
}

