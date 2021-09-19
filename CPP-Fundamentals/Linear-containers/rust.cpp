#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<vector<char>> readMatrix() {

    vector<vector<char>> matrix;
    matrix.resize(10);
    for (int i = 0; i < 10; i++) {
        matrix[i].resize(10);
        for (int j = 0; j < 10; j++) {
            cin >> matrix[i][j];
        }
    }

    return matrix;
}

void findRustElement(const vector<vector<char>>& matrix, queue<int>& row, queue<int>& col) {

    int mat_row = matrix.size();
    for (int i = 0; i < mat_row; i++) {
        int mat_col = matrix[i].size();
        for (int j = 0; j < mat_col; j++) {
            if (matrix[i][j] == '!') {
                row.push(i);
                col.push(j);
            }
        }
    }
}

bool inScope(const vector<vector<char>>& matrix, const int row, const int col) {

    if (row >= 0 && row < matrix.size() && col >= 0 && col < matrix[row].size()) {
        return true;
    }
    return false;
}

void rustParticle(vector<vector<char>>& matrix, const int row, const int col) {

    //top
    if (inScope(matrix, row - 1, col)) {
        if (matrix[row-1][col] != '#') {
            matrix[row - 1][col] = '!';
        }
    }

    //bottom
    if (inScope(matrix, row + 1, col)) {
        if (matrix[row + 1][col] != '#') {
            matrix[row + 1][col] = '!';
        }
    }
    //left
    if (inScope(matrix,row,col-1)) {
        if (matrix[row][col-1] != '#') {
            matrix[row][col-1] = '!';
        }
    }
    //right
    if (inScope(matrix,row,col+1)) {
        if (matrix[row][col+1] != '#') {
            matrix[row][col+1] = '!';
        }
    }

}

void rust(vector<vector<char>>& matrix, queue<int> & rows, queue<int> & cols) {

    int curRow = 0;
    int curCol = 0;
    while (!rows.empty()) {
        curRow = rows.front();
        rows.pop();
        curCol = cols.front();
        cols.pop();

        rustParticle(matrix, curRow, curCol);
    }

}

int main()
{
    vector<vector<char>> matrix = readMatrix();

    int time_elapsed;
    cin >> time_elapsed;
   
    for (int k = 0; k < time_elapsed; k++) {

        queue<int> rows;
        queue<int> cols;
        findRustElement(matrix, rows, cols);
        rust(matrix, rows, cols);

    }
    
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j];
        }
        cout << endl;
    }

}


