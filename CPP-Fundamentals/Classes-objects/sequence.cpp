#include <iostream>
#include <string>
#include <vector>

using namespace std;
int maxLen = -1001;


void createSub(vector<int>& subVec) {
    int longest = maxLen;
    if (subVec.size() > longest) {
        longest = subVec.size();
    }
}

int main()
{
    int numCount;
    cin >> numCount;
    vector<int> vecOfNums;

    for (int i = 0; i < numCount; i++) {
        int num;
        cin >> num;
        vecOfNums.push_back(num);
    }

    vector<int> increasingSub;

    
    return 0;
}


