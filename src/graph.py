import cmath
from collections import deque
from typing import Tuple, List

from src.graph_helpers import GraphHelpers
from src.heap import Heap


class Graph:
    def __init__(self, nodes={}, is_directed=True):
        self.nodes = nodes
        self.is_directed = is_directed

    def __str__(self):
        repr = 'Graph nodes:\n'
        for node in self.nodes.keys():
            repr += f'# {node}: {", ".join(list(self.nodes[node]))}'
            repr += f'\n'
        return repr

    def add_node(self, value: str):
        self.nodes[value] = {}

    def add_edge(self, node_from: str, node_to: str, edge_value: int = 0):
        try:
            self.nodes[node_from][node_to] = edge_value
            if not self.is_directed:
                self.nodes[node_to][node_from] = edge_value
        except KeyError:
            print('One of the nodes provided do not belong to the graph')

    def remove_edge(self, node_from: str, node_to: str):
        try:
            self.nodes[node_from].pop(node_to)
            if not self.is_directed:
                self.nodes[node_to].pop(node_from)
        except KeyError:
            print('One of the nodes provided do not belong to the graph')

    # BFS: Good way to find shortest path
    def search_breadth_recursive(self, node_from: str, node_to: str):
        return GraphHelpers(self.nodes).rec_search_breadth([node_from], node_to, set())

    def search_breadth(self, node_from: str, node_to: str):
        return GraphHelpers(self.nodes).search_breadth(node_from, node_to)

    # DFS: Good way to find if a path exists
    def search_depth_recursive(self, node_from: str, node_to: str):
        return GraphHelpers(self.nodes).rec_search_depth(node_from, node_to)

    def search_depth(self, node_from: str, node_to: str):
        return GraphHelpers(self.nodes).search_depth(node_from, node_to)

    def get_all_paths(self, node_from: str, node_to: str) -> List[List[str]]:
        """Method that finds all possible path between 2 nodes"""
        paths = []
        GraphHelpers(self.nodes).all_paths_rec_bread(set(), deque([(node_from, [])]), node_to, paths)
        return paths

    def get_cycles(self, node_from: str) -> List[List[str]]:
        """
        :param node_from: The entry point
        :return:
        """
        cycles = GraphHelpers(self.nodes).get_cycle_dep(node_from, set())
        return cycles

    def dijkstra(self, node_key: str, node_destination_key: str) -> List[Tuple[str, int]]:
        """
        Method that returns the shortest path between 2 nodes

        We will store for each node its parent(previous_node)
        We will store the distances from source node in a distances registry

        1. At first the distance registry is set to infinite except for the source node
        2. We will use a heap, in which we temporarily store the nodes to visit
        3. The heap will allow us to retrieve the next node with minimal distance from source node
        4. From each visited nodes, we will store its neighbors in the heap,
           and if the distance we found is shorter than the previous one,
           we update the distance and store it in the heap to be visited.
        5. Finally, from the destination key, we will look in the parent registry,
           and create the path with the distance registry
        """
        heap_instance = Heap()
        # set the distances registry
        distances = {}
        visited = []
        previous_node = {}
        for key in self.nodes.keys():
            distances[key] = cmath.inf
        distances[node_key] = 0
        # helper to create path
        previous_node[node_key] = None
        heap_instance.insert(node_key, 0)
        while len(heap_instance.nodes) > 0:
            heap_node = heap_instance.pop_min()
            current_key = heap_node[0]
            visited.append(current_key)
            for child_key, child_value in self.nodes[current_key].items():
                if child_key in visited:
                    continue
                # At first we have zero, then we take this value and we update it(so we don't deal with inf)
                new_dist = distances[current_key] + child_value
                if new_dist < distances[child_key]:
                    distances[child_key] = new_dist
                    heap_instance.insert(child_key, new_dist)
                    previous_node[child_key] = current_key

        key = node_destination_key
        path = []
        while previous_node[key]:
            path.insert(0, (key, distances[key]))
            key = previous_node[key]
        path.insert(0, (node_key, 0))

        return path

    def is_bipartite(self) -> bool:
        """
        Finds if graph is bipartite with coloring
        Definition: A bipartite graph is a graph that does not contains odd length cycles

        Doing a breadth search, we'll color each node with the opposite color from its parent
        If the graph is bipartite, it has no odd length cycle,
        therefore we should not find any child with the same color as its parent
        if not, it means the graph is not bipartite
        """
        for source_node in self.nodes.keys():
            colors = {source_node: 0}
            if GraphHelpers(self.nodes).is_bipartite(source_node, colors, True) is False:
                return False
        return True

    def is_bipartite_count_cycles(self) -> bool:
        """
        Finds if graph is bipartite counting its cycles
        Definition: A bipartite graph is a graph that does not contains odd length cycles
        """
        for source_node in self.nodes.keys():
            for cycle in self.get_cycles(source_node):
                if (len(cycle) % 2) != 0:
                    return False
        return True

    # TODO: remove me once done
    # check that each subset has the same size as the other subset
    # if it is not the case => there is a match
    # for fulkerson
    # find all path between 2 nodes.
    # create a new graph with values === 0
    # for each path, assign the minimum original value to the new graph
