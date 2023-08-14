// what si the output of the following code ?

#include <iostream>
#include <cctype>

template < typename Transformer >
void transform_and_print( Transformer t, std::strng str) {
    t(str);
    std::cout << str << std::endl;
}

int main() {
    auto toupper1 = [](auto str) {for (auto c: str) {c = std::toupper(c);}};
    auto toupper2 = [](auto& str) {for (auto c: str) {c = std::toupper(c);}};
    auto toupper3 = [](auto str) {for (auto& c: str) {c = std::toupper(c);}};
    auto toupper4 = [](auto& str) {for (auto& c: str) {c = std::toupper(c);}};
    transform_and_print(toupper1, "toupper1");
    transform_and_print(toupper2, "toupper2");
    transform_and_print(toupper3, "toupper3");
    transform_and_print(toupper4, "toupper4");
    
}