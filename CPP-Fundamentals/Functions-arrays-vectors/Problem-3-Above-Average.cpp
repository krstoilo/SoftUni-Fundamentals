#include <iostream>
#include <vector>

using namespace std;


vector<int> readArray(int arraySize)
{
    vector<int> arr;

    for (int i = 0; i < arraySize; i++)
    {
        int currentElem;
        cin >> currentElem;

        arr.push_back(currentElem);
    }

    return arr;
}

int findAverage(vector<int> arr, int arraySize)
{
    int average = 0;

    for (int i = 0; i < arraySize; i++)
    {
        average += arr[i];
    }

    average /= arraySize;

    return average;

}

vector<int> compareToAverage(vector<int>arr, int arraySize, float average)
{
    vector<int> newVec;

    for (int i = 0; i < arraySize; i++)
    {
        if (arr[i] >= average)
        {
            newVec.push_back(arr[i]);
        }
    }
    return newVec;
}

int main()
{

    int arraySize;
    cin >> arraySize;

    vector<int> arr = readArray(arraySize);

    float average = findAverage(arr, arraySize);

    vector<int> aboveAverages = compareToAverage(arr, arraySize, average);

    for (auto i : aboveAverages)
    {
        cout << i << " ";
    }

    return 0;
}
