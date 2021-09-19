#include <iostream>
#include <vector>

using namespace std;

void readMatrix(vector<vector<int>> & matrix, int & size) {

    matrix.resize(size);
    for (int i = 0; i < size; i++) {
        matrix[i].resize(size);
        for (int j = 0; j < size; j++) {
            cin >> matrix[i][j];
        }
    }
}

vector<int> findNonDiagonals(vector<vector<int>>& matrix, int & size) {
    vector<int> nonDiagonalNums;

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if ((i != j) && (i+j != (size-1))) {
                nonDiagonalNums.push_back(matrix[i][j]);
            }
        }
    }


    return nonDiagonalNums;

}

int main()
{
    int matrixSize;
    cin >> matrixSize;

    vector <vector<int>> matrix;
    readMatrix(matrix, matrixSize);

    vector<int> nonDiag = findNonDiagonals(matrix, matrixSize);
    int sum = 0;

    for (auto n : nonDiag) {
        if (n % 2 != 0) {
            sum += n;
        }
    }
    
    cout << "The sum is: " << sum << endl;

    return 0;
}

