#include <iostream>
#include <string>
#include <deque>
#include <sstream>
#include <map>

using namespace std;

int main()
{
    int commandRows;
    cin >> commandRows;
    cin.ignore();

    map<string, deque<int>> garbageCollection;
    int materialID = 0;

    for (int i = 0; i < commandRows; i++) {
        string command;
        getline(cin, command);
        istringstream ssText(command);
        string material;
        string position;
        ssText >> material;
        ssText >> position;
        if (material == "glass") {
            materialID++;
            if (garbageCollection.find(material) != garbageCollection.end()) {
                if (position == "front") {
                    garbageCollection[material].push_front(materialID);
                }
                else if (position == "back") {
                    garbageCollection[material].push_back(materialID);
                }
            }
            else {
                garbageCollection[material].push_front(materialID);
            }
        }
        else if (material == "metal") {
            materialID++;
            if (garbageCollection.find(material) != garbageCollection.end()) {
                if (position == "front") {
                    garbageCollection[material].push_front(materialID);
                }
                else if (position == "back") {
                    garbageCollection[material].push_back(materialID);
                }
            }
            else {
                garbageCollection[material].push_front(materialID);
            }
        }
        else if (material == "plastic") {
            materialID++;
            if (garbageCollection.find(material) != garbageCollection.end()) {
                if (position == "front") {
                    garbageCollection[material].push_front(materialID);
                }
                else if (position == "back") {
                    garbageCollection[material].push_back(materialID);
                }
            }
            else {
                garbageCollection[material].push_front(materialID);
            }
        }
    }

    for (auto element : garbageCollection) {
        cout << element.first << " - ";
        for (auto id : element.second) {
            cout << id << " ";
        }
        cout << endl;
    }
   
    return 0;
}


