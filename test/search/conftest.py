import json
from pathlib import Path

with open(Path(__file__).parent / "search_params.json") as f:
    _params = json.load(f)


def pytest_generate_tests(metafunc):
    if "binary_search_case" in metafunc.fixturenames:
        metafunc.parametrize("binary_search_case", _params["binary_search"])
    if "binary_search_first_value_case" in metafunc.fixturenames:
        metafunc.parametrize("binary_search_first_value_case", _params["binary_search_first_value"])
    if "linear_search_case" in metafunc.fixturenames:
        metafunc.parametrize("linear_search_case", _params["linear_search"])
    if "default_rng" in metafunc.fixturenames:
        metafunc.parametrize("default_rng", _params["default_rng"])
