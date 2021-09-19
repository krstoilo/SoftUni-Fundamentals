#include <iostream>
#include <vector>

using namespace std;

void readMatrix(vector<vector<int>>& matrix, const int rows, const int cols) {

    matrix.resize(rows);
    for (int i = 0; i < rows; ++i) {
        matrix[i].resize(cols);
        for (int j = 0; j < cols; ++j) {
            cin >> matrix[i][j];
        }
    }
}

int calculateSquareSum(vector<vector<int>>& square, const int squareSide) {
    int sum = 0;
    for (int i = 0; i < squareSide; ++i) {
        for (int j = 0; j < squareSide; ++j) {
            sum += square[i][j];
        }
    }

    return sum;
}

bool isAboveTarget(const int& sum, const int& target) {
    bool isAbove = false;
    if (sum > target) {
        isAbove = true;
    }
    return isAbove;
}

int main()
{
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> matrix;
    readMatrix(matrix, rows, cols);
    int squareSide, targetSum;
    cin >> squareSide >> targetSum;
    vector<int> averageScores;
    vector<vector<int>> square;

    for (int i = 0; i < (i + squareSide); ++i) {
        for (int j = 0; j < (j + squareSide); ++i) {
            
        }
    }

 

    return 0;
}


