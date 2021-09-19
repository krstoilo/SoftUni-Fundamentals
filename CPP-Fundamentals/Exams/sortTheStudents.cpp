#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
    int numberOfStudents;
    cin >> numberOfStudents;

    int studentCount = 0;

    map<string, double> students;
    map<double, string, greater<double>> scores;

    while (studentCount < numberOfStudents) {
        string fName;
        string lName;
        double avgScore;

        cin >> fName >> lName >> avgScore;
        string fullname = fName + " " + lName;

        students.insert(pair<string,double>(fullname, avgScore));
        scores.insert(pair<double, string>(avgScore, fullname));
        studentCount++;
    }

    for (auto m : scores) {
        cout << m.second << " " << m.first << endl;
    }

    cout << endl;

    for (auto n : students) {
        cout << n.first << " " << n.second << endl;
    }

    return 0;
}

