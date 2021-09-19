#include <iostream>
#include <cmath>

using namespace std;

int main()
{

	double long n;
	cin >> n;

	long double factorial = n;

	for (long double j = 1; j < n; j++)
	{
		factorial *= j;
	}
	
	int trailingZeroes = 0;
	

	for (int i = 1; (n/i) >= 1; i++)
	{
		int result = 0;

		result = n / (pow(5, i));
		
		//for(int i = 1; i != 0; i++)
		//if (result < 1)
		//{
		//	break;
		//}
		
		trailingZeroes += result;
	}

	if (trailingZeroes == 0) 
	{

		cout << "n != " << factorial << " , no trailing zeroes" << endl;
	}

	else if (trailingZeroes == 1)
	{
		cout << "n != " << factorial << " , 1 trailing zero" << endl;
	}

	else
	{
		cout << "n != " << factorial << " , " << trailingZeroes << " trailing zeroes" << endl;
	}

	return 0;
}