#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>

using namespace std;


int main()
{
    unordered_map<string, int> treasures;

    while (true) {
        string word;
        int num;
        pair<string, int> mapPair;
        cin >> word;
        if (word == "stop") {
            break;
        }
        else {
            cin >> num;
        }
        mapPair.first = word;
        mapPair.second = num;
        if (treasures.find(word) != treasures.end()) {
            treasures[word] += num;
        }
        else {
            treasures.insert(mapPair);
        }
       
    }

    for (auto element : treasures) {
        cout << element.first << " -> " << element.second << endl;
    }
    return 0;
}

