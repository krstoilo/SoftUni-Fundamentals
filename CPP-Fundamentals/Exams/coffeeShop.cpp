#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Coffee {
    string name;
    double price;
    double rating;

public:
    Coffee(string name, double price, double rating) :
        name(name),
        price(price),
        rating(rating) {}

    Coffee addNew() {
        string name;
        double pr;
        double rt;
        getline(cin, name);
        cin >> pr >> rt;
        cin.ignore();

        return Coffee(name, pr, rt);
    }

    string getName() {
        return this->name;
    }

    double getRating() {
        return this->rating;
    }

    double getPrice() {
        return this->price;
    }

    void setPrice(double price) {
        this->price = price;
    }

};

void changePrice(Coffee& drink) {
    double newPrice = drink.getPrice() * 0.9;
    drink.setPrice(newPrice);
}

void deleteDrink(vector<Coffee> & drinks, int& pos) {
    drinks.erase(drinks.begin() + pos);
}

void printInfo(vector<Coffee>& drinks) {

    for (auto drink : drinks)
    {
        cout << drink.getName() << " " << drink.getPrice() << endl;
    }
}

int main()
{
    vector<Coffee> drinksVec;
    int drinkCount;
    cin >> drinkCount;
    cin.ignore();

    for (int i = 0; i < drinkCount; i++) {
        Coffee drink = drink.addNew();
        drinksVec.push_back(drink);
    }

    for (int j = 0; j < drinksVec.size(); j++) {
        if (drinksVec[j].getRating() >= 4 && drinksVec[j].getRating() <= 5.99) 
        {
            changePrice(drinksVec[j]);
        }

        if (drinksVec[j].getRating() < 4)
        {
            deleteDrink(drinksVec, j);
        }
    }

    printInfo(drinksVec);

    return 0;
}


