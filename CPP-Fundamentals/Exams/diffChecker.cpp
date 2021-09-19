#include <iostream>
#include <string>

using namespace std;

void compareStr(const int & strSize, string& str1, string& str2, int& diff, string& res)
{
    for (int i = 0; i < strSize; i++)
    {
        if (str1[i] == str2[i])
        {
            res += str1[i];
        }

        else if (toupper(str1[i]) == toupper(str2[i]))
        {
            res += toupper(str1[i]);
        }

        else if (str1[i] != str2[i])
        {
            res += '!';
            diff++;
        }
    }
}

int main()
{
    int strSize;
    cin >> strSize;
    cin.ignore();
    string str1;
    string str2;
    getline(cin, str1);
    getline(cin, str2);
    string result;
    int diff = 0;
    
    compareStr(strSize, str1, str2, diff, result);

    cout << result << endl;
    cout << diff << endl;

    return 0;
}

