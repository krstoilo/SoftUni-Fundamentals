#include <iostream>
#include <vector>

using namespace std; 

//Write a program that reads an integer array from the console(given by size, followed by the elements of the array), 
//followed by an integer number and prints the index of that number in the array on the console
//(if the number does not appear in the array, print - 1).


vector<int> readArray()
{
    
    int elemCount;
    cin >> elemCount;

    vector<int> array(elemCount);

    for (int i = 0; i < elemCount; i++)
    {
        cin >> array[i];
    }

    return array;
}

int findIndex(const int& number, const vector<int> & array)
{
    int index = -1; 

    for (int i = 0; i < array.size(); i++)
    {
        if (number == array[i])
        {
            index = i;
        }
    }

    return index;
}

int main()
{
    vector<int> array = readArray();

    int number;
    cin >> number;

    cout << findIndex(number, array) << endl;

    return 0;
}


