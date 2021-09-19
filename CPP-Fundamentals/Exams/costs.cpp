#include <iostream>
#include <string>

using namespace std;

int main()
{
    double waterCons;
    double gasCons;
    double dailyEnergy;
    double rent;
    double nightEnergy;
    double motherSalary;
    double fatherSalary;

    cin >> waterCons >> gasCons >> dailyEnergy >> rent >> nightEnergy >> motherSalary >> fatherSalary;

    double total_salary = motherSalary + fatherSalary;
    double water_monthly = waterCons * 1.65;
    double gas_monthly = gasCons * 0.09;
    double energy_monthly = (dailyEnergy * 0.13) + (nightEnergy * 0.07);
    double all_costs = water_monthly + gas_monthly + energy_monthly + rent + 40;
    double remaining_salary = total_salary - all_costs;
    double moneyForDay = remaining_salary / 30;

    cout << "Water : " << water_monthly << endl << "Gas : " << gas_monthly << endl << "Energy : " << energy_monthly << endl << "All costs : " << all_costs << endl;
    
    if (remaining_salary <= 0) {
        cout << "Remaining Salary : " << remaining_salary << endl << "You should find new job !" << endl << "Money for one day : " << moneyForDay << endl;
    }

    else {
        cout << "Remaining Salary : " << remaining_salary << endl << "Money for one day : " << moneyForDay << endl;
    }
    return 0;
}


