#include <iostream>
#include <ctime>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

vector<char> arrayGenerator()
{
    vector<char> array;
    char randomSymbol = '!';

    srand(time(0));

    while (randomSymbol != '.')
    {
        randomSymbol = rand() % 96 + 33;
        array.push_back(randomSymbol);

        if (array.size() >= 20)
        {
            array.push_back('.');
            break;
        }
        
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

    bool presentDigit = false;
    vector<char> array;

    while (!presentDigit)
    {
        array = arrayGenerator();

        for (auto i : array)
        {
            if (isdigit(i))
            {
                presentDigit = true;
            }
        }

        if (!presentDigit) {
            array.clear();
        }

        else
        {
            for (auto k : array)
            {
                cout << k << " ";
            }
        }

        cout << endl;
    }

    string numberInStr = findNumber(array);

     int number = stoi(numberInStr);

     ///cout << number << endl;

     int result = sqrt(number);

     cout << result << endl;
    
    return 0;
}

