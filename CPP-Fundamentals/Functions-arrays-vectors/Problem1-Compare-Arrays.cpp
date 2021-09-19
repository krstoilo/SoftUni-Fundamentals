#include <iostream>

using namespace std;

const int maxSize = 100;

bool compareArrays (int arr1[], int arr1Size, int arr2[], int arr2Size)
{
    bool areEqual = false;
    bool equalSize = false;
    bool equalElements = false;
    int equalsCounter = 0;


    if (arr1Size == arr2Size)
    {
        equalSize = true;
    }

    for (int i = 0; i < arr1Size; i++)
    {
        if (arr1[i] == arr2[i]) 
        {
            equalsCounter++;
        }
    }

    if (equalsCounter == arr1Size)
    {
        equalElements = true;
    }

    if (equalSize == 1 && equalElements == 1)
    {
        areEqual = true;
    }

    return areEqual;
}

int main()
{

    int arraySize1, arraySize2;

    cin >> arraySize1;
    int array1[maxSize];
    for (int i = 0; i < arraySize1; i++)
    {
        int enteredValue;
        cin >> enteredValue;
        array1[i] = enteredValue;
    }

    cin >> arraySize2;

    int array2[maxSize];
    for (int j = 0; j < arraySize2; j++)
    {
        int enteredValue;
        cin >> enteredValue;
        array2[j] = enteredValue;
    }

    bool areEqual = compareArrays(array1, arraySize1, array2, arraySize2);

        if (areEqual)
        {
            cout << "equal" << endl;
        }

        else
        {
            cout << "not equal" << endl;
        }

    return 0; 
}

