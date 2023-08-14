// what is the output of the following program?

#include <iostream>
#include <map>
#include <string>

using namespace std;

void f(map<string, int> map) {
    map["bar"] = 3;
}

int main() {
    map<string, int> map;
    map["foo"] = 5;
    f(map);
    map["baz"] = map["foo"] + map["qux"];
    for (auto i: map) {
        cout << i.first << " " << i.second << endl;
    }

    cout << map["bar"] << endl;
    return 0;
}