#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
    int shoppingList;
    cin >> shoppingList;
    double finalSum = 0;

    multimap <double, string, greater<double>> shoppingItems;
    

    for (int i = 0; i < shoppingList; i++) {
        string item;
        double price;
        int count;
        cin >> item >> price >> count;
        double productSum = price * count;
        finalSum += productSum;
        shoppingItems.insert(pair<double, string>(productSum, item));
    }

    cout << "The total sum is: " << finalSum << " lv." << endl;

    for (auto element : shoppingItems) {
        cout << element.second << " " << element.first << endl;
    }

    return 0;
}