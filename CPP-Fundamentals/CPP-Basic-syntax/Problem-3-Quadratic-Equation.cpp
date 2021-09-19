#include <iostream>
#include <cmath>

using namespace std; 

int main()
{
    float a, b, c;
    cin >> a >> b >> c;

    float discriminant = pow(b, 2) - 4 * a * c;

    if (discriminant < 0)
    {
        cout << "no roots" << endl;
    }

    else if (discriminant == 0)
    {
        float root = -b / (2 * a);
        cout << root;
    }

    else if (discriminant > 0)
    {
        float root1, root2;
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);

        cout << root1 << " " << root2;
    }

    return 0;
}
