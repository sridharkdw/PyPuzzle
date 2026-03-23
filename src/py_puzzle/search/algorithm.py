from random import choice

from py_puzzle.generator.input_generator import int_ordered_list


# ---------------------------------------------------------------------------
# Binary Search
# Requires a sorted list. Repeatedly halves the search space to locate the
# target. Time: O(log n)  |  Space: O(1)
# Interactive testing: test/search/notebooks/binary_search.ipynb
# ---------------------------------------------------------------------------
class BinarySearch:
    def __init__(self, arr: list[int] | None = None, target: int | None = None):
        self.input = int_ordered_list(rng=25) if arr is None else arr
        self.target = choice(self.input) if target is None else target
        self.result: dict[str, int | list[int]] = {"Input": self.input, "Target": self.target, "Output": -1}

    def process(self) -> dict[str, int | list[int]]:
        """Search for target in a sorted list. Returns the index or -1 if not found."""
        n = len(self.input)
        if n == 0:
            return self.result
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2  # avoid overflow vs (left + right) / 2
            check = self.input[mid]
            if check == self.target:
                self.result.update({"Output": mid})
                break
            elif check < self.target:
                left = mid + 1  # target is in the right half
            else:
                right = mid - 1  # target is in the left half
        return self.result

    def check_prev_value(self, input_index: int) -> int:
        """Walk left from input_index to find the first occurrence of a duplicate value."""
        # keep stepping left while the previous element is the same value
        while input_index > 0 and self.input[input_index - 1] == self.input[input_index]:
            input_index -= 1
        return input_index

    def first_value(self) -> dict[str, int | list[int]]:
        """Search for the first occurrence of target in a sorted list with duplicates."""
        n = len(self.input)
        if n == 0:
            return self.result
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            check = self.input[mid]
            if check == self.target:
                # target found — walk left to find the first occurrence
                mid_index = self.check_prev_value(input_index=mid)
                self.result.update({"Output": mid_index})
                break
            elif check < self.target:
                left = mid + 1
            else:
                right = mid - 1
        return self.result


# ---------------------------------------------------------------------------
# Linear Search
# Works on unsorted lists. Scans every element until the target is found.
# Time: O(n)  |  Space: O(1)
# Interactive testing: test/search/notebooks/linear_search.ipynb
# ---------------------------------------------------------------------------
class LinearSearch:
    def __init__(self, arr: list[int] | None = None, target: int | None = None):
        self.input = int_ordered_list(rng=25) if arr is None else arr
        self.target = choice(self.input) if target is None else target
        self.result: dict[str, int | list[int]] = {"Input": self.input, "Target": self.target, "Output": -1}

    def process(self) -> dict[str, int | list[int]]:
        """Scan the list from left to right. Returns the first index of target or -1 if not found."""
        for i in range(len(self.input)):
            if self.input[i] == self.target:  # target found — stop immediately
                self.result.update({"Output": i})
                break
        return self.result
