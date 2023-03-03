class MaxHeap:
    def __init__(self):
        self._heap = []
        self._size = 0

    @property
    def size(self):
        return self._size

    def _parent_index(self, index):
        return (index - 1 ) // 2

    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _percolate_up(self, index):
        while index > 0 and self._heap[index] > self._heap[self._parent_index(index)]:
            self._heap[index], self._heap[self._parent_index(index)] = self._heap[self._parent_index(index)], self._heap[index]
            index = self._parent_index(index)

    def _percolate_down(self, index):
        max_index = index
        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)

        if left_index < self._size and self._heap[max_index] < self._heap[left_index]:
            max_index = left_index
        if right_index < self._size and self._heap[max_index] < self._heap[right_index]:
            max_index = right_index
        if max_index != index:
            self._heap[index], self._heap[max_index] = self._heap[max_index], self._heap[index]
            self._percolate_down(max_index)

    def insert(self, value):
        self._heap.append(value)
        self._size += 1
        self._percolate_up(self._size - 1)


    def extract_max(self):
        if self._size == 0:
            raise Exception('Trying to extract from empty heap.')

        value = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._size -= 1
        self._heap.pop()
        self._percolate_down(0)
        return value


def main():
    max_heap = MaxHeap()
    for i in range(10):
        max_heap.insert(i)
    for i in range(10):
        print(max_heap.extract_max())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
