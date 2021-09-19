#include <iostream>
#include <vector>

using namespace std;

void readMatrix(vector< vector<char>>& matrix, int & matrixSize) 
{

    matrix.resize(matrixSize);
    for (int i = 0; i < matrixSize; i++)
    {
        matrix[i].resize(matrixSize);
        for (int j = 0; j < matrixSize; j++)
        {
            cin >> matrix[i][j];
        }
    }
}

bool isInBound(vector<vector<char>>& matrix, int &row, int &col)
{
   
if (row >= 0 &&
    row < (int)matrix.size() &&
    col >= 0 &&
    col < (int)matrix[row].size())
{
    return true;
}

return false;
}

void moveUp(vector<vector<char>>& matrix, int & spaceDust)
{
    bool foundIt = false;
    for (int row = 0; row < matrix.size(); row++)
    {
        for (int col = 0; col < matrix.size(); col++) 
        {
            if (matrix[row][col] == 'K') 
            {
                int up = row - 1;
                if (isInBound(matrix, up , col)) 
                {
                    if (matrix[up][col] == 'V') {
                        spaceDust += 'V';
                    }
                    else if (matrix[up][col] == 'S')
                    {
                        spaceDust += 'S';
                    }
                    else if (matrix[up][col] == 'U')
                    {
                        spaceDust += 'U';
                    }
                    else if (matrix[up][col] == 'N')
                    {
                        spaceDust += 'N';
                    }
                    else
                    {
                        spaceDust /= 2;
                    }
                    matrix[up][col] = 'K';
                    matrix[row][col] = '-';
                    foundIt = true;
                    break;
                }
                else {
                    spaceDust -= 4 * spaceDust;
                    foundIt = true;
                    break;
                }
            }
        }
        if (foundIt) { break; }
    }
}

void moveDown(vector<vector<char>>& matrix, int& spaceDust)
{
    bool foundIt = false;
    for (int row = 0; row < matrix.size(); row++)
    {
        for (int col = 0; col < matrix.size(); col++)
        {
            if (matrix[row][col] == 'K')
            {
                int down = row + 1;
                if (isInBound(matrix, down, col))
                {
                    if (matrix[down][col] == 'V') {
                        spaceDust += 'V';
                    }
                    else if (matrix[down][col] == 'S')
                    {
                        spaceDust += 'S';
                    }
                    else if (matrix[down][col] == 'U')
                    {
                        spaceDust += 'U';
                    }
                    else if (matrix[down][col] == 'N')
                    {
                        spaceDust += 'N';
                    }
                    else
                    {
                        spaceDust /= 2;
                    }
                    matrix[down][col] = 'K';
                    matrix[row][col] = '-';
                    foundIt = true;
                    break;
                }
                else {
                    spaceDust -= 4 * spaceDust;
                    foundIt = true;
                    break;
                }
            }
        }
        if (foundIt) { break; }
    }
}

void moveLeft (vector<vector<char>>& matrix, int& spaceDust)
{
    bool foundIt = false;
    for (int row = 0; row < matrix.size(); row++)
    {
        for (int col = 0; col < matrix.size(); col++)
        {
            if (matrix[row][col] == 'K')
            {
                int left = col - 1;
                if (isInBound(matrix, row, left))
                {
                    if (matrix[row][left] == 'V') {
                        spaceDust += 'V';
                    }
                    else if (matrix[row][left] == 'S')
                    {
                        spaceDust += 'S';
                    }
                    else if (matrix[row][left] == 'U')
                    {
                        spaceDust += 'U';
                    }
                    else if (matrix[row][left] == 'N')
                    {
                        spaceDust += 'N';
                    }
                    else
                    {
                        spaceDust /= 2;
                    }
                    matrix[row][left] = 'K';
                    matrix[row][col] = '-';
                    foundIt = true;
                    break;
                }
                else {
                    spaceDust -= 4 * spaceDust;
                    foundIt = true;
                    break;
                }
            }
        }
        if (foundIt) { break; }
    }
}

void moveRight(vector<vector<char>>& matrix, int& spaceDust)
{
    bool foundIt = false;
    for (int row = 0; row < matrix.size(); row++)
    {
        for (int col = 0; col < matrix.size(); col++)
        {
            if (matrix[row][col] == 'K')
            {
                int right = col + 1;
                if (isInBound(matrix, row, right))
                {
                    if (matrix[row][right] == 'V') {
                        spaceDust += 'V';
                    }
                    else if (matrix[row][right] == 'S')
                    {
                        spaceDust += 'S';
                    }
                    else if (matrix[row][right] == 'U')
                    {
                        spaceDust += 'U';
                    }
                    else if (matrix[row][right] == 'N')
                    {
                        spaceDust += 'N';
                    }
                    else
                    {
                        spaceDust /= 2;
                    }
                    matrix[row][right] = 'K';
                    matrix[row][col] = '-';
                    foundIt = true;
                    break;
                }
                else {
                    spaceDust -= 4 * spaceDust;
                    foundIt = true;
                    break;
                }
            }
        }
        if (foundIt) { break; }
    }
}


int main()
{
    int mSize;
    cin >> mSize;
    vector<vector<char>> matrix;
    readMatrix(matrix, mSize);
    int spaceDust;
    cin >> spaceDust;
    char command;
    cin >> command;
    while (command != 'S')
    {
        if (command == 'U')
        {
            moveUp(matrix, spaceDust);
        }
        else if (command == 'D')
        {
            moveDown(matrix, spaceDust);
        }
        else if (command == 'L')
        {
            moveLeft(matrix, spaceDust);
        }
        else if (command == 'R')
        {
            moveRight(matrix, spaceDust);
        }

        cin >> command;
    }
    cout << "Space Dust Collected: " << spaceDust << endl;
    for (auto row : matrix)
    {
        for (auto col : row)
        {
            cout << col << " ";
        }
        cout << endl;
    }

    return 0;
}


