// which of the following calls to ohai() are valid?

struct A {
    void ohai() {}
};

struct B: protected A {};

struct C: private A {
    friend int main() {}
};

struct D: B {
    void test() {
        ohai(); // 1
    }
};

struct E: C {
    void test() {
        ohai(); // 2
    }
};

int main() {
    A().ohai(); // 3
    B().ohai(); // 4 
    C().ohai(); // 5
    E().ohai(); // 6
}