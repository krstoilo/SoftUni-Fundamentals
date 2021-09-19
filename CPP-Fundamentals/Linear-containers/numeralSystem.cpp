#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<char> readInput() {

    vector <char> vec(10);

    cin >> vec[0] >> vec[1] >> vec[2] >> vec[3] >> vec[4] >> vec[5] >> vec[6] >> vec[7] >> vec[8] >> vec[9];

    return vec;
}

int convertToNumeral(vector<char>& vec, string number) {

    char currentChar = ' ';
    string resultStr = " ";

    for (size_t i = 0; i < number.size(); i++) {

        currentChar = number[i];
        
        if (currentChar == vec[0]) {
            resultStr += '0';
        }
        else if (currentChar == vec[1]) {
            resultStr += '1';
        }
        else if (currentChar == vec[2]) {
            resultStr += '2';
        }
        else if (currentChar == vec[3]) {
            resultStr += '3';
        }
        else if (currentChar == vec[4]) {
            resultStr += '4';
        }
        else if (currentChar == vec[5]) {
            resultStr += '5';
        }
        else if (currentChar == vec[6]) {
            resultStr += '6';
        }
        else if (currentChar == vec[7]) {
            resultStr += '7';
        }
        else if (currentChar == vec[8]) {
            resultStr += '8';
        }
        else if (currentChar == vec[9]) {
            resultStr += '9';
        }
    }

    int result = stoi(resultStr);
    return result;
}

std::string turnToSymbol(int sum, const std::vector <char>& vec) {

    std::string convertedSum;
    std::string result;

    std::stringstream istr;

    istr << sum;

    convertedSum = istr.str();

    int SIZE = convertedSum.size();

    for (int i = 0; i < SIZE; i++) {

        if (convertedSum[i] == '0') {
            result += vec[0];
        }
        else if (convertedSum[i] == '1') {
            result += vec[1];
        }
        else if (convertedSum[i] == '2') {
            result += vec[2];
        }
        else if (convertedSum[i] == '3') {
            result += vec[3];
        }
        else if (convertedSum[i] == '4') {
            result += vec[4];
        }
        else if (convertedSum[i] == '5') {
            result += vec[5];
        }
        else if (convertedSum[i] == '6') {
            result += vec[6];
        }
        else if (convertedSum[i] == '7') {
            result += vec[7];
        }
        else if (convertedSum[i] == '8') {
            result += vec[8];
        }
        else if (convertedSum[i] == '9') {
            result += vec[9];
        }

    }

    return result;
}

int main()
{

    vector<char> input = readInput();
    string firstNum, secNum;
    cin >> firstNum >> secNum;

    int num1 = convertToNumeral(input, firstNum);
    int num2 = convertToNumeral(input, secNum);

    int sum = num1 + num2;

    cout << turnToSymbol(sum, input);
    
    return 0;
}
