#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

void findSum(string& text, int& sum)
{
    int stringSize = text.size();
    vector<int> nums;
    for (int i = 0; i < stringSize; i++)
    {
        if (isdigit(text[i]))
        {
            nums.push_back(text[i] - '0');
        }
    }


    for (auto n : nums)
    {
        sum += n;
    }
}

bool isLetter(int& sum)
{
    if (sum >= 65 && sum <= 90 || sum >= 97 && sum <= 122)
    {
        return true;
    }

    return false;
}

int main()
{
    string inputText; 
    getline(cin, inputText);
    int digitSum = 0;
    findSum(inputText, digitSum);

    if (isLetter(digitSum))
    {
        char let = digitSum;
        cout << let;
    }
    else
    {
        cout << digitSum;
    }

    return 0;
}


