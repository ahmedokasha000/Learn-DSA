
from typing import List, Union, Optional
from math import sqrt
import copy
from utils import animate_path
from priority_queue import PriorityQueue, Node
from test_map import g_map


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


def main():

    start = 38
    end = 1

    sh, route = shortest_path(g_map, start, end, "Manhattan")  # Assuming shortest_path function returns both shortest_path and route
    if sh:
        animate_path(g_map, route, sh, start, end, "Manhattan")

    sh, route = shortest_path(g_map, start, end, "Euclidean")  # Assuming shortest_path function returns both shortest_path and route
    if sh:
        animate_path(g_map, route, sh, start, end, "Euclidean")


if __name__ == "__main__":
    main()
