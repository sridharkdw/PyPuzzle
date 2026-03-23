from py_puzzle.search.algorithm import BinarySearch, LinearSearch


class TestBinarySearch:
    def test_process(self, binary_search_case):
        result = BinarySearch(arr=binary_search_case["arr"], target=binary_search_case["target"]).process()
        assert result["Output"] == binary_search_case["expected_index"]

    def test_first_value(self, binary_search_first_value_case):
        result = BinarySearch(
            arr=binary_search_first_value_case["arr"],
            target=binary_search_first_value_case["target"],
        ).first_value()
        assert result["Output"] == binary_search_first_value_case["expected_index"]


class TestBinarySearchDefaults:
    def test_process_default(self, default_rng):
        bs = BinarySearch()
        result = bs.process()
        assert result["Output"] >= 0
        assert bs.input[result["Output"]] == bs.target

    def test_first_value_default(self, default_rng):
        bs = BinarySearch()
        result = bs.first_value()
        assert result["Output"] >= 0
        assert bs.input[result["Output"]] == bs.target


class TestLinearSearch:
    def test_process(self, linear_search_case):
        result = LinearSearch(arr=linear_search_case["arr"], target=linear_search_case["target"]).process()
        assert result["Output"] == linear_search_case["expected_index"]

    def test_process_default(self, default_rng):
        ls = LinearSearch()
        result = ls.process()
        assert result["Output"] >= 0
        assert ls.input[result["Output"]] == ls.target
