// what is the output of the following code ?

#include <iostream>
#define MAX(a, b)\
    a > b ? a : b
int main() {
    int a = 1, b = 2;
    int c = 3 + MAX(a, b) + 4;
    std::cout << c << std::endl;
    return 0;
}