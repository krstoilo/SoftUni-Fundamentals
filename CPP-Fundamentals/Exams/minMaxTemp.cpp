#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
    map<string, vector<double>> minMaxTemps;
    int mapSize;
    cin >> mapSize;
    int cityCount = 0;

    while (cityCount < mapSize) {
        string city;
        double minTemp;
        double maxTemp;
        cin >> city >> minTemp >> maxTemp;
        if (minMaxTemps.find(city) != minMaxTemps.end()) {
            if (minTemp < minMaxTemps[city][0]) {
                minMaxTemps[city][0] = minTemp;
            }

            if (maxTemp > minMaxTemps[city][1]) {
                minMaxTemps[city][1] = maxTemp;
            }
        }
        else {
                minMaxTemps[city].push_back(minTemp);
                minMaxTemps[city].push_back(maxTemp);
                cityCount++;
        
        }
    }


    for (auto element : minMaxTemps) {
        cout << element.first << " " << element.second[0] << " " << element.second[1] << endl;
    }

    return 0;
}


