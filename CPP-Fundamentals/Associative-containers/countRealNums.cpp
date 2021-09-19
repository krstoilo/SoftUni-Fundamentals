#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>

using namespace std;

void readNumbers(vector<double>& nums){

    string numbers;
    getline(cin, numbers);
    istringstream ssNums(numbers);
    double curNum;
    while (ssNums >> curNum) {
        nums.push_back(curNum);
    }
}

void recordEntries(vector<double>& nums, map<double, int> & mapOfNums) {

    
    for (auto i = 0; i < nums.size(); i++) {
        mapOfNums[nums[i]]++;
    }


}
int main()
{
    vector<double> numbers;
    readNumbers(numbers);
    map<double, int> mapOfNums;
    recordEntries(numbers, mapOfNums);
 
    for (auto i = mapOfNums.begin(); i != mapOfNums.end(); i++) {
        cout << i->first << " -> " << i->second << endl;
    }

    return 0;
}

