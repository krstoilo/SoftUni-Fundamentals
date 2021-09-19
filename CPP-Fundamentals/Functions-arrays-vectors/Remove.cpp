#include <iostream>
#include <vector>

using namespace std;

vector<int> readInput()
{
    int vecSize;
    cin >> vecSize;

    vector<int> array(vecSize);

    for (int i = 0; i < vecSize; i++)
    {
        cin >> array[i];
    }

    return array;
}

vector<int> recordNewArray(const int number, const vector<int>& array)
{
    vector<int> newArray;
    for (int i = 0; i < array.size(); i++)
    {
        if (number != array[i])
        {
            newArray.push_back(array[i]);
        }
    }
    return newArray;
}


int main()
{
    vector<int> array = readInput();

    int number;
    cin >> number;
    
    vector<int> newArray = recordNewArray(number, array);

    for (auto k : newArray)
    {
        cout << k << " ";
    }
    
    return 0;
}

