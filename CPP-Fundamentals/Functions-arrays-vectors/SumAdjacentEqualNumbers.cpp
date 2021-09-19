#include <iostream>
#include <vector>

using namespace std;

vector<int> readArray(const int & size)
{
    vector<int> array;
    int tempNum;

    for (int i = 0; i < size; i++)
    {
        cin >> tempNum;
        array.push_back(tempNum);
    }

    return array;
}

bool adjacentEquals(const vector<int>& array, const int size)
{
    bool areEqual = false;
    int counter = 0;

    for (int i = 1; i < size; i++)
    {
        if (array[i] == array[i - 1])
        {
            counter++;
        }
    }
    
    if (counter > 0)
    {
        areEqual = true;
    }

    return areEqual;
}

void newArray(vector<int>& array, int size)
{

    while (true)
    {

        int sum = 0;
        int counter = 0;

        for (int i = 1; i < size; i++)
        {
            if (array[i] == array[i - 1])
            {
                sum = array[i] + array[i - 1];
                array[i] = sum;
                array.erase(array.begin()+counter);
                size = array.size();
            }
            else
            {
                counter++;
                continue;
            }
        }

        bool areEqual = adjacentEquals(array, size);
        if (areEqual == false)
        {
            break;
        }
    }
}


int main()
{
    int numOfElems;
    cin >> numOfElems;

    vector<int> array = readArray(numOfElems);

    newArray(array, numOfElems);

    for (auto n : array)
    {
        cout << n << " ";
    }

    return 0;
}

