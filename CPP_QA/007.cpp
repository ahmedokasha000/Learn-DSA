// What is the output of the following code?

struct parent { virtual ~parent(){}};
struct child1: parent {};
struct child2: parent {};
struct grandchild1: child1 {};

grandchild1 obj;
parent *parent_ptr = &obj;
child1 *c1_ptr = dynamic_cast<child1 *>(parent_ptr);
child2 *c2_ptr = dynamic_cast<child2 *>(parent_ptr);
grandchild1 *gc1_ptr = dynamic_cast<grandchild1 *>(parent_ptr);
std::cout << std::boolalpha << (c1_ptr == nullptr)
          << ' ' << (c2_ptr == nullptr)
          << ' ' << (gc1_ptr == nullptr) << '\n';