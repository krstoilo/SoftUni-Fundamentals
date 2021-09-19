#include <iostream>
#include <string>

using namespace std;


void printAnswerIfOnes(const int number)
{
   
    switch (number)
    {
    case 0:
        cout << "zero" << " ";
        break;
    case 1:
        cout << "one" << " ";
        break;
    case 2:
        cout << "two" << " ";
        break;
    case 3:
        cout << "three" << " ";
        break;
    case 4:
        cout << "four" << " ";
        break;
    case 5:
        cout << "five" << " ";
        break;
    case 6:
        cout << "six" << " ";
        break;
    case 7:
        cout << "seven" << " ";
        break;
    case 8:
        cout << "eight" << " ";
        break;
    case 9:
        cout << "nine" << " ";
        break;
    default:
        cout << "error" << " ";
    }
}

void printAnswerIfTens(const int number)
{

    switch (number)
    {
    case 10:
        cout << "ten" << " ";
        break;
    case 11:
        cout << "eleven" << " ";
        break;
    case 12:
        cout << "twelve" << " ";
        break;
    case 13:
        cout << "thirteen" << " ";
        break;
    case 14:
        cout << "fourteen" << " ";
        break;
    case 15:
        cout << "fifteen" << " ";
        break;
    case 16:
        cout << "sixteen" << " ";
        break;
    case 17:
        cout << "seventeen" << " ";
        break;
    case 18:
        cout << "eighteen" << " ";
        break;
    case 19:
        cout << "nineteen" << " ";
        break;
    default:
        cout << "error" << " ";
    }
}

void printAnswerIfTensll(const string number)
{

    switch (number[0])
    {
    case '2':
        cout << "twenty" << " ";
        break;
    case '3':
        cout << "thirty" << " ";
        break;
    case '4':
        cout << "forty" << " ";
        break;
    case '5':
        cout << "fifty" << " ";
        break;
    case '6':
        cout << "sixty" << " ";
        break;
    case '7':
        cout << "seventy" << " ";
        break;
    case '8':
        cout << "eighty" << " ";
        break;
    case '9':
        cout << "ninety" << " ";
        break;
    default:
        cout << "error" << " ";
    }

    switch (number[1])
    {
    case '1':
        cout << "one" << " ";
        break;
    case '2':
        cout << "two" << " ";
        break;
    case '3':
        cout << "three" << " ";
        break;
    case '4':
        cout << "four" << " ";
        break;
    case '5':
        cout << "five" << " ";
        break;
    case '6':
        cout << "six" << " ";
        break;
    case '7':
        cout << "seven" << " ";
        break;
    case '8':
        cout << "eight" << " ";
        break;
    case '9':
        cout << "nine" << " ";
        break;
    default:
        cout << "" << " ";
    }
}

void printAnswerIfHundreds (const string number)
{

    switch (number[0])
    {
    case '1':
        cout << "one hundred" << " ";
        break;
    case '2':
        cout << "two hundred" << " ";
        break;
    case '3':
        cout << "three hundred" << " ";
        break;
    case '4':
        cout << "four hundred" << " ";
        break;
    case '5':
        cout << "five hundred" << " ";
        break;
    case '6':
        cout << "six hundred" << " ";
        break;
    case '7':
        cout << "seven hundred" << " ";
        break;
    case '8':
        cout << "eight hundred" << " ";
        break;
    case '9':
        cout << "nine hundred" << " ";
        break;
    default:
        cout << "";
    }

    switch (number[1])
    {
    case '2':
        cout << "twenty" << " ";
        break;
    case '3':
        cout << "thirty" << " ";
        break;
    case '4':
        cout << "forty" << " ";
        break;
    case '5':
        cout << "fifty" << " ";
        break;
    case '6':
        cout << "sixty" << " ";
        break;
    case '7':
        cout << "seventy" << " ";
        break;
    case '8':
        cout << "eighty" << " ";
        break;
    case '9':
        cout << "ninety" << " ";
        break;
    default:
        cout << "";
    }

    switch (number[2])
    {
    case '1':
        cout << "one" << " ";
        break;
    case '2':
        cout << "two" << " ";
        break;
    case '3':
        cout << "three" << " ";
        break;
    case '4':
        cout << "four" << " ";
        break;
    case '5':
        cout << "five" << " ";
        break;
    case '6':
        cout << "six" << " ";
        break;
    case '7':
        cout << "seven" << " ";
        break;
    case '8':
        cout << "eight" << " ";
        break;
    case '9':
        cout << "nine" << " ";
        break;
    default:
        cout << "";
    }
}

void printAnswerIfThousands(const string number)
{

    switch (number[0])
    {
    case '1':
        cout << "one thousand" << " ";
        break;
    case '2':
        cout << "two thousand" << " ";
        break;
    case '3':
        cout << "three thousand" << " ";
        break;
    case '4':
        cout << "four thousand" << " ";
        break;
    case '5':
        cout << "five thousand" << " ";
        break;
    case '6':
        cout << "six thousand" << " ";
        break;
    case '7':
        cout << "seven thousand" << " ";
        break;
    case '8':
        cout << "eight thousand" << " ";
        break;
    case '9':
        cout << "nine thousand" << " ";
        break;
    default:
        cout << "";
    }

    switch (number[1])
    {
    case '1':
        cout << "one hundred" << " ";
        break;
    case '2':
        cout << "two hundred" << " ";
        break;
    case '3':
        cout << "three hundred" << " ";
        break;
    case '4':
        cout << "four hundred" << " ";
        break;
    case '5':
        cout << "five hundred" << " ";
        break;
    case '6':
        cout << "six hundred" << " ";
        break;
    case '7':
        cout << "seven hundred" << " ";
        break;
    case '8':
        cout << "eight hundred" << " ";
        break;
    case '9':
        cout << "nine hundred" << " ";
        break;
    default:
        cout << "";
    }

    switch (number[2])
    {
    case '2':
        cout << "twenty" << " ";
        break;
    case '3':
        cout << "thirty" << " ";
        break;
    case '4':
        cout << "forty" << " ";
        break;
    case '5':
        cout << "fifty" << " ";
        break;
    case '6':
        cout << "sixty" << " ";
        break;
    case '7':
        cout << "seventy" << " ";
        break;
    case '8':
        cout << "eighty" << " ";
        break;
    case '9':
        cout << "ninety" << " ";
        break;
    default:
        cout << "";
    }

    switch (number[3])
    {
    case '1':
        cout << "one" << " ";
        break;
    case '2':
        cout << "two" << " ";
        break;
    case '3':
        cout << "three" << " ";
        break;
    case '4':
        cout << "four" << " ";
        break;
    case '5':
        cout << "five" << " ";
        break;
    case '6':
        cout << "six" << " ";
        break;
    case '7':
        cout << "seven" << " ";
        break;
    case '8':
        cout << "eight" << " ";
        break;
    case '9':
        cout << "nine" << " ";
        break;
    default:
        cout << "";
    }
}

int main()
{

    int number;
    cin >> number;

    string numberStr = to_string(number);

    if (number <= 9 && number >= 0)
    {
        printAnswerIfOnes(number);
    }

    else if (number >= 10 && number <= 19)
    {
        printAnswerIfTens(number);
    }

    else if (number >= 20 && number <= 99)
    {
        printAnswerIfTensll(numberStr);
    }

    else if (number >= 100 && number <= 999)
    {
        printAnswerIfHundreds(numberStr);
    }

    else if (number >= 1000 && number <= 9999)
    {
        printAnswerIfThousands(numberStr);
    }

    return 0;
}

