#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

class Pet {
    string name;
    int age;
    double score;
public:
    Pet(string name, int age, double score):
        name(name),
        age(age),
        score(score){}

    string getName() {
        return this->name;
    }

    double getScore() {
        return this->score;
    }

    int getAge() {
        return this->age;
    }

    void changeScore()
    {
        this->score += 2.5;
    }
};

void checkExhibition(vector<Pet>& exhibition) {

    for (int i = 0; i < exhibition.size(); i++)
    {
        if (exhibition[i].getAge() >= 12)
        {
            exhibition[i].changeScore();
        }

        if (exhibition[i].getScore() < 4)
        {
            exhibition.erase(exhibition.begin() + i);
            i--;
        }
    }
}


int main()
{
    int participants;
    cin >> participants;

    vector<Pet> exhibition;
    multimap<double, string, greater<double>> petWinners;

    for (int i = 0; i < participants; i++)
    {
        string name;
        cin >> name;
        int age;
        cin >> age;
        double score;
        cin >> score;

        Pet p1(name, age, score);
        exhibition.push_back(p1);
    }

    checkExhibition(exhibition);
    for (int i = 0; i < exhibition.size(); i++)
    {
        petWinners.insert(pair<double, string>(exhibition[i].getScore(), exhibition[i].getName()));
    }

    for (auto element : petWinners)
    {
        cout << element.second << " ";
    }

    return 0;
}


