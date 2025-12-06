#!/bin/bash
set -e

echo "🧹 Cleaning project..."

# Remove Python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type f -name "*.pyo" -delete 2>/dev/null || true

# Remove test cache
rm -rf .pytest_cache .ruff_cache .mypy_cache .coverage htmlcov

# Remove build artifacts
rm -rf build dist *.egg-info

# Remove OS files
find . -name ".DS_Store" -delete 2>/dev/null || true

echo "✨ Cleanup complete!"
