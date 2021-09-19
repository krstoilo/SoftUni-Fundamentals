#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <unordered_map>

using namespace std;

vector<string> readInput() {

    vector<string> wordsVec;
    string inputLine;
    getline(cin, inputLine);
    istringstream ssLine(inputLine);
    string word;
    while (ssLine >> word) {
        wordsVec.push_back(word);
    }
    
    for (int i = 0; i < wordsVec.size(); i++) {
        for (int j = 0; j < wordsVec[i].size(); j++) {
            wordsVec[i][j] = tolower(wordsVec[i][j]);
        }
    }
    return wordsVec;

}

void mapWords(unordered_map<string, int>& map, vector<string> & words) {

    for (int i = 0; i < words.size(); i++) {
        map[words[i]]++;
    }

}


int main()
{
    vector<string> input = readInput();
    unordered_map<string, int> entries;

    mapWords(entries, input);

    for (pair <string, int> element : entries) {
        if (element.second % 2 != 0) {
            cout << ", " << element.first;
        }
    }

    return 0;
}


