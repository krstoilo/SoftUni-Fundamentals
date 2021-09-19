#include <iostream>
#include <vector>

using namespace std;

vector<int> belowAvrgVec(vector<int>& vec) {

    vector<int> belVec;
    int vecSize = vec.size();
    double avrg = 0.0;
    for (int i = 0; i < vec.size(); ++i) {
        avrg += vec[i];
    }
    avrg /= vecSize;

    for (auto n : vec) {
        if (n <= avrg) {
            belVec.push_back(n);
        }
    }
    return belVec;
}

void calculateSums(int& evenSum, int& oddSum, vector<int> & belowVec) {
    for (int i = 0; i < belowVec.size(); ++i) {
        if (i % 2 == 0) {
            evenSum += belowVec[i];
        }
        else {
            oddSum += belowVec[i];
        }
    }

}

int main()
{
    int vecSize;
    cin >> vecSize;

    vector<int> vec;
    for (int i = 0; i < vecSize; ++i) {
        int num;
        cin >> num;
        vec.push_back(num);
    }
    vector<int> belowVec = belowAvrgVec(vec);
    int evenSum = 0;
    int oddSum = 0;
    calculateSums(evenSum, oddSum, belowVec);
    cout << evenSum * oddSum << endl;


    return 0;
}
