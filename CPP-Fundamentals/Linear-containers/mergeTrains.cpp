#include <iostream>
#include <stack>
#include <string>
#include <sstream>

using namespace std;

stack <int> composeTrain() {

    stack<int> train;
    string numbers;
    getline(cin, numbers);
    int num;
    istringstream ssLine(numbers);
    while (ssLine >> num) {
        train.push(num);
    }

    return train;
}

stack<int> compareTrains(stack<int>& trainA, stack<int>& trainB) {

    stack<int> newTrain;

    while (!trainA.empty() && !trainB.empty())
    {
        if (trainA.top() >= trainB.top()) {
            newTrain.push(trainB.top());
            trainB.pop();
            cout << "B";
        }
        else {
            newTrain.push(trainA.top());
            trainA.pop();
            cout << "A";
        }
    }

    if (!trainA.empty() && trainB.empty()) {

        while (!trainA.empty()) {
            newTrain.push(trainA.top());
            trainA.pop();
            cout << "A";
        }

    }

    else {
        while (!trainB.empty()) {
            newTrain.push(trainB.top());
            trainB.pop();
            cout << "B";
        }

    }
    
    cout << endl;
    return newTrain;
}

int main()
{

    stack<int> trainA = composeTrain();
    stack<int> trainB = composeTrain();

    stack<int> newTrain = compareTrains(trainA, trainB);
    while (!newTrain.empty()){
        cout << newTrain.top() << " ";
        newTrain.pop();
    }
    
    return 0;
}

