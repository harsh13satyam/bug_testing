from src.utils import slugify, flatten_list, clamp_value


class TestSlugify:
    def test_basic_slug(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_characters(self):
        assert slugify("Hello! @World#") == "hello-world"

    def test_multiple_spaces(self):
        assert slugify("hello   world") == "hello-world"

    def test_trailing_spaces(self):
        assert slugify("  hello world  ") == "hello-world"


class TestFlattenList:
    def test_flat_list(self):
        assert flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_nested_list(self):
        assert flatten_list([1, [2, 3], 4]) == [1, 2, 3, 4]

    def test_deeply_nested(self):
        assert flatten_list([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

    def test_empty_list(self):
        assert flatten_list([]) == []


class TestClampValue:
    def test_value_in_range(self):
        assert clamp_value(5, 0, 10) == 5

    def test_value_below_min(self):
        assert clamp_value(-5, 0, 10) == 0

    def test_value_above_max(self):
        assert clamp_value(15, 0, 10) == 10

    def test_value_at_boundary(self):
        assert clamp_value(0, 0, 10) == 0
