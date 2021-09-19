#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int convertToDecimal(const char a, const char b) {
    int decimalA = 0;
    int decimalB = 0;
    int decimal = 0;
    
    switch (a)
    {
    case '0':
        decimalA = 0;
        break;
    case '1':
        decimalA = 1 * 16;
        break;
    case '2':
        decimalA = 2 * 16;
        break;
    case '3':
        decimalA = 3 * 16;
        break;
    case '4':
        decimalA = 4 * 16;
        break;
    case '5':
        decimalA = 5 * 16;
        break;
    case '6':
        decimalA = 6 * 16;
        break;
    case '7':
        decimalA = 7 * 16;
        break;
    case '8':
        decimalA = 8 * 16;
        break;
    case '9':
        decimalA = 9 * 16;
        break;
    case 'a':
        decimalA = 10 * 16;
        break;
    case 'b':
        decimalA = 11 * 16;
        break;
    case 'c':
        decimalA = 12 * 16;
        break;
    case 'd':
        decimalA = 13 * 16;
        break;
    case 'e':
        decimalA = 14 * 16;
        break;
    case 'f':
        decimalA = 15 * 16;
        break;
    default:
        break;
    }

    switch (b)
    {
    case '0':
        decimalB = 0;
        break;
    case '1':
        decimalB = 1;
        break;
    case '2':
        decimalB = 2;
        break;
    case '3':
        decimalB = 3;
        break;
    case '4':
        decimalB = 4;
        break;
    case '5':
        decimalB = 5;
        break;
    case '6':
        decimalB = 6;
        break;
    case '7':
        decimalB = 7;
        break;
    case '8':
        decimalB = 8;
        break;
    case '9':
        decimalB = 9;
        break;
    case 'a':
        decimalB = 10;
        break;
    case 'b':
        decimalB = 11;
        break;
    case 'c':
        decimalB = 12;
        break;
    case 'd':
        decimalB = 13;
        break;
    case 'e':
        decimalB = 14;
        break;
    case 'f':
        decimalB = 15;
        break;
    default:
        break;
    }

    decimal = decimalA + decimalB;

    return decimal;
}

void recordDecColors(string& hexCode, int& red, int& green, int& blue) {
    
    string redS;
    string greenS;
    string blueS;

    redS += hexCode[1]; redS += hexCode[2]; greenS += hexCode[3]; greenS += hexCode[4]; blueS += hexCode[5]; blueS += hexCode[6];
    
    red = convertToDecimal(redS[0], redS[1]);
    green = convertToDecimal(greenS[0], greenS[1]);
    blue = convertToDecimal(blueS[0], blueS[1]);
}

void calcHex(stack<char>& stack, int & number) {

    int quo = 0;
    int rem = 0;
    if (number == 0) {
        stack.push('0');
        stack.push('0');
    }
    else {
        while (number > 0) {
            quo = number / 16;
            rem = number % 16;
            switch (rem)
            {
            case 0:
                stack.push('0');
                break;
            case 1:
                stack.push('1');
                break;
            case 2:
                stack.push('2');
                break;
            case 3:
                stack.push('3');
                break;
            case 4:
                stack.push('4');
                break;
            case 5:
                stack.push('5');
                break;
            case 6:
                stack.push('6');
                break;
            case 7:
                stack.push('7');
                break;
            case 8:
                stack.push('8');
                break;
            case 9:
                stack.push('9');
                break;
            case 10:
                stack.push('a');
                break;
            case 11:
                stack.push('b');
                break;
            case 12:
                stack.push('c');
                break;
            case 13:
                stack.push('d');
                break;
            case 14:
                stack.push('e');
                break;
            case 15:
                stack.push('f');
                break;
            default:
                break;
            }
            number = quo;
        }
    }
}

string convertToHex(int& red, int& green, int& blue) {

    string hexCode;
    stack<char> stack;

    calcHex(stack, blue);
    calcHex(stack, green);
    calcHex(stack, red);

    while (!stack.empty()) {
        hexCode += stack.top();
        stack.pop();
    }
    
    return hexCode;
}

int main()
{
    string color1, color2;
    cin >> color1 >> color2;

    int red1, green1, blue1, red2, green2, blue2;

    recordDecColors(color1, red1, green1, blue1);
    recordDecColors(color2, red2, green2, blue2);

    int redNew, greenNew, blueNew = 0;
    redNew = (red1 + red2) / 2;
    greenNew = (green1 + green2) / 2;
    blueNew = (blue1 + blue2) / 2;

    cout << "#" << convertToHex(redNew, greenNew, blueNew) << endl;
    
    return 0;
}

