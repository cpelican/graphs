import pytest

from src.algorithms import levenshtein


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