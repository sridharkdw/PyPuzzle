# PyPuzzle
Python based Data Structures and Algorithms

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Folder Structure](#2-folder-structure)
3. [Setup](#3-setup)
4. [Algorithms](#4-algorithms)
   - 4.1 [Binary Search](#41-binary-search)
   - 4.2 [Linear Search](#42-linear-search)
5. [Notebooks](#5-notebooks)
   - 5.1 [Binary Search Notebook](#51-binary-search-notebook)
   - 5.2 [Linear Search Notebook](#52-linear-search-notebook)
6. [Running Tests](#6-running-tests)
7. [Documentation](#7-documentation)

---

## 1. Prerequisites

- Python 3.12+
- IDE: [Visual Studio Code](https://code.visualstudio.com/download) or [PyCharm](https://www.jetbrains.com/pycharm/)

---

## 2. Folder Structure

```
PyPuzzle/
├── src/
│   └── py_puzzle/
│       ├── generator/
│       │   └── input_generator.py        # Random input generators
│       └── search/
│           └── algorithm.py              # Search algorithm implementations
├── test/
│   ├── generator/
│   │   ├── conftest.py
│   │   ├── generator_params.json
│   │   └── test_generator.py
│   └── search/
│       ├── notebooks/
│       │   ├── binary_search.ipynb       # Interactive binary search notebook
│       │   └── linear_search.ipynb       # Interactive linear search notebook
│       ├── conftest.py
│       ├── search_params.json
│       └── test_search.py
├── docs/                                 # Sphinx documentation
├── build.sh                              # Build, lint, type-check, test
├── pyproject.toml                        # Project configuration
└── requirements.txt
```

---

## 3. Setup

**1. Create a virtual environment**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

**2. Install dependencies**

```bash
pip install -e ".[dev]"
```

**3. Run the build**

```bash
./build.sh
```

The build script runs the following steps in order:

| Step | Tool | Description |
|---|---|---|
| Clean | `rm -rf build/` | Remove previous build artifacts |
| Install | `pip` | Install package and dev dependencies |
| Wheel | `python -m build` | Build distributable wheel to `build/dist/` |
| Format | `black` | Auto-format source and test files |
| Lint | `ruff` | Check and auto-fix style and import order |
| Type check | `mypy` | Static type checking with strict mode |
| Docs | `sphinx-build` | Generate HTML docs to `build/docs/` |
| Tests | `pytest` | Run tests with coverage report to `build/coverage/` |

---

## 4. Algorithms

### 4.1 Binary Search

Binary search operates on a **sorted list** and finds a target value by repeatedly halving the search space.

**Time complexity:** O(log n)
**Space complexity:** O(1)

| Method | Description |
|---|---|
| `process()` | Returns the index of the target, or `-1` if not found |
| `first_value()` | Returns the index of the **first occurrence** of the target in a list with duplicates |

**Example**

```python
from py_puzzle.search.algorithm import BinarySearch

bs = BinarySearch(arr=[1, 3, 5, 7, 9, 11], target=7)
print(bs.process())
# {'Input': [1, 3, 5, 7, 9, 11], 'Target': 7, 'Output': 3}

bs = BinarySearch(arr=[1, 2, 2, 2, 5, 9], target=2)
print(bs.first_value())
# {'Input': [1, 2, 2, 2, 5, 9], 'Target': 2, 'Output': 1}
```

**Using default random input**

```python
bs = BinarySearch()   # generates a sorted random list of 25 integers
print(bs.process())
```

> To test and explore Binary Search interactively, use the dedicated notebook:
> `test/search/notebooks/binary_search.ipynb` — see [Section 5.1](#51-binary-search-notebook)

---

### 4.2 Linear Search

Linear search scans the list from left to right and returns the first index where the target is found. Works on **unsorted lists**.

**Time complexity:** O(n)
**Space complexity:** O(1)

| Method | Description |
|---|---|
| `process()` | Returns the index of the first occurrence of the target, or `-1` if not found |

**Example**

```python
from py_puzzle.search.algorithm import LinearSearch

ls = LinearSearch(arr=[4, 2, 7, 1, 9, 3], target=7)
print(ls.process())
# {'Input': [4, 2, 7, 1, 9, 3], 'Target': 7, 'Output': 2}
```

**Using default random input**

```python
ls = LinearSearch()   # generates a sorted random list of 25 integers
print(ls.process())
```

> To test and explore Linear Search interactively, use the dedicated notebook:
> `test/search/notebooks/linear_search.ipynb` — see [Section 5.2](#52-linear-search-notebook)

---

## 5. Notebooks

The notebooks under `test/search/notebooks/` are dedicated to **interactive user testing**. They allow you to run and observe algorithm behaviour step by step with live output, without needing to execute the full test suite.

**Launch Jupyter**

```bash
jupyter notebook test/search/notebooks/
```

---

### 5.1 Binary Search Notebook

`test/search/notebooks/binary_search.ipynb`

| Cell | Description |
|---|---|
| Cell 1 | Runs `first_value()` on a hardcoded list with duplicates and asserts the first occurrence index |
| Cell 2 | Runs `process()` on a random input, detects if the result is not the first occurrence via `AssertionError`, then automatically retries with `first_value()` on the same instance |

---

### 5.2 Linear Search Notebook

`test/search/notebooks/linear_search.ipynb`

| Cell | Description |
|---|---|
| Cell 1 | Runs `process()` on a random input and asserts the output index matches the expected position |

---

## 6. Running Tests

```bash
pytest
```

Coverage reports are generated at:

- HTML: `build/coverage/html/index.html`
- XML: `build/coverage/coverage.xml`
- Terminal: printed after each test run

---

## 7. Documentation

```bash
sphinx-build -b html docs/ build/docs
open build/docs/index.html
```
