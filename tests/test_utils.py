from src.utils import flatten_list


class TestFlattenList:
    def test_nested_list(self):
        assert flatten_list([1, [2, 3], 4]) == [1, 2, 3, 4]
