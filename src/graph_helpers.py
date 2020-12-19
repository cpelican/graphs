from collections import deque
from typing import List, Optional


class GraphHelpers:
    def __init__(self, nodes):
        self.nodes = nodes

    def search_depth(self, node_from: str, node_to: str) -> Optional[dict]:
        visited_set = set()
        stack = [node_from]

        while len(stack) > 0:
            node_key_to_search = stack.pop()
            if node_key_to_search in visited_set:
                continue
            if node_key_to_search == node_to:
                return {node_to: self.nodes[node_key_to_search]}
            visited_set.add(node_key_to_search)
            current_node = self.nodes[node_key_to_search]
            stack.extend(list(current_node.keys()))

    def rec_search_depth(self, node_from_key: str, node_to_key: str, visited: list = []):
        for node_key in self.nodes[node_from_key].keys():
            if node_key in visited:
                continue

            visited.append(node_key)
            self.rec_search_depth(node_key, node_to_key, visited)
        if node_to_key in visited:
            return {node_to_key: self.nodes[node_to_key]}
        else:
            return None

    def search_breadth(self, node_from: str, node_to: str) -> Optional[dict]:
        visited_set = set()
        queue = deque([node_from])
        while len(queue) > 0:
            node_key_to_search = queue.popleft()
            if node_key_to_search in visited_set:
                continue
            if node_key_to_search == node_to:
                return {node_to: self.nodes[node_key_to_search]}
            visited_set.add(node_key_to_search)
            for key in list(self.nodes[node_key_to_search].keys()):
                queue.append(key)

    def rec_search_breadth(self, nodes_queue, node_to_key: str, visited_set: set) -> Optional[dict]:
        if len(nodes_queue) == 0:
            return None
        queue = deque(list(nodes_queue))
        for node_from_key in nodes_queue:
            queue.popleft()
            if node_from_key == node_to_key:
                return {node_to_key: self.nodes[node_to_key]}
            if node_from_key in visited_set:
                continue
            visited_set.add(node_from_key)

            for key in list(self.nodes[node_from_key].keys()):
                if key not in visited_set:
                    queue.append(key)
        return self.rec_search_breadth(queue, node_to_key, visited_set)

    def get_cycle_dep(self, node_from, visited_set) -> List[List[str]]:
        """Method that finds cycles in a graph"""
        queue = deque([(node_from, [])])
        cycles = []
        # we need this to prevent double cycles with nodes in different order
        cycles_sets = [set(c) for c in cycles]
        while len(queue) > 0:
            current_node, parents = queue.popleft()
            children = list(self.nodes[current_node].keys())
            if set(children).intersection(parents):
                for intersection in set(children).intersection(parents):
                    cycle = [*parents[parents.index(intersection):], current_node]
                    if len(cycle) > 2 and set(cycle) not in cycles_sets:
                        cycles.append(cycle)
                        cycles_sets.append(set(cycle))
            if current_node in visited_set:
                continue
            visited_set.add(current_node)
            parents = [*parents, current_node]
            for key in children:
                queue.append((key, parents))
        return cycles

    def all_paths_rec_bread(self, visited_set: set, queue, node_to: str, paths: List[List[str]]):
        current_node, path = queue.popleft()
        visited_set.add(current_node)
        if current_node == node_to:
            paths.append([*path, node_to])
        else:
            for child in self.nodes[current_node].keys():
                if child not in visited_set:
                    queue.append((child, [*path, current_node]))
                    self.all_paths_rec_bread(visited_set, queue, node_to, paths)

        visited_set.remove(current_node)

    def is_bipartite(self, parent_node: str, colors: dict, bipartite=True) -> bool:
        """Method that finds cycles in a graph coloring its nodes"""
        is_b = bipartite or True
        for child in self.nodes[parent_node]:
            visited = colors.get(child) is not None
            if not visited:
                colors[child] = 0 if colors[parent_node] == 1 else 1
            if colors.get(child) == colors.get(parent_node):
                return False
            if visited:
                continue
            is_b = self.is_bipartite(child, colors, is_b)
            if is_b is False:
                return False
        return True
