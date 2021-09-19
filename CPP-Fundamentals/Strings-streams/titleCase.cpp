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

    string line = readLine();

    for (int i = 1; i < line.size(); i++) {
        line[0] = toupper(line[0]);
        if (isalpha(line[i - 1]) == false) {
            line[i] = toupper(line[i]);
        }
    }

    cout << line << endl;

    return 0;
}
