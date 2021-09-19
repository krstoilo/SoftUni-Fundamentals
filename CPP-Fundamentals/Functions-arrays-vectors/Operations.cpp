#include <iostream>

using namespace std; 

int performOperation(const int & leftOp,const int & rightOp, const char & operation)
{
    int result = INT16_MIN;

    if (operation == '+')
    {
        result = leftOp + rightOp;
    }

    else if (operation == '-')
    {
        result = leftOp - rightOp;
    }

    else if (operation == '*')
    {
        result = leftOp * rightOp;
    }

    else if (operation == '/')
    {
        if (rightOp == 0)
        {
            cout << "Can't divide by zero" << endl;
        }
        else
        {
            result = leftOp / rightOp;
        }
    }

    return result;
}

int main()
{

    int leftOp, rightOp;
    char operation;

    cin >> leftOp >> rightOp;
    cin >> operation;

    while (operation != '+' && operation != '-' && operation != '*' && operation != '/')
    {
        cout << "try again" << endl;
        cin >> operation;
    }

    int result = performOperation(leftOp, rightOp, operation);

    if (result != INT16_MIN)
    {
        cout << result;
    }

    return 0;
}
