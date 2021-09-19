#include <iostream>
#include <string>

using namespace std;

string readLine() {

	string line;
	getline(cin, line);
	return line;
}


int main()
{
	string line = readLine();
	string find, replace;
	cin >> find >> replace;

	int index = 0;
	while (true) {
		if (line.find(find, index) == string::npos) {
			break;
		}
		line.replace(line.find(find, index), find.size(), replace);
		index += line.find(find, index);
	}
	
	cout << line << endl;

	return 0;
}