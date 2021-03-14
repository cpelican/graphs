import pytest

from src.algorithms import levenshtein, selection_sort, bubble_sort, heap_sort, merge, merge_sort


class TestAlgorithms:
    @pytest.mark.parametrize('str_1, str_2, expected', [
        ('bao', 'cab', 2),
        ('abcdef', 'abcdef', 0),
        ('abcdef', 'azcdef', 1),
        ('abcdef', 'axydef', 2),
        ('abcdef', 'axyzef', 3),
        ('abcdef', 'axyzaf', 4),
        ('abcdef', 'axyzab', 5),
        ('abcdef', 'axyzabc', 6),
    ])
    def test_levenshtein_works_as_expected(self, str_1, str_2, expected):
        assert levenshtein(str_1, str_2) == expected

    @pytest.mark.parametrize('input, expected', [
        ([9, 8, 23, 0, 0, 232, 1], [0, 0, 1, 8, 9, 23, 232]),
    ])
    def test_selection_sort(self, input, expected):
        assert selection_sort(input) == expected

    @pytest.mark.parametrize('input, expected', [
        ([9, 8, 23, 0, 0, 232, 1], [0, 0, 1, 8, 9, 23, 232]),
    ])
    def test_bubble_sort(self, input, expected):
        assert bubble_sort(input) == expected

    @pytest.mark.parametrize('input, expected', [
        ([9, 8, 23, 0, 0, 232, 1], [0, 0, 1, 8, 9, 23, 232]),
    ])
    def test_bubble_sort(self, input, expected):
        assert heap_sort(input) == expected

    @pytest.mark.parametrize('left, right, expected', [
        ([1, 3, 17], [0, 10, 11, 14, 15], [0, 1, 3, 10, 11, 14, 15, 17]),
    ])
    def test_merge_helper(self, left, right, expected):
        assert merge(left, right) == expected

    @pytest.mark.parametrize('input, expected', [
        ([9, 8, 23, 0, 0, 232, 1], [0, 0, 1, 8, 9, 23, 232]),
    ])
    def test_merge_sort(self, input, expected):
        assert merge_sort(input) == expected