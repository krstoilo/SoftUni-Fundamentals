#include <iostream>
#include <vector>

using namespace std;

void readMatrix (vector<vector<char>>& matrix) {

    int rows, cols;
    cin >> rows >> cols;
    
    matrix.resize(rows);
    for (int i = 0; i < rows; i++) {
        matrix[i].resize(cols);
        for (int j = 0; j < cols; j++) {
            cin >> matrix[i][j];
        }
    }
}

void fillPoints(char fillChar, char paintable, int rowpos, int colpos, vector<vector<char>> & matrix) {

    if (rowpos < 0 || rowpos > matrix.size() || colpos < 0 || colpos > matrix[0].size() || matrix[rowpos][colpos] != paintable) {
        return;
    }

    matrix[rowpos][colpos] = fillChar;

    fillPoints(fillChar, paintable, rowpos - 1, colpos, matrix);
    fillPoints(fillChar, paintable, rowpos, colpos + 1, matrix);
    fillPoints(fillChar, paintable, rowpos + 1, colpos, matrix);
    fillPoints(fillChar, paintable, rowpos, colpos - 1, matrix);

}

int main()
{
    vector<vector<char>> matrix;
    
    readMatrix(matrix);
    char fillChar;
    cin >> fillChar;
    int startRow, startCol;
    cin >> startRow >> startCol;

    char startChar = matrix[startRow][startCol];

    fillPoints(fillChar, startChar, startRow, startCol, matrix);

    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j];
        }
        cout << endl;
    }

    return 0;
}

