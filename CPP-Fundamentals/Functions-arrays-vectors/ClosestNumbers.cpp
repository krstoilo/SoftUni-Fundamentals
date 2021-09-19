#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

///read array
///find closest

 vector <int> readArray(const int& arrSize)
{

    vector<int> array;

    for (int i = 0; i < arrSize; i++)
    {
        int arrElement;
        cin >> arrElement;
        array.push_back(arrElement);
    }

    return array;

}

vector<int> findAbsDif(const vector<int>& array, const int& arrSize)
 {

    vector<int> absDifs;

    for (int i = 0; i < arrSize; i++)
    {
        for (int j = 0; j < arrSize; j++)
        {
            int difference = abs(array[i] - array[j]);
            if (difference != 0)
            {
                absDifs.push_back(difference);
            }
        }
    }

    return absDifs;

 }

bool equalElements(const vector<int>& array, const int & arrSize)
{
    bool areEqual = false;
    int counter = 0;

    for (int i = 0; i < arrSize; i++)
    {
        for (int j = 0; j < arrSize; j++)
        {
            if (array[i] == array[j])
            {
                counter++;
            }
        }
    }

    if (counter == (arrSize * arrSize))
    {
        areEqual = true;
    }

    return areEqual;
}


int main()
{

    int arrSize;
    cin >> arrSize;

    vector<int> array = readArray(arrSize);

    bool ifEqual = equalElements(array, arrSize);

    if (ifEqual)
    {
        cout << "0" << endl;
    }

    else 
    {
        vector<int> absDifs = findAbsDif(array, arrSize);

        sort(absDifs.begin(), absDifs.end());

        cout << absDifs[0] << endl;
    }
    
    return 0;
}

