#include <iostream>
#include <string>

using namespace std;

string readArray() {

    string arr = "";
    getline(cin, arr);
    return arr;
}
    
bool compareArrays(const string& arr1, const string& arr2) {

    bool areEqual = false;
        if (arr1 == arr2) {
        areEqual = true;
    }
        return areEqual;
}


int main()
{
    string arr1 = readArray();
    string arr2 = readArray();

    if (compareArrays(arr1, arr2)) {
        cout << "equal" << endl;
    }
    else {
        cout << "not equal" << endl;
    }

    return 0;
}

