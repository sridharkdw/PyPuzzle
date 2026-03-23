import json
from pathlib import Path

with open(Path(__file__).parent / "generator_params.json") as f:
    _params = json.load(f)


def pytest_generate_tests(metafunc):
    if "rng" in metafunc.fixturenames:
        metafunc.parametrize("rng", _params["rng"])
