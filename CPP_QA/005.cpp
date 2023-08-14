// what is the output of the following code ?

#include <iostream>
#include <memory>


struct Base {
    Base() { f("Base::ctor");}
    virtual ~Base() { f("Base::dtor"); }
    virtual void f(char const* msg) { std::cout << msg << ": Base\n"; }
    void g() const { return f("Base::g"); }
};

struct Derived: Base {
    Derived() { f("Derived::ctor"); }
    ~Derived() { f("Derived::dtor"); }
    void f(char const* msg) const { std::cout << msg << ": Derived\n"; }
    void g() const { return f("Derived::g"); }
};

int main() {
    std::unique_ptr<Base> b(new Derived());
    b->g();
    return 0;
}