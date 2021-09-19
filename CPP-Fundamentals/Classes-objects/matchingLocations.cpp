#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Location {
    string name;
    string latitude;
    string longitude;

public:
    Location(string name, string latitude, string longitude) :
        name(name),
        latitude(latitude),
        longitude(longitude){
    }

    
};


int main()
{
    string text;
    getline(cin, text);
    istringstream ssT(text);
    string temp;
    string n;
    string la;
    string lo;
    getline(ssT, temp, ',');
    n = temp;
    getline(ssT, temp, ',');
    la = temp;
    getline(ssT, temp, ',');
    lo = temp;


    cout << "name: " << n << " la: " << la << " lo: " << lo << endl;
    return 0;
}