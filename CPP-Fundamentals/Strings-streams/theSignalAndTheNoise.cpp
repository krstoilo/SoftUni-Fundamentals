#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
	string line;
	getline(cin, line);
	string newLine;
	for (int i = 0; i < line.size(); i++) {
		if (line[i] == ' ' || isdigit(line[i])) {
			newLine += line[i];
		}
	}

	istringstream ssline(newLine);
	int num;
	vector<int> nums;
	while (ssline >> num) {
		nums.push_back(num);
	}

	int max = INT_MIN;
	for (auto n : nums) {
		if (n > max) {
			max = n;
		}
	}

	cout << max << endl;

	return 0;
}
