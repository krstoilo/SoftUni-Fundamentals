#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

int sumNumbers(std::vector <int> vec) {

    int sum = 0;

    for (int number : vec) {

        sum += number;
    }

    return sum;
}


std::vector <int> extractNums(std::string lineStr) {


    std::istringstream istrLine(lineStr);
    std::vector <int> numbers;
    int foundNumb;
    std::string foundWords;

    while (!istrLine.eof()) {

        istrLine >> foundWords;
        if (std::stringstream(foundWords) >> foundNumb) {

            numbers.push_back(foundNumb);
            foundWords = "";
        }
    }

    return numbers;

}


int main() {

    std::string line;
    getline(std::cin, line);

    std::vector <int> numbers = extractNums(line);

    std::cout << sumNumbers(numbers) << std::endl;

    std::istringstream lineStrm(line);
    std::string words;
    std::string printWord;

    while (lineStrm >> words) {

        if (isalpha(words[0])) {

            printWord += words + " ";
        }
    }

    std::cout << printWord;

    return 0;
}
