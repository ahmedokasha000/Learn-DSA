class QueueArr:
    def __init__(self, capacity=10):
        self._last_ind = -1
        self._first_ind = -1
        self._arr = [0] * capacity
        self._initial_cap = capacity

    def enqueue(self, value):
        self._last_ind += 1
        if self.is_full():
            self.stretch()
        self._arr[self._last_ind] = value

    def dequeue(self):
        # print(f" dequeueing, first_ind = {self._first_ind} , len = {len(self._arr)}")
        if self._first_ind < self._last_ind:
            self._first_ind += 1
            res = self._arr[self._first_ind]
            if (self._first_ind > int(len(self._arr) /2)-1 and len(self._arr) > self._initial_cap):
                print(f" squeeze, first_ind = {self._first_ind} , len = {len(self._arr)}")

                self.squeeze()
            return res
        else:
            raise IndexError("Trying to dequeue from empty queue")

    @property
    def size(self):
        return self._last_ind - self._first_ind

    def top(self):
        return self._arr[self._last_ind]

    def is_empty(self):
        return self._last_ind == -1

    def is_full(self):
        return self._last_ind >= len(self._arr)

    def stretch(self):
        print("stretching queue")
        self._arr = self._arr + [0] * len(self._arr)

    def squeeze(self):
        print("squeeze queue")

        last_del_ind = int(len(self._arr) /2)
        self._first_ind -= last_del_ind
        self._last_ind -= last_del_ind
        self._arr = self._arr[last_del_ind:]


def main():
    queue1 = QueueArr()
    for val in range(40):
        queue1.enqueue(val)
        # print(queue1._arr)

    print("dequeue started")
    for val in range(40):
        # queue1.dequeue()
        print(queue1.dequeue())
        # print(queue1._arr)


if __name__ == '__main__':
    main()