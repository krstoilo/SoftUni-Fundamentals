#include <iostream>
#include <vector>

using namespace std;

vector<int> readMeasurements(const int& pipes) 
{

    vector<int> measurements;
    int temp = 0;

        for (int i = 0; i < pipes; i++) {

            cin >> temp;
            measurements.push_back(temp);
        }

     return measurements;

}


    int main() {

        int pipes;
        cin >> pipes;

        vector<int> checkup= readMeasurements(pipes);
        vector<int> installation = readMeasurements(pipes);

        vector<int> lifetimes;

        int damagePerYear = 0;
        int remainingYears = 0;

        for (int i = 0; i < pipes; i++) {

            damagePerYear = installation[i] - checkup[i];
            remainingYears = abs(installation[i] / damagePerYear);

            lifetimes.push_back(remainingYears);
        }


        for (int num : lifetimes) {

            cout << num << " ";
        }

        return 0;
    }


