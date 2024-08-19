#!/bin/bash

# Enable exit on non 0
set -e

# Get and set the environment variables
source ./deploy.test_set_envs.sh

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

# Run the linter first since it's really fast
sh /workspace/scripts/lint_apply.sh

echo ""
echo "Running pytest..."

# pytest /home/user/workspace/tests/ -v --lf --durations=0
# pytest /home/user/workspace/tests/ -v --durations=0
# --exitfirst = stop the execution of the tests instantly on first error or failed test
pytest /workspace/tests/ --lf -v --durations=0

echo ""
echo "pytest complete!"

exit 0
