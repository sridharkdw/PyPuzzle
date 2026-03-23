from random import randint, sample
from typing import List

from random_word import RandomWords


def int_list(rng: int = 10) -> List[int]:
    return [randint(1, 100) for _ in range(0, rng)]


def int_ordered_list(rng: int = 10) -> List[int]:
    return sorted(int_list(rng))


def str_list(rng: int = 10) -> List[str]:
    return [RandomWords().get_random_word() for _ in range(0, rng)]


def str_ordered_list(rng: int = 10) -> List[str]:
    return sorted(str_list(rng))


def int_unique_list(rng: int = 10) -> List[int]:
    return sample(range(1, 100), rng)


def int_unique_ordered_list(rng: int = 10) -> List[int]:
    return sorted(int_unique_list(rng))
