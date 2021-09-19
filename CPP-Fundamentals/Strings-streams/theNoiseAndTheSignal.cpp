#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm> 

using namespace std;


int main()
{
	string line;
	getline(cin, line);
	string newLine;
	for (int i = 0; i < line.size(); i++) {
		if (line[i] == ' ' || isdigit(line[i]) == false) {
			newLine += line[i];
		}
	}

	int counter = 0;
	for (int j = 0; j < newLine.size(); j++) {
		if (newLine[j] == ' ') {
			counter++;
		}
	}


	if (newLine.size() == counter) {
		cout << "no noise" << endl;
	}

	else {
		istringstream ssLine(newLine);
		vector<string> words;
		string currWord;
		while (ssLine >> currWord) {
			words.push_back(currWord);
		}
		
		sort(words.begin(), words.end());

		cout << words[0] << " " << words[1] << " " << words[2] << endl;
	}

	return 0;
}