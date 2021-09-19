#include <iostream>
#include <string>

using namespace std;

int main()
{
    int wordLen;
    cin >> wordLen;

    string word1, word2;
    cin >> word1 >> word2;
    int diff = 0;
    int digitSum = 0;
    string newWord;

    for (int i = 0; i < wordLen; i++) {
        if (isdigit(word1[i])) {
            digitSum += int(word1[i]) - 48;
        }

        if (isdigit(word2[i])) {
            digitSum += int(word2[i]) - 48;
        }

        if (word1[i] == word2[i]) {
            newWord += word1[i];
        }

        else if (toupper(word1[i]) == toupper(word2[i]) || tolower(word2[i]) == tolower(word1[i])) {
            newWord += toupper(word1[i]);
        }

        else {
            newWord += "#";
            diff++;
        }
    }

    cout << newWord << endl;
    cout << diff << endl;
    cout << wordLen - diff << endl;
    cout << digitSum << endl;

    return 0;
}

