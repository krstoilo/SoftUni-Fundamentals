#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    string input_line;
    vector<string> words;
    stringstream ssLine;
    
    while (true) {
        getline(cin, input_line);
        if (input_line == "end") {
            break;
        }
        else {
            ssLine << input_line << " ";
        }   
    }
    
    string word;
    while (ssLine >> word) {
        words.push_back(word);
    }

    int lenWords = words.size();
    for (int i = lenWords-1; i >= 0; i--) {
        cout << words[i] << " ";
    }
    
    return 0;
}
