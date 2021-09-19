#include <iostream>
#include <vector>

using namespace std;

void readMatrix(vector<vector<int>> & matrix, int & n) {
    
    matrix.resize(n);
    for (int i = 0; i < n; i++) {
        matrix[i].resize(n);
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
}

int main()
{
    vector<vector<int>> matrix;
    int size;
    cin >> size;
    readMatrix(matrix, size);

    int sum = 0;

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < i; j++) {
            if (i + j >= size) {
                int number = matrix[i][j];
                bool isPrime = true;

                if (number == 0 || number == 1) {
                    isPrime = false;
                }

                else {
                    for (int k = 2; k <= number / 2; ++k) {
                        if (number % k == 0) {
                            isPrime = false;
                            break;
                        }
                    }
                }

                if (isPrime) {
                    sum += number;
                }
            }
        }

    }

    cout << sum << endl;
    return 0;
}

