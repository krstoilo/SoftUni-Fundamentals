#include <iostream>
#include <vector>

using namespace std;

int turnToMins(const int arrivalTime)
{
    int hours = arrivalTime / 100 * 60;

    int mins = arrivalTime % 100;

    int minsAfterMidnight = hours + mins;

    return minsAfterMidnight;
}

int compareTimes(const int trainTime, vector<int> & arrivalTimes)
{
    int waitingMins = INT_MAX;

    int trainTimeMins = turnToMins(trainTime);

    for (int i = 0; i < arrivalTimes.size(); i++)
    {
        int busArrivalMins = turnToMins(arrivalTimes[i]);

        int difference = trainTimeMins - busArrivalMins;

        if (difference < 0)
        {
            difference = 1440 - (busArrivalMins - trainTimeMins);
        }

        if (difference < waitingMins)
        {
            waitingMins = difference;
        }
    }

    return waitingMins;
}

vector<int> returnBusTimes(const int trainTime, vector<int> & arrivalTimes)
{
    vector<int> busTimes;

    int waitingMins = INT_MAX;

    int trainTimeMins = turnToMins(trainTime);

    for (int i = 0; i < arrivalTimes.size(); i++)
    {
        int busArrivalMins = turnToMins(arrivalTimes[i]);

        int difference = trainTimeMins - busArrivalMins;

        if (difference < 0)
        {
            difference = 1440 - (busArrivalMins - trainTimeMins);
        }

        if (difference < waitingMins)
        {
            waitingMins = difference;
        }

        busTimes.push_back(difference);
    }

    return busTimes;
}

int findBusNumber(vector<int>& busNumbers)
{
    int temp = INT_MAX;
    int busNumber = 0;

    for (int i = 0; i < busNumbers.size(); i++)
    {
        if (busNumbers[i] < temp)
        {
            temp = busNumbers[i];
            busNumber = i+1;
        }
    }

    return busNumber;
}


int main()
{
    int numberOfBuses;
    cin >> numberOfBuses;

    vector<int> arrivalTimes;

    for (int i = 0; i < numberOfBuses; i++)
    {
        int time;
        cin >> time;
        arrivalTimes.push_back(time);
    }

    int trainTime;
    cin >> trainTime;

    cout << compareTimes(trainTime, arrivalTimes) << endl;

    vector<int> busTimes = returnBusTimes(trainTime, arrivalTimes);

    cout << findBusNumber(busTimes) << endl;

    return 0;
}

