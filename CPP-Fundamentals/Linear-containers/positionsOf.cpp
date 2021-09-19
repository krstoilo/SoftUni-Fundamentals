#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<vector<int>> readMatrix(int rows) {

    
    vector<vector<int>> matrix;
    for (int i = 0; i < rows; i++) {
        vector<int> row;
        string numbers;
        getline(cin, numbers);
        int num;
        istringstream ssNums(numbers);
        while (ssNums >> num) {
            row.push_back(num);
        }
        matrix.push_back(row);
    }

    return matrix;
}


int main()
{
    int rows, cols;
    cin >> rows >> cols;
    cin.ignore();
    vector<vector<int>> matrix = readMatrix(rows);
    int numToFind;
    cin >> numToFind;
    int matches = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (matrix[i][j] == numToFind) {
                cout << i << " " << j << endl;
                matches++;
            }
        }
    }

    if (matches == 0) {
        cout << "not found" << endl;
    }

    return 0;
}


