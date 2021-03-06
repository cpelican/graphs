import math
from typing import Tuple, List, Dict


class Heap:
    def __init__(self, nodes: Dict[str, Dict[str, int]] = None):
        nodes = {} if not nodes else nodes
        # binary
        self.heap_type = 2
        self.nodes = []
        self.index = {}  # this dict allows to know with O(1) complexity the index of a node from its key {'node_1': 3}.
        for key in list(nodes.keys()):
            self.insert(key, nodes[key]['value'])

    def print(self) -> None:
        print('##########################')
        for key, value in self.nodes:
            print(f'{key}, value: {value}')

    def get_key(self, index: int) -> str:
        return self.nodes[index][0]

    def get_value(self, index: int) -> str:
        return self.nodes[index][1]

    def get_index(self, key: str) -> int:
        return self.index[key]

    def node_has_children(self, index: int) -> bool:
        return index * self.heap_type + 1 < len(self.nodes)

    def get_node_children(self, index: int) -> List[Tuple[str, str]]:
        return self.nodes[index * self.heap_type:index * self.heap_type + self.heap_type + 1]

    def insert(self, key: str, value: int) -> None:
        # add as last leave
        self.nodes.append((key, value))
        current_node_index = len(self.nodes) - 1
        self.index[key] = current_node_index
        self.heapify_up(current_node_index)

    def update_value(self, key: str, new_value: int) -> None:
        new_heap = []
        heapify_up = True
        changed_node_index = None
        for index, (node_key, value) in enumerate(self.nodes):
            if key == node_key:
                changed_node_index = index
                if new_value > value:
                    heapify_up = False
                node = node_key, new_value
            else:
                node = node_key, value
            new_heap.append(node)

        self.nodes = new_heap
        if heapify_up is True:
            self.heapify_up(changed_node_index)
            return
        self.heapify_down(changed_node_index)

    def heapify_up(self, current_node_index: int):
        """
        This method is used when we insert a new value in the heap (from the bottom).
        We need then to re-order all the values
        """
        if current_node_index == 0:
            return self.nodes
        parent_index = math.floor((current_node_index - 1) / self.heap_type)
        parent_value = self.nodes[parent_index][1]
        current_value = self.nodes[current_node_index][1]
        if parent_value <= current_value:
            return self.nodes
        elif parent_value > current_value:
            # we swap the two nodes and update also the index dict accordingly
            parent_key = self.get_key(parent_index)
            current_key = self.get_key(current_node_index)
            temp = self.nodes[parent_index]
            self.nodes[parent_index] = self.nodes[current_node_index]
            self.index[parent_key] = current_node_index
            self.nodes[current_node_index] = temp
            self.index[current_key] = parent_index
        return self.heapify_up(parent_index)

    def pop_min(self) -> Tuple[str, str]:
        current_index = 0
        heap_min = self.nodes[current_index]
        current_key = self.get_key(current_index)
        self.index[current_key] = None
        # exchange leave with root, reduce the heap size
        self.nodes[current_index] = self.nodes[len(self.nodes) - 1]
        current_key = self.get_key(current_index)
        self.index[current_key] = 0
        # remove the last value from the heap
        # todo: we also could put the extracted value at the end and
        #  therefore not recontruct a new list (and have an end_index)
        self.nodes = [*self.nodes[:len(self.nodes) - 1]]
        self.heapify_down(current_index)

        return heap_min

    def heapify_down(self, current_node_index: int):
        """
        This method is used when we take the minimum value and have to rebuild the heap
        """
        min_child_index = self.get_min_child_index(current_node_index)
        if not min_child_index:
            return self.nodes
        if self.nodes[current_node_index][1] <= self.nodes[min_child_index][1]:
            return self.nodes
        temp = self.nodes[current_node_index]
        current_node_key = self.get_key(current_node_index)
        self.nodes[current_node_index] = self.nodes[min_child_index]
        min_child_key = self.get_key(current_node_index)
        self.nodes[min_child_index] = temp
        self.index[current_node_key] = min_child_index
        self.index[min_child_key] = current_node_index

        current_index = min_child_index
        return self.heapify_down(current_index)

    def get_min_child_index(self, current_node_index: int) -> int:
        first_child_index = current_node_index * self.heap_type + self.heap_type - 1
        second_child_index = current_node_index * self.heap_type + self.heap_type
        # if the node does not have a child
        if first_child_index > len(self.nodes) - 1:
            return False
        # if the node has only on child
        if second_child_index > len(self.nodes) - 1:
            return first_child_index
        # return the smallest of both
        if self.nodes[first_child_index][1] < self.nodes[second_child_index][1]:
            return first_child_index
        return second_child_index

