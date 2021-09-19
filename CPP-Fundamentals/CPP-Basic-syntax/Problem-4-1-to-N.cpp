#include <iostream>

using namespace std;

int main()
{
	int number;
	cin >> number;

	if (number <= 0)
	{
		cout << "error" << endl;
	}

	for (int i = 1; i <= number; i++)
	{
		cout << i << " ";
	}

	
	return 0;
}
