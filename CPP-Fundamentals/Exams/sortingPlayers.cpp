#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
    map <string, int> playerScores;
    string command;
    cin >> command;
    
    while (command != "End") {
        string name = command;
        int victories;
        int losses;
        cin >> victories >> losses;
        int finalScore = victories - losses;

        if (playerScores.find(name) != playerScores.end())
        {
            playerScores[name] += finalScore;
        }

        else
        {
            playerScores[name] = finalScore;
        }

        cin >> command;
    }

    for (auto element : playerScores) {
        cout << element.first << " " << element.second << endl;
    }

    return 0;
}
