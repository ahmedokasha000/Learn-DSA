import sys
from pathlib import Path
script_path = Path(__file__).parent.parent
sys.path.append(f"{script_path}")

from my_datastructures.single_linked_list import SingleLinkedList, Node


class Stack:
    """
    Stack implementation with single linked list.
    """
    def __init__(self):
        self._size = 0
        self._list = SingleLinkedList()
        pass

    def push(self, value):
        self._list.prepend(value)
        self._size += 1

    def pop(self):
        if not self.is_empty():
            res = self._list.head.value
            self._list.head = self._list.head.next
            self._size -= 1
            return res
        else:
            raise IndexError("Poping from an empty stack")
    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self._size < 1

    def top(self):
        if not self.is_empty():
            return self._list.head.value
        else:
            raise IndexError("Toping from an empty stack")
class StackArr:
    def __init__(self, capacity=10):
        self._last_ind = -1
        self._arr = [0] * capacity

    def push(self, value):
        self._last_ind += 1
        if self.is_full():
            self.stretch()
        self._arr[self._last_ind] = value

    def pop(self):
        if self._last_ind > -1:
            res = self._arr[self._last_ind]
            self._last_ind -= 1
            return res
        else:
            raise IndexError("Trying to pop from empty stack")

    @property
    def size(self):
        return self._last_ind + 1

    def top(self):
        return self._arr[self._last_ind]

    def is_empty(self):
        return self._last_ind == -1

    def is_full(self):
        return self._last_ind == len(self._arr)

    def stretch(self):
        # print("stretching stack")
        self._arr = self._arr + [0] * len(self._arr)


class StackPy:
    """
    Stack implementation with python lists.
    """
    def __init__(self):
        self._list = []

    def push(self, value):
        self._list.append(value)

    def pop(self):
        if not self.is_empty():
            return self._list.pop()

        else:
            raise IndexError("Poping from an empty stack")

    def size(self):
        return len(self._list)

    def is_empty(self):
        return len(self._list) < 1

    def top(self):
        if not self.is_empty():
            return self._list[-1]
        else:
            raise IndexError("Toping from an empty stack")

def main():
    stack1 = Stack()
    for val in range(10):
        print(stack1.size)
        stack1.push(val)

    for val in range(10):
        print(stack1.pop())
        # stack1.push(val)

if __name__ == '__main__':
    main()