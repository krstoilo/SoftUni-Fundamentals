#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

void readGrid(vector<vector<char>>& grid, const int rows, const int cols) {
    grid.resize(rows);
    for (int i = 0; i < rows; ++i) {
        grid[i].resize(cols);
        for (int j = 0; j < cols; ++j) {
            cin >> grid[i][j];
        }
    }
}

bool isInBound(const vector<vector<char>>& grid, const int row, const int col)
{
    if (row >= 0 &&
        row < (int)grid.size() &&
        col >= 0 &&
        col < (int)grid[row].size())
    {
        return true;
    }

    return false;
}


// 1 4 7 2
// 0 0 1 9


//b=2
//[0][2]
//g[0][2](7) + g[0][1] + g[0][3] + g[1][2] + 

int bombIt (vector<vector<char>>& grid, const int row, const int col, const int bombPow) {
    int score = 0;
    if (bombPow == 0) {
        score += grid[row][col] - '0';
        grid[row][col] = '0';
    }
    else {
        for (int i = 1; i <= bombPow; i++) {
            score += grid[row][col] - '0';
            grid[row][col] = '0';

            if (isInBound(grid, row, col + i)) {
                score += grid[row][col + i] - '0';
                grid[row][col + i] = '0';
            }
            if (isInBound(grid, row, col - i)) {
                score += grid[row][col - i] - '0';
                grid[row][col - i] = '0';
            }
            if (isInBound(grid, row + i, col)) {
                score += grid[row + i][col] - '0';
                grid[row + i][col] = '0';
            }
            if (isInBound(grid, row - i, col)) {
                score += grid[row - i][col] - '0';
                grid[row - i][col] = '0';
            }
        }
    }
    return score;
}


void powerUp(int& bombPow) {
    bombPow++;
}

void powerDown(int& bombPow) {
    bombPow--;
    if (bombPow < 0) {
        bombPow = 0;
    }
}


int main()
{
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<char>> grid;
    readGrid(grid, rows, cols);

    int rounds;
    cin >> rounds;
    cin.ignore();
    int bombPow = 0;
    for (int i = 0; i < rounds; ++i) {
        string command;
        getline(cin, command);
        if (command == "power up") {
            powerUp(bombPow);
            cout << "Increased bomb power to " << bombPow << endl;
        }
        else if (command == "power down") {
            powerDown(bombPow);
            cout << "Decreased bomb power to " << bombPow << endl;
        }

        else {
            istringstream ssCom(command);
            string bomb;
            int row;
            int col;
            ssCom >> bomb;
            ssCom >> row;
            ssCom >> col;
            int score = bombIt(grid, row, col, bombPow);
            cout << score << " points" << endl;
            }
    }
    return 0;
}

