// which of the following compiles correctly?

#include <iostream>
#include <memory>
#include <string>
//1. 
void fn(std::unique_ptr<std::string> const& ptr) {
    (*ptr)+="!";
}


//2. 
struct some_class {
    const int x;
    some_class(const int y) {
        x = y;
    }
};


//3. 
void fn(const char* ptr) {
    ptr = "string";
}

//4.
std::size_t gn (std::vector<std::string> const& v) {
    v.reserve(100);
    return v.size();
}