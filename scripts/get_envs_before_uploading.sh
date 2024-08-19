#!/bin/bash

# Set variable names from .env file
export $(cat ../.devcontainer/.env | grep -v "^#" | xargs)

# To ensure we use BuildKit for faster, more efficient builds
export DOCKER_BUILDKIT=1
export BUILDKIT_INLINE_CACHE=1
export COMPOSE_DOCKER_CLI_BUILD=1

echo "PYPI_TOKEN_PROD: $PYPI_TOKEN_PROD"