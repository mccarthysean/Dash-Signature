#!/bin/bash

# Ensure the script fails if any of the commands fail
set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

echo -e "\nFirst we will build the frontend assets using yarn"
yarn run bundle

echo -e "\nNow we will build the backend package using poetry"
poetry build

echo -e "\nPackage built successfully"
