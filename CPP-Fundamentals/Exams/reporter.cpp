#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>


using namespace std;

vector<string> checkDuplicates(vector<string>& vec) {

    vector<string> clearedVec;
    for (string word : vec) {
        auto it = find(clearedVec.begin(), clearedVec.end(), word);
        if (it == clearedVec.end()) {
            clearedVec.push_back(word);
        }
    }
    return clearedVec;
}


int main()
{
    int lineCount;
    cin >> lineCount;
    cin.ignore();
    vector<vector<string>> fullText;
    vector<string> remainingWords;
    vector<string> sentence;

    for (int i = 0; i < lineCount; ++i) {
        
        string textLine;
        getline(cin, textLine);
        stringstream ssText(textLine);
        string word;
        while (ssText >> word) {

            if (word == ".") {
                sentence.push_back(".");
                break;
            }

            else {

                sentence.push_back(word);
            }
        }

        if (ssText) {
            string tempWord;
            while (ssText >> tempWord) {
                remainingWords.push_back(tempWord);
            }
        }
        vector<string> clearedSentence = checkDuplicates(sentence);
        fullText.push_back(clearedSentence);
        if (i + 1 == lineCount) {
            fullText.push_back(remainingWords);
        }
        sentence.clear();

        if (!remainingWords.empty()) {
            for (int i = 0; i < remainingWords.size(); ++i) {
                sentence.push_back(remainingWords[i]);
            }
            remainingWords.clear();
        }
        
    }

    for (auto sent : fullText) {
        for (auto word : sent) {
            cout << word << " ";
        }
    }
    return 0;
}
