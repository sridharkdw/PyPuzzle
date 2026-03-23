#!/bin/bash

set -e


echo "░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓████████▓▒░"
echo "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        "
echo "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░    ░▒▓██▓▒░     ░▒▓██▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        "
echo "░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██▓▒░     ░▒▓██▓▒░  ░▒▓█▓▒░      ░▒▓██████▓▒░   "
echo "░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██▓▒░     ░▒▓██▓▒░    ░▒▓█▓▒░      ░▒▓█▓▒░        "
echo "░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░        "
echo "░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░ "


echo "Cleaning build..."
rm -rf build/

echo "Installing dependencies..."
pip install -e ".[dev]"
pip install build

echo "Building wheel..."
python -m build --wheel --outdir build/dist

echo "Formatting..."
black src/ test/

echo "Linting..."
ruff check --fix src/ test/

echo "Type checking..."
mypy src/

echo "Building docs..."
sphinx-build -b html docs/ build/docs

echo "Running Tests..."
pytest
