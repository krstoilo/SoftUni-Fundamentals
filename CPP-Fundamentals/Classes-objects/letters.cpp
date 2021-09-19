#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

void fillSet(set<string>& words, char& letter, istringstream& ssText) {
    string word;
    while (ssText >> word) {
        word.erase(remove(word.begin(), word.end(), '.'), word.end());
        for (int i = 0; i < word.size(); i++) {
            if (word[i] == toupper(letter) || word[i] == tolower(letter)) {
                words.insert(word);
            }
        }
    }
}

int main()
{
    string text;
    getline(cin, text);
    
    
    char letterToFind;
    cin >> letterToFind;
    while (letterToFind != '.') {
        istringstream ssText(text);
        set<string> words;
        fillSet(words, letterToFind, ssText);
        for (auto n : words) {
            cout << n << " ";
        }
        cin >> letterToFind;
    }

    
    return 0;
}

