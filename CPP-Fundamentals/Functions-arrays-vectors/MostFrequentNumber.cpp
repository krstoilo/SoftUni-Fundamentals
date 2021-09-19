#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> readArray()
{

	vector<int> array;

	int numsInArray;
	cin >> numsInArray;
	int currentNum;

	for (int i = 0; i < numsInArray; i++)
	{
		cin >> currentNum;
		array.push_back(currentNum);
	}

	return array;

}

vector<int> findMostFrequent(vector<int> & array, size_t arraySize)
{

	int maxCount = 1;
	int currCount = 1;
	vector<int> resultArray;
	bool wentThroughLoop = false;


	for (int i = 1; i < arraySize; i++)
	{
		if (array[i] == array[i - 1])
		{
			currCount++;
			wentThroughLoop = true;
		}

		else
		{
			if (currCount > maxCount)
			{
				maxCount = currCount;
				if (resultArray.empty()) {
					resultArray.push_back(array[i - 1]);
				}
				else {
					resultArray.clear();
					resultArray.push_back(array[i - 1]);
				}
			}

			else if (currCount == maxCount)
			{
				if (!resultArray.empty()) {
					resultArray.push_back(array[i - 1]);
				}
			}
			
			currCount = 1;
		}
	}

	if (currCount >= maxCount)
	{
		maxCount == currCount;
		resultArray.push_back(array.back());
	}

	if (wentThroughLoop)
	{
		return resultArray;
	}

	else
	{ 
		return array;
	}
}


int main()
{
	vector<int> array = readArray();

	sort(array.begin(), array.end());

	size_t arSize = array.size();

	vector<int> result = findMostFrequent(array, arSize);

	for (auto i : result)
	{
		cout << i << " ";
	}

	return 0;
}

