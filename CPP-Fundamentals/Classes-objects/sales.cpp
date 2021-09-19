#include <iostream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

//rework it using map<town,total>
//products should be calculated separately in total

class Sale {
public:
    string town;
    string product;
    double price;
    int qty;

    map<string, double> productTot;
    map<string, double> townTotal;
    
    void getInfo() {
        string text1;
        string text2;
        double pr;
        int qt;
        cin >> text1 >> text2 >> pr >> qt;
    }

    double calcTotal(map<string, double>& productTot) {
        if (productTot.find(product) == productTot.end()) {
            productTot.insert(pair<string, double>(product, (price * qty)));
        }
        else {
            productTot[product] += (price * qty);
        }

        double total = 0;
        for (auto element : productTot) {
            total += element.second;
        }

        return total;
    }

    void fillMap(map<string, double>& townTotal) {
        if (townTotal.find(town) == townTotal.end()) {
            townTotal.insert(pair<string, double>(town, calcTotal(productTot)));
        }
        else {
            townTotal[town] += calcTotal(productTot);
        }
    }
    

    void printMap(map<string, double>& townTotal) {
        for (auto element : townTotal) {
            cout << element.first << " -> " << element.second << endl;
        }
    }
    
};

int main()
{
    //Sofia beer 1.20 160
    //Varna chocolate 2.35 86
    //Sofia coffee 0.40 853
    //Varna apple 0.86 75.44
    //Plovdiv beer 1.10 88

    int saleCount;
    cin >> saleCount;
    Sale sales;
    for (int i = 0; i < saleCount; i++) {
        sales.getInfo();
        sales.fillMap(sales.productTot);
    }

    sales.printMap(sales.townTotal);
    return 0;
}


