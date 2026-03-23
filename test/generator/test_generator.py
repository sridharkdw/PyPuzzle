from py_puzzle.generator.input_generator import (
    int_list,
    int_ordered_list,
    int_unique_list,
    int_unique_ordered_list,
    str_list,
    str_ordered_list,
)


class TestIntGenerators:
    def test_int_list(self, rng):
        result = int_list(rng)
        assert len(result) == rng
        assert all(isinstance(x, int) for x in result)

    def test_int_ordered_list(self, rng):
        result = int_ordered_list(rng)
        assert len(result) == rng
        assert result == sorted(result)

    def test_int_unique_list(self, rng):
        result = int_unique_list(rng)
        assert len(result) == rng
        assert len(set(result)) == rng

    def test_int_unique_ordered_list(self, rng):
        result = int_unique_ordered_list(rng)
        assert len(result) == rng
        assert result == sorted(result)
        assert len(set(result)) == rng


class TestStrGenerators:
    def test_str_list(self, rng):
        result = str_list(rng)
        assert len(result) == rng
        assert all(isinstance(x, str) for x in result)

    def test_str_ordered_list(self, rng):
        result = str_ordered_list(rng)
        assert len(result) == rng
        assert result == sorted(result)
