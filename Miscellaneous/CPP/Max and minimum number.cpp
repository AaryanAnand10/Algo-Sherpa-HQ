#include <iostream>
#include <climits>  // for INT_MAX and INT_MIN

int main() {
    int n;  // number of elements
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    int num;
    int max = INT_MIN;  // initialize max to smallest possible integer
    int min = INT_MAX;  // initialize min to largest possible integer

    for (int i = 0; i < n; ++i) {
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> num;

        // Update max and min
        if (num > max) {
            max = num;
        }
        if (num < min) {
            min = num;
        }
    }

    std::cout << "Maximum number: " << max << std::endl;
    std::cout << "Minimum number: " << min << std::endl;

    return 0;
}
