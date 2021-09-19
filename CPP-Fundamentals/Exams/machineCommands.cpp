#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

void insertNumber(vector<int>& mem, string & command) {

    istringstream ssCom(command);
    int num;
    while (ssCom >> num) {
        mem.push_back(num);
    }
}

void sumElements(vector<int>& mem) {
    int sum = 0;
    sum += mem.back();
    mem.pop_back();
    sum += mem.back();
    mem.pop_back();
    mem.push_back(sum);
}

void subtractElements(vector<int>& mem) {
    int result = 0;
    result += mem.back();
    mem.pop_back();
    result -= mem.back();
    mem.pop_back();
    mem.push_back(result);
}

void concatenate(vector<int>& mem) {
    int numOne = mem.back();
    mem.pop_back();
    int numTwo = mem.back();
    mem.pop_back();
    ostringstream ssNum;
    ssNum << numTwo << numOne;
    string result = ssNum.str();
    istringstream ssRes(result);
    int resNum;
    ssRes >> resNum;
    mem.push_back(resNum);
}

int main()
{
    vector<int> memoryVec;
    string command;
    cin >> command;

    while (command != "end") 
    {
        if (command == "sum")
        {
            sumElements(memoryVec);
        }
        else if (command == "subtract")
        {
            subtractElements(memoryVec);
        }
        else if (command == "concat")
        {
            concatenate(memoryVec);
        }
        else if (command == "discard")
        {
            memoryVec.pop_back();
        }
        else
        {
            insertNumber(memoryVec, command);   
        }
      
        cin >> command;
    }

    for (auto n : memoryVec) {
        cout << n << endl;
    }
    return 0;
}


