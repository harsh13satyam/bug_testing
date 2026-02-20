from src.utils import slugify, flatten_list, clamp_value


class TestSlugify:
    def test_basic_slug(self):
        assert slugify("Hello World") == "hello-world"


class TestFlattenList:
    def test_nested_list(self):
        assert flatten_list([1, [2, 3], 4]) == [1, 2, 3, 4]


class TestClampValue:
    def test_value_below_min(self):
        assert clamp_value(-5, 0, 10) == 0
