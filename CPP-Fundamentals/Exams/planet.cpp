#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const long long int c = 299792;

class Planet {
public:
    string name;
    long long int distanceFromSun;
    long long int diameter;
    long long int mass;

    Planet(string name, long long int distanceFromSun, long long int diameter, long long int mass) :
        name(name),
        distanceFromSun(distanceFromSun),
        diameter(diameter),
        mass(mass) {

    }

    void printInfo() {
        ostringstream info;
        info << this->name << " " << this->distanceFromSun << " " << this->diameter << " " << this->mass;
        cout << info.str();
    }

    long long int calculate_seconds() {
        return this->distanceFromSun / c;
    }
};

void calcMinMass(vector<Planet>& plVec) {
    long long int minMass = INT_MAX;
    for (auto n : plVec) {
        if (n.mass < minMass) {
            minMass = n.mass;
        }
    }
    cout << minMass << endl;
}

void calcMaxDiameter(vector<Planet>& plVec) {
    long long int maxDiam = INT_MIN;
    for (auto n : plVec) {
        if (n.diameter > maxDiam) {
            maxDiam = n.diameter;
        }
    }
    cout << maxDiam << endl;
}

int main()
{
    int count;
    cin >> count;
    vector<Planet> planetVec;

    for (int i = 0; i < count; i++) {
        string name;
        long long int distance, diameter, mass;
        cin >> name;
        cin >> distance >> diameter >> mass;

        Planet p(name, distance, diameter, mass);
        planetVec.push_back(p);
    }

    for (auto n : planetVec) {
        n.printInfo();
        long long int time = n.calculate_seconds();
        cout << endl;
        cout << time << endl;
    }

    calcMinMass(planetVec);
    calcMaxDiameter(planetVec);

    return 0;
}

