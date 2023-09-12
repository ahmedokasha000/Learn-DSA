
from math import sqrt

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

class Node:
    def __init__(self, id, via_vertex, actual_cost, total_estimated_cost):
        self.id = id
        self.via_vertex = via_vertex
        self.actual_cost = actual_cost
        self.total_est_cost = total_estimated_cost
    def __lt__(self, other):
        """Less than comparison operator for priority queue. """
        return self.total_est_cost < other.total_est_cost
    def __eq__(self, other):
        """Equality comparison operator for priority queue. """
        return self.total_est_cost == other.total_est_cost
    def __gt__(self, other):
        """Greater than comparison operator for priority queue. """
        return self.total_est_cost > other.total_est_cost

def heuristic_cost_estimate(vertex, goal_vertex):
    """Calculate the heuristic cost estimate between two vertices. Ecludian distance is used here."""
    
    return sqrt((vertex[0] - goal_vertex[0])**2 + (vertex[1] - goal_vertex[1])**2)

def road_distance(vertex1, vertex2):
    """ Calculate the road distance between two vertices."""
    return sqrt((vertex1[0] - vertex2[0])**2 + (vertex1[1] - vertex2[1])**2)


def shortest_path(m, start, goal):
    next_vertex = PriorityQueue()
    route = []
    next_vertex.insert(Node(start, None, 0, heuristic_cost_estimate(m.intersections[start], m.intersections[goal])))
    while next_vertex.size > 0:
        cur_node = next_vertex.extract_min()
        # Ignore nodes that are already in the route. This means we visited it already through a shorter path.
        if cur_node.id in route:
            continue

        route.append(cur_node.id)
        if cur_node.id == goal:
            break

        for road in m.roads[cur_node.id]:
            actual_cost = cur_node.actual_cost + road_distance(m.intersections[cur_node.id], m.intersections[road])
            total_est_cost = actual_cost + heuristic_cost_estimate(m.intersections[road], m.intersections[goal])
            next_city_node = Node(road, cur_node.id, actual_cost, total_est_cost)
            next_vertex.insert(next_city_node)

    print(f"shortest path called {route}")
    return route if route[-1] == goal else None

class Map:
    intersectons = None
    roads = None


def main():
    test_m = Map()
    test_m.intersections = {0: [0.7798606835438107, 0.6922727646627362],
                            1: [0.7647837074641568, 0.3252670836724646],
                            2: [0.7155217893995438, 0.20026498027300055],
                            3: [0.7076566826610747, 0.3278339270610988],
                            4: [0.8325506249953353, 0.02310946309985762],
                            5: [0.49016747075266875, 0.5464878695400415],
                            6: [0.8820353070895344, 0.6791919587749445],
                            7: [0.46247219371675075, 0.6258061621642713],
                            8: [0.11622158839385677, 0.11236327488812581],
                            9: [0.1285377678230034, 0.3285840695698353]}
    test_m.roads = [[7, 6, 5],
                    [4, 3, 2],
                    [4, 3, 1],
                    [5, 4, 1, 2],
                    [1, 2, 3],
                    [7, 0, 3],
                    [0],
                    [0, 5],
                    [9],
                    [8]]

    shortest_path(test_m, 6, 4)


if __name__ == "__main__":
    main()
