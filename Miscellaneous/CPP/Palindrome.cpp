#include <iostream>
int main() {
    int num, originalNum, reversedNum = 0;
    std::cout << "Enter a number: ";
    std::cin >> num;
    originalNum = num;
    while (num > 0) {
        int digit = num % 10;
        reversedNum = reversedNum * 10 + digit;
        num /= 10;
    }
    if (originalNum == reversedNum) {
        std::cout << originalNum << " is a palindrome.\n";
    } else {
        std::cout << originalNum << " is not a palindrome.\n";
    }
    return 0;
}

    

    


  

