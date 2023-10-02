
from typing import List, Union, Optional
from math import sqrt
import copy

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



def heuristic_cost_estimate(vertex: tuple, goal_vertex: tuple, fn="Euclidean") -> float:
    """
    Calculate the heuristic cost estimate between two vertices. Euclidean distance is used here.

    :param vertex: The vertex to calculate the heuristic cost estimate from.
    :type vertex: tuple(x, y)
    :param goal_vertex: The goal vertex.
    type goal_vertex: tuple(x, y)
    :return: The heuristic cost estimate.
    """
    distance = 0
    if fn == "Euclidean":
        distance = sqrt((vertex[0] - goal_vertex[0])**2 + (vertex[1] - goal_vertex[1])**2)
    elif fn == "Manhattan":
        distance = abs(vertex[0] - goal_vertex[0]) + abs(vertex[1] - goal_vertex[1])

    return distance


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


def shortest_path(m, start: Union[str, int], goal: Union[str, int], heuristic_fn="Euclidean") -> List[Union[str, int]]:
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

    open_set_queue.insert(Node(start, None, 0, heuristic_cost_estimate(m.intersections[start], m.intersections[goal], heuristic_fn)))

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
            total_est_cost = actual_cost + heuristic_cost_estimate(m.intersections[city], m.intersections[goal], heuristic_fn)
            city_new_node = Node(city, cur_node.id, actual_cost, total_est_cost)     # Create a new node for the city on the other end of the road
            city_old_node = open_set_queue.get_node_by_id(city)
            if city_old_node is not None:
                if city_old_node.total_est_cost > city_new_node.total_est_cost:
                    open_set_queue.delete_node_by_id(city_old_node.id)
                    open_set_queue.insert(city_new_node)
            else:
                open_set_queue.insert(city_new_node)
        closed_set.add(cur_node.id)

    dbg_route = copy.deepcopy(route)
    return route2shortest(route, start, goal) , dbg_route


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



class Map:
    intersectons = None
    roads = None

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def plot_roads(m, ax):
    """Plot the roads on the given axis."""
    for start, ends in enumerate(m.roads):
        x1, y1 = m.intersections[start]
        for end in ends:
            x2, y2 = m.intersections[end]
            ax.plot([x1, x2], [y1, y2], color='lightgray', zorder=0)

def animate_path(m, route, shortest_path, start, end, suffix=""):
    fig, ax = plt.subplots(figsize=(16, 12))  # Adjust the figure size

    plot_roads(m, ax)  # Plot the roads

    # Plot all intersections
    for intersection in m.intersections.values():
        ax.scatter(intersection[0], intersection[1], c='darkgray', s=50, zorder=1)

    visited_x, visited_y = [], []  
    visited = ax.scatter([], [], c=[], cmap='coolwarm', s=100, zorder=2)  # Visited nodes with bigger size
    path, = ax.plot([], [], 'ro-', lw=2, zorder=3)  # Final path

    # Add grid and labels
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title('A* Pathfinding Algorithm')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')

    def init():
        return visited, path

    def update(frame):
        if frame < len(route):
            x, y = m.intersections[route[frame].id]
            visited_x.append(x)
            visited_y.append(y)
            visited.set_offsets(np.c_[visited_x, visited_y])
            visited.set_array(np.linspace(0, 1, len(visited_x)))
        if frame == len(route):
            x_vals = [m.intersections[node][0] for node in shortest_path]
            y_vals = [m.intersections[node][1] for node in shortest_path]
            path.set_data(x_vals, y_vals)
            ax.scatter([m.intersections[start][0]], [m.intersections[start][1]], c='limegreen', s=100, zorder=4, label='Start')
            ax.scatter([m.intersections[end][0]], [m.intersections[end][1]], c='crimson', s=100, zorder=4, label='End')
            ax.legend()
        return visited, path

    ani = animation.FuncAnimation(fig, update, frames=range(len(route) + 1), init_func=init, blit=False, interval=500)
    ani.save(f'animation_{start}_{end}_{suffix}.mp4', writer='ffmpeg', fps=1)





