#include <iostream>
#include <vector>
#include <string>
#include <algorithm> 

using namespace std;

class Car {
private:
    string make = "";
    int year = 0;
    double price = 0.0;
public:
    Car() {
        make = "N/A";
        year = 0;
        price = 0.0;
    }
    
    void setMake(string make) {
        this->make = make;
    }

    void SetYear(int year) {
        if (year < 1950 || year > 2019)
        {
            year = 2000;
        }

        this->year = year;
    }

    void setPrice(double price) {
        if (price <= 0)
        {
            price = 1000;
        }

        this->price = price;
    }

    string getMake() {
        return this->make;
    }

    int getYear() {
        return this->year;
    }

    double getPrice() {
        return this->price;
    }

    void printCarInfo() {
        cout << "Make: " << this->make << endl;
        cout << "Year: " << this->year << endl;
        cout << "Price: " << this->price << endl;
    }
};

class AutoHouse {
private:
    double initialCapital = 0;
    double overcharge = 0;
public:
    AutoHouse() {
        initialCapital = 0.0;
        overcharge = 0.0;
        carStorage.clear();
    }

    vector<Car> carStorage;

    void setCapital(double initialCapital) {
        if (initialCapital <= 0) {
            initialCapital = 10000;
        }

        this->initialCapital = initialCapital;
    }
    
    void setOvercharge(double overcharge) {
        if (overcharge <= 0) {
            overcharge = 500;
        }

        this->overcharge = overcharge;
    }

    double getInitialCapital() {
        return this->initialCapital;
    }

    double getOverccharge() {
        return this->overcharge;
    }

    void showCars() {
        for (auto n : carStorage) {
            n.printCarInfo();
        }
    }
    
    void buyCar() {
        string make;
        int year;
        double price;
        cin >> make >> year >> price;

        Car carObj;
        carObj.setMake(make);
        carObj.SetYear(year);
        carObj.setPrice(price);

        if (initialCapital >= price) {
            initialCapital -= carObj.getPrice();
            carStorage.push_back(carObj);
        }
    }

    void sellCars() {
        cout << "Capital before sell : " << this->initialCapital << endl;
        while (!carStorage.empty()) {
            this->initialCapital += carStorage[0].getPrice() + this->overcharge;
            carStorage.erase(carStorage.begin());
        }
        cout << "Capital after sell: " << this->initialCapital << endl;
    }
};

void Menu() {

    double initialCapital = 0;
    double overCharge = 0;
    int menuChoice = -1;

    bool exitMenu = false;
    vector<int> choiceVec;

    cin >> initialCapital;
    cin >> overCharge;
    AutoHouse houseObj;
    houseObj.setCapital(initialCapital);
    houseObj.setOvercharge(overCharge);

    while (!exitMenu) {
        cin >> menuChoice;
        switch (menuChoice)
        {
        case 0:
        {
            exitMenu = true;
        }
        break;
        case 1:
        case 2:
        case 3:
        {
            choiceVec.push_back(menuChoice);
        }
        break;

        default:
            break;

        }

    }

    sort(choiceVec.begin(),choiceVec.end(), greater<int>());

    for (unsigned int i = 0; i < choiceVec.size(); i++)
    {
        switch (choiceVec.at(i))
        {
        case 1:
        {
            houseObj.showCars();
        }
        break;

        case 2:
        {
            houseObj.sellCars();
        }
        break;

        case 3:
        {
            houseObj.buyCar();
        }
        break;

        default:
            break;
        }
    }
    
}
int main()
{
    Menu();
    return 0;
}

