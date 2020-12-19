import pytest

from src.graph import Graph

############# Tree ###############
#                                #
#            n_1                 #
#          /    \                #
#         /      \               #
#      n_2        n_3            #
#     /   \       /  \           #
#    /     \     /    \          #
#  n_4    n_5  n_6     n_7       #
#             / \      /  \      #
#            /   \    /    \     #
#         n_8   n_9  n_10   n_11 #
#                                #
##################################

tree = {
    'node_1': {
        'node_2': 10,
        'node_3': 7
    },
    'node_2': {
        'node_4': 40,
        'node_5': 7
    },
    'node_3': {
        'node_6': 8,
        'node_7': 22
    },
    'node_4': {},
    'node_5': {},
    'node_6': {
        'node_8': 2,
        'node_9': 1
    },
    'node_7': {
        'node_10': 15,
        'node_11': 5
    },
    'node_8': {},
    'node_9': {},
    'node_10': {},
    'node_11': {},
}

graph_with_fake_cycle = {**tree, 'node_4': {'node_5': 4}}

cycle = {'node_9': {'node_7': 1}, 'node_7': {**tree['node_7'], 'node_1': 22}}

graph_with_fake_cycle_and_true_cycle = {**graph_with_fake_cycle, **cycle}

graph_with_cycle = non_bipartite_graph = {**tree, **cycle}

graph_with_two_distinct_cycles = {**graph_with_cycle, 'node_4': {'node_5': 1}, 'node_5': {'node_2': 0}}

graph_with_two_merged_cycles = {**graph_with_cycle, 'node_6': {**tree['node_6'], 'node_7': 1}}

bipartite_graph = {
    'node_1': {
        'node_6': 0
    },
    'node_2': {},
    'node_3': {
        'node_9': 0
    },
    'node_4': {
        'node_7': 0,
        'node_8': 0,
    },
    'node_5': {
        'node_9': 0
    },
    'node_6': {
        'node_3': 0
    },
    'node_7': {
        'node_1': 0
    },
    'node_8': {},
    'node_9': {
        'node_4': 0
    },
    'node_10': {
        'node_5': 0
    }
}

