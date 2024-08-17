#!/bin/bash

# Enable exit on non 0
set -e
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
# cd ..
echo "Current working directory: $(pwd)"

# Use Ruff to lint everything
echo ""
echo "Running ruff linter..."
# Run the linter
ruff check ../dash_signature --fix --config ../pyproject.toml
ruff check ../tests --fix --config ../pyproject.toml

# Run the formatter
echo ""
echo "Running ruff formatter..."
ruff format ../dash_signature --config ../pyproject.toml
ruff format ../tests --config ../pyproject.toml
