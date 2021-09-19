#include <iostream>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

void readInput(vector<string> & words) {
    string text;
    getline(cin, text);
    istringstream ssText(text);
    string word;
    while (ssText >> word) {
        words.push_back(word);
    }
}

void fillMap(map<string, int>& wordWithCount, vector<string>& words) {
    for (int i = 0; i < words.size(); i++) {
        wordWithCount[words[i]]++;
    }
}

void printMap(map<string, int>& wordsWithCount) {
    for (auto n : wordsWithCount) {
        if (n.second % 2 != 0) {
            cout << n.first << " ";
        }
    }

    cout << endl;

    for (auto m : wordsWithCount) {
        if (m.second % 2 == 0) {
            cout << m.first << " ";
        }
    }
}


int main()
{
    vector<string> words;
    readInput(words);
    map<string, int> sortedWords;
    fillMap(sortedWords, words);
    printMap(sortedWords);

   

    return 0;
}

