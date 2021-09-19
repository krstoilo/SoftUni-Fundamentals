#include <iostream>
#include <vector>

using namespace std;

//Write a program that finds the longest sequence of equal elements in an integer array and then prints that sequence on the console
//(integers separated by space on a single line).If there is more than one such sequence, print the last one.
//The input array will be entered on two lines the first line will contain an integer representing the number of elements, 
//the second will contain the elements separated by spaces

void longestSequence(vector<int> array, int arraySize)
{

	int counter = 1;
	int repeatingElem = 0;
	int elemCount = 0;

	for (int i = 1; i < (arraySize); i++)
	{
		if (array[i-1] == array[i])
		{
			repeatingElem = array[i];
			counter++;
			elemCount = counter;
		}
		else
		{
			counter = 1;
		}
	}


	if (arraySize == 1)
	{
		cout << array[0] << " ";
	}

	else if (elemCount == 0)
	{
		cout << array[arraySize - 1];
	}

	else
	{
		for (int j = 0; j < elemCount; j++)
		{
			cout << repeatingElem << " ";
		}
	}
}


int main()
{
	int arrSize;
	cin >> arrSize;

	vector<int> arr;

	for (int i = 0; i < arrSize; i++)
	{
		int intInput;
		cin >> intInput;
		arr.push_back(intInput);
	}

	longestSequence(arr, arrSize);
	
	return 0;
}