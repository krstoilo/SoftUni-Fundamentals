#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>

using namespace std;

int main()
{
    string text;
    getline(cin, text);
    string word;
    istringstream ssText(text);
    vector<string> wordsFromText;
    while (ssText >> word) {
        for (int i = 0; i < word.size(); i++) {
            word[i] = tolower(word[i]);
        }
        wordsFromText.push_back(word);
    }
    set<string> wordList;

    for (auto n : wordsFromText) {
        if (n.size() < 5) {
            wordList.insert(n);
        }
    }

    for (auto m : wordList) {
        if (wordList.find(m) == wordList.begin()) {
            cout << m ;
        }
        else {
            cout << ", " << m;
        }
    }



    return 0;
}

