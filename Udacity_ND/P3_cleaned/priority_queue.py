from typing import Optional, Union


class Node:
    """Data structure to be used for vertices in A* algorithm."""

    def __init__(self, node_id: Union[str, int], via_vertex: Union[str, int], actual_cost: float, total_estimated_cost: float):
        """
        Initialize a node for the priority queue.

        :param node_id: The id of the node.
        :param via_vertex: The id of the node that leads to this node.
        :param actual_cost: The actual cost to reach this node.
        :param total_estimated_cost: The total estimated cost to reach the goal from this node.
        """
        self.id = node_id
        self.via_vertex = via_vertex
        self.actual_cost = actual_cost
        self.total_est_cost = total_estimated_cost

    def __lt__(self, other):
        """Less than comparison operator for priority queue."""
        return self.total_est_cost < other.total_est_cost

    def __eq__(self, other):
        """Equality comparison operator for priority queue."""
        return self.total_est_cost == other.total_est_cost

    def __gt__(self, other):
        """Greater than comparison operator for priority queue."""
        return self.total_est_cost > other.total_est_cost


class PriorityQueue:
    """A priority queue implemented as a min-heap."""

    def __init__(self):
        """Initialize heap-array and size."""
        self._heap = []
        self._size = 0

    @property
    def size(self) -> int:
        """Return the size of the priority queue."""
        return self._size

    @staticmethod
    def _parent_ind(ind: int) -> int:
        """Return the index of the parent node."""
        return (ind - 1) // 2

    @staticmethod
    def _left_child_ind(ind: int) -> int:
        """Return the index of the left child node."""
        return 2 * ind + 1

    @staticmethod
    def _right_child_ind(ind: int) -> int:
        """Return the index of the right child node."""
        return 2 * ind + 2

    def insert(self, x: Node) -> None:
        """
        Add an element to the the min-heap.

        :param x: The element to be added.
        """
        self._heap.append(x)
        self._size += 1
        self._percolate_up(self._size - 1)

    def _percolate_up(self, ind: int) -> None:
        """
        Percolate up the element at the given index. Used to restore heap property after insertion.

        :param ind: The index of the element to be percolated up.
        """
        while ind > 0 and self._heap[ind] < self._heap[self._parent_ind(ind)]:
            self._heap[ind], self._heap[self._parent_ind(ind)] = self._heap[self._parent_ind(ind)], self._heap[ind]
            ind = self._parent_ind(ind)

    def extract_min(self):
        """
        Extract the minimum element from the min-heap.

        :return: The smallest element in the heap.
        """
        if self._size == 0:
            raise Exception('Priority queue is empty.')
        min_val = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._size -= 1
        self._heap.pop()
        self._percolate_down(0)
        return min_val

    def _percolate_down(self, ind: int) -> None:
        """
        Percolate down the element at the given index. Used to restore heap property after deletion.

        :param ind: The index of the element to be percolated down.
        """
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

    def find_node_by_id(self, node_id: Union[int, str]) -> int:
        """
        Find the index of a node with certain id in the heap.

        :param node_id: The id of the node to be found.
        :return: The index of the node in the heap, or -1 if not found.
        """
        for i, node in enumerate(self._heap):
            if node.id == node_id:
                return i
        return -1

    def get_node_by_id(self, node_id: Union[int, str]) -> Optional[Node]:
        """Get a node from the heap by its id."""

        node_ind = self.find_node_by_id(node_id)

        if node_ind == -1:
            return None
        else:
            return self._heap[node_ind]

    def delete_node_by_id(self, node_id: Union[int, str]) -> None:
        """
        Delete a node from the heap using its id and re-heapify.
        
        :param node_id: The id of the node to be deleted.
        """
        ind = self.find_node_by_id(node_id)
        if ind == -1:
            return
        if ind == 0 and self._size == 1:
            self._heap.pop()
            self._size -= 1
            return

        # Swap the node with the last node and remove it
        self._heap[ind], self._heap[-1] = self._heap[-1], self._heap[ind]
        self._heap.pop()
        self._size -= 1

        # Re-heapify
        if ind < self._size:  # Check if index is still within the heap bounds
            self._percolate_down(ind)
            self._percolate_up(ind)
