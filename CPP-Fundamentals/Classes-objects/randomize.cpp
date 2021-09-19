#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

using namespace std;

class Words {
    vector<string> list_words;
    

public:
    void readWords(vector<string> & words) {
        this->list_words = words;
    }
    void getRandomized(vector<string> & words) {
        unsigned seed = chrono::system_clock::now().time_since_epoch().count();
        default_random_engine e(seed);
        shuffle(begin(words), end(words), e);
        for (auto n : words) {
            cout << n << endl;
        }
    }
};

int main()
{
    string text;
    getline(cin, text);
    istringstream ssText(text);
    vector<string> words;
    string wd;
    while (ssText >> wd) {
        words.push_back(wd);
    }
    Words wordsList;
    wordsList.readWords(words);
    wordsList.getRandomized(words);

    return 0;
}

