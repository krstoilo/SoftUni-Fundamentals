#include <iostream>
#include <vector>

using namespace std; 

int main()
{
    int n, m;
    cin >> n >> m;

    vector < vector<int> >matrixArray;

    for (int i = 0; i < n; i++)
    {
        vector<int> insideArray;

        for (int j = 0; j < m; j++)
        {
            int value;
            cin >> value;
            insideArray.push_back(value);
        }

        matrixArray.push_back(insideArray);
    }

    vector<int> weights;

    for (int k = 0; k < n; k++)
    {
        int weight;
        cin >> weight;
        weights.push_back(weight);
    }

    vector<int> result;
    int sum = 0;

    for (int cols = 0; cols < m; cols++)
    {
        for (int rows = 0; rows < n; rows++)
        {
            sum += matrixArray[rows][cols] * weights[rows];
        }

        result.push_back(sum);
        sum = 0;
    }

    for (auto n : result)
    {
        cout << n << " ";
    }

    return 0;
}