def main():
    test_m = Map()
    test_m.intersections = {0: [0.7801603911549438, 0.49474860768712914],
                            1: [0.5249831588690298, 0.14953665513987202],
                            2: [0.8085335344099086, 0.7696330846542071],
                            3: [0.2599134798656856, 0.14485659826020547],
                            4: [0.7353838928272886, 0.8089961609345658],
                            5: [0.09088671576431506, 0.7222846879290787],
                            6: [0.313999018186756, 0.01876171413125327],
                            7: [0.6824813442515916, 0.8016111783687677],
                            8: [0.20128789391122526, 0.43196344222361227],
                            9: [0.8551947714242674, 0.9011339078096633],
                            10: [0.7581736589784409, 0.24026772497187532],
                            11: [0.25311953895059136, 0.10321622277398101],
                            12: [0.4813859169876731, 0.5006237737207431],
                            13: [0.9112422509614865, 0.1839028760606296],
                            14: [0.04580558670435442, 0.5886703168399895],
                            15: [0.4582523173083307, 0.1735506267461867],
                            16: [0.12939557977525573, 0.690016328140396],
                            17: [0.607698913404794, 0.362322730884702],
                            18: [0.719569201584275, 0.13985272363426526],
                            19: [0.8860336256842246, 0.891868301175821],
                            20: [0.4238357358399233, 0.026771817842421997],
                            21: [0.8252497121120052, 0.9532681441921305],
                            22: [0.47415009287034726, 0.7353428557575755],
                            23: [0.26253385360950576, 0.9768234503830939],
                            24: [0.9363713903322148, 0.13022993020357043],
                            25: [0.6243437191127235, 0.21665962402659544],
                            26: [0.5572917679006295, 0.2083567880838434],
                            27: [0.7482655725962591, 0.12631654071213483],
                            28: [0.6435799740880603, 0.5488515965193208],
                            29: [0.34509802713919313, 0.8800306496459869],
                            30: [0.021423673670808885, 0.4666482714834408],
                            31: [0.640952694324525, 0.3232711412508066],
                            32: [0.17440205342790494, 0.9528527425842739],
                            33: [0.1332965908314021, 0.3996510641743197],
                            34: [0.583993110207876, 0.42704536740474663],
                            35: [0.3073865727705063, 0.09186645974288632],
                            36: [0.740625863119245, 0.68128520136847],
                            37: [0.3345284735051981, 0.6569436279895382],
                            38: [0.17972981733780147, 0.999395685828547],
                            39: [0.6315322816286787, 0.7311657634689946]}
    test_m.roads = [[36, 34, 31, 28, 17],
                    [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
                    [39, 36, 21, 19, 9, 7, 4],
                    [35, 20, 15, 11, 6],
                    [39, 36, 21, 19, 9, 7, 2],
                    [32, 16, 14],
                    [35, 20, 15, 11, 1, 3],
                    [39, 36, 22, 21, 19, 9, 2, 4],
                    [33, 30, 14],
                    [36, 21, 19, 2, 4, 7],
                    [31, 27, 26, 25, 24, 18, 17, 13],
                    [35, 20, 15, 3, 6],
                    [37, 34, 31, 28, 22, 17],
                    [27, 24, 18, 10],
                    [33, 30, 16, 5, 8],
                    [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
                    [37, 30, 5, 14],
                    [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
                    [31, 27, 26, 25, 24, 1, 10, 13, 17],
                    [21, 2, 4, 7, 9],
                    [35, 26, 1, 3, 6, 11, 15],
                    [2, 4, 7, 9, 19],
                    [39, 37, 29, 7, 12],
                    [38, 32, 29],
                    [27, 10, 13, 18],
                    [34, 31, 27, 26, 1, 10, 15, 17, 18],
                    [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
                    [31, 1, 10, 13, 18, 24, 25, 26],
                    [39, 36, 34, 31, 0, 12, 17],
                    [38, 37, 32, 22, 23],
                    [33, 8, 14, 16],
                    [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
                    [38, 5, 23, 29],
                    [8, 14, 30],
                    [0, 12, 17, 25, 26, 28, 31],
                    [1, 3, 6, 11, 15, 20],
                    [39, 0, 2, 4, 7, 9, 28],
                    [12, 16, 22, 29],
                    [23, 29, 32],
                    [2, 4, 7, 22, 28, 36]]
    
    start = 38
    end = 6
    

    sh, route = shortest_path(test_m, start, end, "Manhattan")  # Assuming shortest_path function returns both shortest_path and route

    if sh:
        display_animation = animate_path(test_m, route, sh, start, end, "Manhattan")

    sh, route = shortest_path(test_m, start, end, "Euclidean")  # Assuming shortest_path function returns both shortest_path and route

    if sh:
        display_animation = animate_path(test_m, route, sh, start, end, "Euclidean")
if __name__ == "__main__":
    main()





