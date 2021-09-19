#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool isMagic(char& symbol) {
    bool isMagic = false;
    if (symbol == 'a' || symbol == 'e' || symbol == 'o' || symbol == 'u' || symbol == 'i') {
        isMagic = true;
    }

    return isMagic;
}

void clearWord(string& word) {

    for (int i = 1; i <= word.size(); i++) {
        if (word[i - 1] == word[i] && !isMagic(word[i])) {
            word.erase(i - 1, 1);
            i--;
        }
    }
}

int main()
{
    string inputText;
    getline(cin, inputText);

    string resultString;
    istringstream ssText(inputText);
    string word;
    while (ssText >> word) {
        clearWord(word);
        resultString += word + " ";
    }
    
    cout << resultString;
    return 0;
}

