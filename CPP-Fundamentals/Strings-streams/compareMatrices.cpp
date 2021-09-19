#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<vector<int>> readMatrix() {

    int rowCount;
    cin >> rowCount;
    cin.ignore();
    vector<vector<int>> matrix;
    for (int i = 0; i < rowCount; i++) {
        vector<int> row;
        string nums;
        getline(cin, nums);
        istringstream ssNums(nums);
        int num;
        while (ssNums >> num) {
            row.push_back(num);
        }
        matrix.push_back(row);
    }

    return matrix;
}

bool compareMatrices(const vector<vector<int>>& m1, const vector<vector<int>>& m2) {

    bool areEqual = true;

    if (m1[0].size() != m2[0].size()) {
        areEqual = false;
    }

    else {
        for (int i = 0; i < m1.size(); i++) {
            for (int j = 0; j < m1[i].size(); j++) {
                if (m1[i][j] != m2[i][j]) {
                    areEqual = false;
                    break;
                }
            }

            if (areEqual == false) {
                break;
            }
        }
    }

    return areEqual;

}

int main()
{

    vector<vector<int>> matrix1 = readMatrix();
    vector <vector<int>> matrix2 = readMatrix();

    bool equality = compareMatrices(matrix1, matrix2);

    if (equality) {
        cout << "equal" << endl;
    }

    else {
        cout << "not equal" << endl;
    }

    return 0;
}