class TestGraph:
    @pytest.mark.parametrize('graph_content, node_from, expected', [
        (tree, 'node_1', []),
        (graph_with_cycle, 'node_1', [['node_1', 'node_3', 'node_7'], ['node_1', 'node_3', 'node_6', 'node_9', 'node_7']]),
        (graph_with_two_distinct_cycles, 'node_1', [['node_1', 'node_3', 'node_7'], ['node_2', 'node_4', 'node_5'], ['node_1', 'node_3', 'node_6', 'node_9', 'node_7']]),
        (graph_with_two_merged_cycles, 'node_1', [['node_1', 'node_3', 'node_7'], ['node_1', 'node_3', 'node_6', 'node_7'], ['node_1', 'node_3', 'node_6', 'node_9', 'node_7']])
    ])
    def test_count_cycles(self, graph_content, node_from, expected):
        assert Graph(graph_content).get_cycles(node_from) == expected

    @pytest.mark.parametrize('graph_content, node_from, node_to, path', [
        (tree, 'node_1', 'node_11', [{'node_11': 34}, {'node_7': 29}, {'node_3': 7}]),
        (graph_with_cycle, 'node_1', 'node_11',
         [{'node_11': 22}, {'node_7': 17}, {'node_9':  16}, {'node_6': 15}, {'node_3': 7}]),
        (graph_with_two_merged_cycles, 'node_1', 'node_11',
         [{'node_11': 22}, {'node_7': 17}, {'node_9':  16}, {'node_6': 15}, {'node_3': 7}])
    ])
    def test_djikstra(self, graph_content, node_from, node_to, path):
        assert Graph(graph_content).dijkstra(node_from, node_to)

    @pytest.mark.parametrize('graph_content, node_from, node_to, expected', [
        (tree, 'node_1', 'node_11', [['node_1', 'node_3', 'node_7', 'node_11']]),
        (graph_with_cycle, 'node_1', 'node_7', [['node_1', 'node_3', 'node_6', 'node_9', 'node_7'], ['node_1', 'node_3', 'node_7']]),
        (graph_with_two_distinct_cycles, 'node_1', 'node_7', [['node_1', 'node_3', 'node_6', 'node_9', 'node_7'], ['node_1', 'node_3', 'node_7']]),
        (graph_with_two_merged_cycles, 'node_1', 'node_7', [['node_1', 'node_3', 'node_6', 'node_9', 'node_7'], ['node_1', 'node_3', 'node_6', 'node_7'], ['node_1', 'node_3', 'node_7']])
    ])
    def test_all_paths(self, graph_content, node_from, node_to, expected):
        assert Graph(graph_content).get_all_paths(node_from, node_to) == expected

    @pytest.mark.parametrize('graph_content, node_from, node_to, expected', [
        (tree, 'node_1', 'node_11', {'node_11': {}}),
        (tree, 'node_1', 'node_22', None),
        (graph_with_cycle, 'node_1', 'node_11', {'node_11': {}}),
        (graph_with_cycle, 'node_1', 'node_22', None),
        (graph_with_two_distinct_cycles, 'node_1', 'node_7', {'node_7': {'node_10': 15, 'node_11': 5, 'node_1': 22}}),
        (graph_with_two_distinct_cycles, 'node_1', 'node_22', None),
        (graph_with_two_merged_cycles, 'node_1', 'node_7', {'node_7': {'node_10': 15, 'node_11': 5, 'node_1': 22}}),
        (graph_with_two_merged_cycles, 'node_1', 'node_22', None),
    ])
    def test_search_breadth_recursive_succeeds_and_fails(self, graph_content, node_from, node_to, expected):
        assert Graph(graph_content).search_breadth_recursive(node_from, node_to) == expected

    @pytest.mark.parametrize('graph_content, node_from, node_to, expected', [
        (tree, 'node_1', 'node_11', {'node_11': {}}),
        (tree, 'node_1', 'node_22', None),
        (graph_with_cycle, 'node_1', 'node_11', {'node_11': {}}),
        (graph_with_cycle, 'node_1', 'node_22', None),
        (graph_with_two_distinct_cycles, 'node_1', 'node_7', {'node_7': {'node_10': 15, 'node_11': 5, 'node_1': 22}}),
        (graph_with_two_distinct_cycles, 'node_1', 'node_22', None),
        (graph_with_two_merged_cycles, 'node_1', 'node_7', {'node_7': {'node_10': 15, 'node_11': 5, 'node_1': 22}}),
        (graph_with_two_merged_cycles, 'node_1', 'node_22', None),
    ])
    def test_search_breadth_succeeds_and_fails(self, graph_content, node_from, node_to, expected):
        assert Graph(graph_content).search_breadth(node_from, node_to) == expected

    @pytest.mark.parametrize('graph_content, node_from, node_to, expected', [
        (tree, 'node_1', 'node_11', {'node_11': {}}),
        (tree, 'node_1', 'node_22', None),
        (graph_with_cycle, 'node_1', 'node_11', {'node_11': {}}),
        (graph_with_cycle, 'node_1', 'node_22', None),
        (graph_with_two_distinct_cycles, 'node_1', 'node_7', {'node_7': {'node_10': 15, 'node_11': 5, 'node_1': 22}}),
        (graph_with_two_distinct_cycles, 'node_1', 'node_22', None),
        (graph_with_two_merged_cycles, 'node_1', 'node_7', {'node_7': {'node_10': 15, 'node_11': 5, 'node_1': 22}}),
        (graph_with_two_merged_cycles, 'node_1', 'node_22', None),
    ])
    def test_search_depth_succeeds_and_fails(self, graph_content, node_from, node_to, expected):
        assert Graph(graph_content).search_depth(node_from, node_to) == expected

    @pytest.mark.parametrize('graph_content, node_from, node_to, expected', [
        (tree, 'node_1', 'node_11', {'node_11': {}}),
        (tree, 'node_1', 'node_22', None),
        (graph_with_cycle, 'node_1', 'node_11', {'node_11': {}}),
        (graph_with_cycle, 'node_1', 'node_22', None),
        (graph_with_two_distinct_cycles, 'node_1', 'node_7', {'node_7': {'node_10': 15, 'node_11': 5, 'node_1': 22}}),
        (graph_with_two_distinct_cycles, 'node_1', 'node_22', None),
        (graph_with_two_merged_cycles, 'node_1', 'node_7', {'node_7': {'node_10': 15, 'node_11': 5, 'node_1': 22}}),
        (graph_with_two_merged_cycles, 'node_1', 'node_22', None),
    ])
    def test_search_depth_succeeds_and_fails(self, graph_content, node_from, node_to, expected):
        assert Graph(graph_content).search_depth_recursive(node_from, node_to) == expected

    @pytest.mark.parametrize('graph_content, expected', [
        (bipartite_graph, True),
        (non_bipartite_graph, False)
    ])
    def test_is_bipartite_graph(self, graph_content, expected):
        assert Graph(graph_content).is_bipartite() == expected

    @pytest.mark.parametrize('graph_content, expected', [
        (bipartite_graph, True),
        (non_bipartite_graph, False)
    ])
    def test_is_bipartite_count_cycles_graph(self, graph_content, expected):
        assert Graph(graph_content).is_bipartite_count_cycles() == expected