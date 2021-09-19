#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main()
{
    int arSize;
    cin >> arSize;
    vector<int> ar;
    double avgScore = 0;

    for (int i = 0; i < arSize; i++)
    {
        int num;
        cin >> num;
        ar.push_back(num);
        avgScore += num;
    }

    avgScore /= arSize;
    vector<int> resVec;

    for (auto n : ar)
    {
        if (n > avgScore)
        {
            resVec.push_back(n);
        }
    }

    sort(resVec.begin(), resVec.end(), greater<int>());

    if (resVec.empty())
    {
        cout << "No" << endl;
    }
    else
    {
        int vecSize = resVec.size();
        int topEl = 0;
        for (int j = 0; j < vecSize; j++)
        {
            cout << resVec[j] << " ";
            topEl++;
            if (topEl == 5)
            {
                break;
            }
        }
    }

    return 0;
}


