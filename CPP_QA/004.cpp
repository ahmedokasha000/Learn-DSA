// Assume that functions f and g, as well as T's constructor, may throw an exception, but nothing else.
// Which of the following snippets are guaranteed not to leak memory,regardless of whether of an exception is thrown?

#include <memory>

// 1.
f(std::shared_ptr<T>(new T()), g());

// 2.

auto p = std::shared_ptr<T>(new T());


// 3.

T* p = new T();
f();
delete p;


// 4.

f(std::make_shared<T>(), g());