#include <iostream>

int sum_of_two_digits(int first, int second) {
    return first + second;
}

int main() {
    int a = 0;
    int b = 0;
    std::cin >> a >> b;
    std::cout << sum_of_two_digits(a, b);
    return 0;
}