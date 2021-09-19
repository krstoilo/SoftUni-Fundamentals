#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
	int commandCount;
	cin >> commandCount;
	cin.ignore();

	vector<string> pepiCustomers;
	vector<int> pepiMins;
	vector<string> mimiCustomers;
	vector<int> mimiMins;
	

	for (int i = 0; i < commandCount; i++) {
		string command;
		getline(cin, command);
		istringstream ssCom(command);
		string sister, customer;
		int minutesForProcess;
		ssCom >> sister;
		ssCom >> customer;
		ssCom >> minutesForProcess;
		if (sister == "Pepi") {
			pepiCustomers.push_back(customer);
			pepiMins.push_back(minutesForProcess);
		}
		else {
			mimiCustomers.push_back(customer);
			mimiMins.push_back(minutesForProcess);
		}
	}

	int timeT;
	int count = 0;
	cin >> timeT;

	while (true) {
		if (count >= timeT) {
			break;
		}
		if (pepiCustomers.empty()) {
			cout << "Pepi Idle" << endl;
		}
		else if (pepiMins[0] -1 == 0) {
			cout << "Pepi processing " << pepiCustomers[0] << endl;
			pepiMins.erase(pepiMins.begin(), pepiMins.begin() + 1);
			pepiCustomers.erase(pepiCustomers.begin(), pepiCustomers.begin() + 1);
		}
		else if (pepiMins[0] - 1 > 0) {
			cout << "Pepi processing " << pepiCustomers[0] << endl;
			pepiMins[0] -= 1;
		}
		

		if (mimiCustomers.empty()) {
			cout << "Mimi Idle" << endl;
		}
		else if (mimiMins[0] - 1 == 0) {
			cout << "Mimi processing " << mimiCustomers[0] << endl;
			mimiMins.erase(mimiMins.begin(), mimiMins.begin() + 1);
			mimiCustomers.erase(mimiCustomers.begin(), mimiCustomers.begin() + 1);
		}
		else if (mimiMins[0] - 1 > 0) {
			cout << "Mimi processing " << mimiCustomers[0] << endl;
			mimiMins[0] -= 1;
		}
		
		count++;
	}
		return 0;
}

