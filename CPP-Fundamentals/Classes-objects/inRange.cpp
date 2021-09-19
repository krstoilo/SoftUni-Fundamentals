#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>

using namespace std;

void readInput(vector<int>& listNums) {
    string textInput;
    getline(cin, textInput);
    int num;
    istringstream ssNums(textInput);
    while (ssNums >> num) {
        listNums.push_back(num);
    }
}

void fillSet(set<int>& sortedNums, vector<int>& nums, int & start, int& end) {
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] >= start && nums[i] < end) {
            sortedNums.insert(nums[i]);
        }
    }
}


int main()
{
    vector<int> numbers;
    readInput(numbers);
    int start, end;
    cin >> start >> end;

    set<int> sortedNumbers;
    fillSet(sortedNumbers, numbers, start, end);
    for (auto n : sortedNumbers) {
        cout << n << " ";
    }

    return 0;
}

