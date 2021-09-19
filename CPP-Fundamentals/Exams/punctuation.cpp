#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include<map>

using namespace std;

vector<string> recordSentences(string& essayText) {
    vector<string> sentences;
    istringstream ssText(essayText);
    string newSent;
    while (getline(ssText, newSent, '|')) {
        sentences.push_back(newSent);
    }

    return sentences;
}

int countPunctSigns(string& sentence) {
    int punctCount = 0;
    for (char l : sentence) {
        if (ispunct(l)) {
            punctCount++;
        }
    }

    return punctCount;

}

void recordStatistics(map<int, int>& m, vector<string>& sentences) {
    for (int i = 0; i < sentences.size(); i++) {
        int countPunct = countPunctSigns(sentences[i]);
        m[countPunct]++;
    }
}

int main()
{
    string essayText;
    getline(cin, essayText);
    vector<string> sentences = recordSentences(essayText);
    map<int, int> statistics;
    recordStatistics(statistics, sentences);

    for (auto element : statistics) {
        cout << element.first << " symbol sentences: " << element.second << endl;
    }

    return 0;
}

