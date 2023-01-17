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
def main():
    stack1 = StackArr()
    for val in range(50):
        # print(stack1.size)
        stack1.push(val)



if __name__ == '__main__':
    main()