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
    string expression = readLine();
    int count_open = 0;
    int count_close = 0;
    
    for (int i = 0; i < expression.size(); i++) {
        if (expression[i] == '(') {
            count_open += 1;
        }
        else if (expression[i] == ')') {
            count_close += 1;
        }
    }

    if (count_open == count_close) {
        cout << "correct" << endl;
    }
    else {
        cout << "incorrect" << endl;
    }
    return 0;
}
