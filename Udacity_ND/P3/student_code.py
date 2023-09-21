
from typing import List, Union, Optional
from math import sqrt


class Node:
    """ Data structure to be used for vertices in A* algorithm."""

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

        # Swap the node with the last node and remove it
        self._heap[ind], self._heap[-1] = self._heap[-1], self._heap[ind]
        self._heap.pop()
        self._size -= 1

        # Re-heapify
        self._percolate_down(ind)
        self._percolate_up(ind)


def heuristic_cost_estimate(vertex: tuple, goal_vertex: tuple) -> float:
    """
    Calculate the heuristic cost estimate between two vertices. Euclidean distance is used here.

    :param vertex: The vertex to calculate the heuristic cost estimate from.
    :type vertex: tuple(x, y)
    :param goal_vertex: The goal vertex.
    type goal_vertex: tuple(x, y)
    :return: The heuristic cost estimate.
    """
    return sqrt((vertex[0] - goal_vertex[0])**2 + (vertex[1] - goal_vertex[1])**2)


def road_distance(vertex1: tuple, vertex2: tuple) -> float:
    """
    Calculate the road distance between two svertices.

    :param vertex1: The first vertex.
    :type vertex1: tuple(x, y)
    :param vertex2: The second vertex.
    :type vertex2: tuple(x, y)
    :return: The road distance between the two vertices.
    """
    return sqrt((vertex1[0] - vertex2[0])**2 + (vertex1[1] - vertex2[1])**2)


def shortest_path(m, start: Union[str, int], goal: Union[str, int]) -> List[Union[str, int]]:
    """
    Calculate the shortest path between two vertices using A* algorithm.

    :param m: The map containing the vertices and roads.
    :param start: The id of the start vertex.
    :param goal: The id of the goal vertex.
    :return: The shortest path between the two vertices as a list of vertex ids.
    """
    open_set_queue = PriorityQueue()    # Priority queue to store the nodes to be visited and evaluated in the future.
    closed_set = set()                  # Set to store the nodes that have been visited and evaluated.
    route = []                          # list to store all the traversed nodes

    open_set_queue.insert(Node(start, None, 0, heuristic_cost_estimate(m.intersections[start], m.intersections[goal])))

    while open_set_queue.size > 0:
        cur_node = open_set_queue.extract_min()

        route.append(cur_node)

        # Early exit if we reached the goal
        if cur_node.id == goal:
            break

        # Ignore nodes that are already in the closed set. This means we visited it already through a shorter path.
        if cur_node.id in closed_set:
            continue

        for city in m.roads[cur_node.id]:
            if city in closed_set:
                continue
            actual_cost = cur_node.actual_cost + road_distance(m.intersections[cur_node.id], m.intersections[city])
            total_est_cost = actual_cost + heuristic_cost_estimate(m.intersections[city], m.intersections[goal])
            city_new_node = Node(city, cur_node.id, actual_cost, total_est_cost)     # Create a new node for the city on the other end of the road
            city_old_node = open_set_queue.get_node_by_id(city)
            if city_old_node is not None:
                if city_old_node.total_est_cost > city_new_node.total_est_cost:
                    open_set_queue.delete_node_by_id(city_old_node.id)
                    open_set_queue.insert(city_new_node)
            else:
                open_set_queue.insert(city_new_node)
        closed_set.add(cur_node.id)

    return route2shortest(route, start, goal)


def route2shortest(path: List[Union[str, int]], start: Union[str, int], goal: Union[str, int]) -> Optional[List[Union[str, int]]]:
    """
    Find the shortest path from the route returned by A* algorithm.

    Some nodes in the route may be visited more than once based on the nature of the graph. As a result,  additional processing is needed to find the shortest path.

    :param path: The route returned by A* algorithm.
    :param start: The id of the start vertex.
    :param goal: The id of the goal vertex.
    :return: The shortest path between the two vertices as a list of vertex ids or None if no path is found.
    """
    # Early exit if the last node's id is not the goal
    if len(path) == 0 or path[-1].id != goal:
        return None

    cur_node = path.pop()
    prev_node = cur_node.via_vertex
    shortest_path = [cur_node.id]

    while len(path) > 0:
        cur_node = path.pop()
        # Check if we reached the previous node
        if cur_node.id == prev_node:
            shortest_path.append(cur_node.id)
            prev_node = cur_node.via_vertex
            # Break if we reached the start node, no need to check the rest of the path
            if prev_node == start:
                shortest_path.append(prev_node)
                break

    return shortest_path[::-1] if shortest_path[-1] == start else None
