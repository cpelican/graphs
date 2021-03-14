
################ Heap #################
# node name: value                    #
#                n_1:0                #
#              /       \              #
#             /         \             #
#          n_4:3        n_6:5         #
#         /   \            /  \       #
#        /     \          /    \      #
#      n_9:8    n_10:9  n_6     n_7   #
#      /   \        \     \           #
#     /     \        \     \          #
#  n_8:777   n_2:12  n5:40  n_11:100  #
#                                     #
#######################################
import pytest

from src.heap import Heap

heap_input = {
    'node_1': {
        'value': 0
    },
    'node_2': {
        'value': 12
    },
    'node_3': {
        'value': 6
    },
    'node_4': {
        'value': 3
    },
    'node_5': {
        'value': 40
    },
    'node_6': {
        'value': 5
    },
    'node_7': {
        'value': 69
    },
    'node_8': {
        'value': 777
    },
    'node_9': {
        'value': 8
    },
    'node_10': {
        'value': 9
    },
    'node_11': {
        'value': 100
    },
}

nodes = [
    ('node_1', 0), ('node_4', 3), ('node_6', 5), ('node_9', 8), ('node_10', 9), ('node_3', 6), ('node_7', 69),
    ('node_8', 777), ('node_2', 12), ('node_5', 40), ('node_11', 100)
]
index = {
    'node_1': 0, 'node_2': 8, 'node_3': 5, 'node_4': 1, 'node_5': 9, 'node_6': 2, 'node_7': 6, 'node_8': 7, 'node_9': 3,
    'node_10': 4, 'node_11': 10
}


class TestHeap:
    """The heapify down is tested in test_algorithms with the heap sort test"""
    @pytest.mark.parametrize('input_nodes, expected_nodes, expected_index', [
        (heap_input, nodes, index),
    ])
    def test_init(self, input_nodes, expected_nodes, expected_index):
        """
        testing the init also allows to test the heapify up
        """
        new_heap = Heap(input_nodes)
        assert new_heap.nodes == expected_nodes
        assert new_heap.index == expected_index

