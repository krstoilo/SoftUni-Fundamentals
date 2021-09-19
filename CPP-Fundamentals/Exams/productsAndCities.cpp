#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

void getInput(map<string, double>& cityMap) {
	string cityName;
	double prQty;
	double pricePerProduct;
	double total;
	cin >> cityName;
	cin >> prQty >> pricePerProduct;
	total = prQty * pricePerProduct;
	if (cityMap.find(cityName) != cityMap.end()) {
		cityMap[cityName] += total;
	}
	else {
		cityMap[cityName] = total;
	}
}

int main()
{
	map<string, double> cities;
	int cityCount;
	cin >> cityCount;
	while (true) {
		if (cities.size() + 1 > cityCount) {
			break;
		}
		getInput(cities);
	}

	for (auto element : cities) {
		cout << element.first << " " << element.second << endl;
	}
	return 0;
}


