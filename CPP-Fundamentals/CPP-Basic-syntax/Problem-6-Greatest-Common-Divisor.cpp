#include <iostream>

using namespace std;

int gcd(int a, int b) 
{
    int R;

    while ((a % b) != 0) 
    {
        R = a % b;
        a = b;
        b = R;
    }

    return b;
}

int main()
{
    int a, b;
    cin >> a >> b;

    int result = gcd(a, b);
    cout << result << endl;

    return 0;
}

