#!/bin/bash

# Run all code quality checks and tests

set -e

echo "======================================"
echo "Running Code Quality Checks"
echo "======================================"

echo ""
echo "1. Running Black (Code Formatting)..."
black app tests

echo ""
echo "2. Running Flake8 (Linting)..."
flake8 app tests

echo ""
echo "3. Running MyPy (Type Checking)..."
mypy app

echo ""
echo "4. Running Bandit (Security Scanning)..."
bandit -r app

echo ""
echo "5. Running Pytest (Tests)..."
pytest -v

echo ""
echo "======================================"
echo "All checks passed successfully! ✓"
echo "======================================"
