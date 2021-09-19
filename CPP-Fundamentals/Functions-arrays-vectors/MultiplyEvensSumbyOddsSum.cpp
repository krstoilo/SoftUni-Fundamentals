#include <iostream>
#include <vector>

using namespace std;

int sumEven(int number)
{
    int evenSum = 0;
    int tempNum;
    vector<int> evenNums;
   
    while (number != 0)
    {
        tempNum = number % 10;
        number = number / 10;

        if (tempNum % 2 == 0)
        {
            evenNums.push_back(tempNum);
        }
    }

    for (auto n : evenNums)
    {
        evenSum += n;
    }

    return evenSum;
}

int sumOdd (int number)
{
    int oddSum = 0;
    int tempNum;
    vector<int> oddNums;

    while (number != 0)
    {
        tempNum = number % 10;
        number = number / 10;

        if (tempNum % 2 == 1)
        {
            oddNums.push_back(tempNum);
        }
    }

    for (auto n : oddNums)
    {
        oddSum += n;
    }

    return oddSum;
}

int main()
{
    int number;
    cin >> number;

    if (number < 0)
    {
        number = abs(number);
    }

    int evenSum = sumEven(number);
    int oddSum = sumOdd(number);

    cout << evenSum * oddSum << endl;

    return 0;
}

