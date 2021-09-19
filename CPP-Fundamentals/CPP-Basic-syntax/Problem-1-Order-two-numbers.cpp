#include <iostream>

using namespace std; 

int main()
{
	int firstNum, secNum;
	cin >> firstNum >> secNum;

	if (firstNum > secNum)
	{
		cout << secNum << " " << firstNum;
	}

	else
	{
		cout << firstNum << " " << secNum;
	}

	return 0;
}
