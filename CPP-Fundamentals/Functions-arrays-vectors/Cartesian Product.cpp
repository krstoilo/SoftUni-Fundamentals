#include <iostream>
#include <vector>

using namespace std;

vector<int> readArray()
{
    vector <int> array;
    int arrSize;
    cin >> arrSize;

    for (int i = 0; i < arrSize; i++)
    {
        int element;
        cin >> element;
        array.push_back(element);
    }

    return array;
}

vector<int> cartesian(const vector<int> & array, size_t arrSize)
{
    vector<int> productArray;

    for (int i = 0; i < arrSize; i++)
        for (int j = 0; j < arrSize; j++)
        {
            int multiplication = 0;
            multiplication = array[i] * array[j];
            productArray.push_back(multiplication);
        }

    return productArray;

}

int main()
{
    vector<int> array = readArray();
    
    size_t arrSize = array.size();

    vector<int> product = cartesian(array, arrSize);

    for (auto i : product)
    {
        cout << i << ' ';
    }

    return 0;
}

