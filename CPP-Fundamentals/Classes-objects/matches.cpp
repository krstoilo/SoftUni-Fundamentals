#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>

using namespace std;

void readInput(vector<int>& row) {
    string text;
    getline(cin, text);
    istringstream ssText(text);
    int num;
    while (ssText >> num) {
        row.push_back(num);
    }
}

void fillSet(vector<int>& row1, vector<int>& row2, set<int>& newRow) {
    int size = 0;
    if (row1.size() >= row2.size()) {
        size = row2.size();
    }
    else {
        size = row1.size();
    }
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (row1[i] == row2[j]) {
                newRow.insert(row1[i]);
            }
        }
    }
}

int main()
{
    vector<int> row1;
    vector<int> row2;
    readInput(row1);
    readInput(row2);
    set<int> newRow;

    fillSet(row1, row2, newRow);
    if (newRow.empty()) {
        cout << "no matches" << endl;
    }
    else {
        for (auto n : newRow) {
            cout << n << " ";
        }
    }

    return 0;
}

