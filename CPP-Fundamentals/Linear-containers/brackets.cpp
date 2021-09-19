#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool validBrackets (string brackets) {

    
    bool areValid = true;
    bool validLevels = true;
    stack<char> openBrackets;

    for (size_t i = 0; i < brackets.size(); i++) {

        if (brackets[i] == '{' || brackets[i] == '[' || brackets[i] == '(') {
            openBrackets.push(brackets[i]);
        }

        if ((brackets[i] == '(' && (brackets[i + 1] == '[' || brackets[i + 1] == '{')) || brackets[i] == '[' && brackets[i+1] == '{') {

            validLevels = false;
            break;
        }

        switch (brackets[i]) {
        case ')':
            if (openBrackets.top() == '(') {
                openBrackets.pop();
            }
            break;

        case ']':
            if (openBrackets.top() == '[') {
                openBrackets.pop();
            }
            break;

        case '}':
            if (openBrackets.top() == '{') {
                openBrackets.pop();
            }
            break;
        }

    }

    if (!openBrackets.empty() || !validLevels) {
        areValid = false;
    } 

    return areValid;
}

int main() {

    string brackets;
    cin >> brackets;

    bool validity = validBrackets(brackets);
    if (validity) {
        cout << "valid" << endl;
    }
    else {
        cout << "invalid" << endl;
    }
   
    return 0;
}