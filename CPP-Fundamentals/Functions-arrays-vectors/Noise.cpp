#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

vector <char> readInput()
{
    vector <char> array;
    char enteredSymbol;
    cin >> enteredSymbol;

    while (enteredSymbol != '.')
    {
        array.push_back(enteredSymbol);
        cin >> enteredSymbol;
    }

    return array;
}

string findNumber(const vector<char>& array)
{
    string numberInStr = "";

    for (int i = 0; i < array.size(); i++)
    {
        if (isdigit(array[i]))
        {
            numberInStr += array[i];
        }
    }

    return numberInStr;
}

int main()
{
    vector<char> array = readInput();

    string numberInStr = findNumber(array);

    int number = stoi(numberInStr);

    int result = sqrt(number);

    cout << result << endl;
    
    return 0;
}


