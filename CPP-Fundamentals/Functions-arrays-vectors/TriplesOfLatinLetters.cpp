#include <iostream>

using namespace std; 

int main()
{
    int n;

    cin >> n;

    if (n > 26)
    {
        cout << "Error! Not enough letters!" << endl;
        return 1;
    }

    char startingCount = n + 97;

    for (char i = 97; i < startingCount; i++)
    {
        for (char j = 97; j < startingCount; j++)
        {
            for (char k = 97; k < startingCount; k++)
            {
                cout << i << j << k << endl;
            }
        }
    }

    return 0;
}

