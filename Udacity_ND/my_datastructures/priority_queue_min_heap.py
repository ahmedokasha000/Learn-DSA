class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._size = 0

    @property
    def size(self):
        return self._size

    def _parent_ind(self, ind):
        return (ind - 1) // 2

    def _left_child_ind(self, ind):
        return 2 * ind + 1

    def _right_child_ind(self, ind):
        return 2 * ind + 2

    def get_min(self):
        if self._size == 0:
            raise Exception("Priority queue is empty.")
        return self._heap[0]

    def insert(self, x):
        self._heap.append(x)
        self._size += 1
        self._percolate_up(self._size - 1)

    def _percolate_up(self, ind):
        while ind > 0 and self._heap[ind] < self._heap[self._parent_ind(ind)]:
            self._heap[ind], self._heap[self._parent_ind(ind)] = self._heap[self._parent_ind(ind)], self._heap[ind]
            ind = self._parent_ind(ind)

    def extract_min(self):
        if self._size == 0:
            raise Exception("Priority queue is empty.")
        min_val = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._size -= 1
        self._heap.pop()
        self._percolate_down(0)
        return min_val

    def _percolate_down(self, ind):
        min_index = ind
        lchild_ind = self._left_child_ind(ind)
        if lchild_ind < self._size and self._heap[lchild_ind] < self._heap[min_index]:
            min_index = lchild_ind
        rchild_ind = self._right_child_ind(ind)
        if rchild_ind < self._size and self._heap[rchild_ind] < self._heap[min_index]:
            min_index = rchild_ind
        if ind != min_index:
            self._heap[ind], self._heap[min_index] = self._heap[min_index], self._heap[ind]
            self._percolate_down(min_index)


def main():
    min_heap = PriorityQueue()
    min_heap.insert(5)
    min_heap.insert(7)
    min_heap.insert(8)
    min_heap.insert(1)

    while min_heap.size > 0:
        print(min_heap.extract_min())


if __name__ == '__main__':
    main()
