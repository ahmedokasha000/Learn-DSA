/// Ignoring details about the machine or compiler, which of the following functions should
///take the least amount of time on average given a collection with a large number of elements?

#include <iostream>
#include <set>

// 1.

void fn(std::set<int> & set) {
    set.insert(42);
}

// 2.

void fn(std::unordered_set<int> const& set) {
    auto result = set.find(42);
    if (result != set.end()) {
        std::cout << "found" << std::endl;
    }
}

// 3.

void fn(std::forward_list<int> list){
    list.clear();
}


// 4.

void fn(std::vector<into>& vector) {
    auto fn = [](int x) { return x + 42; };
    std::traansform(vector.begin(), vector.end(), vector.begin(), fn);
}
