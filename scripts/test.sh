#!/bin/bash
set -e

echo "🧪 Running full test suite..."

cd "$(dirname "$0")/.."

# Activate virtual environment
source .venv/bin/activate

# Run pytest with coverage
echo "📊 Running tests with coverage..."
pytest -v --cov=src --cov-report=term-missing

# Check code quality
echo ""
echo "🔍 Checking code quality..."
ruff check . || echo "⚠️  Ruff found issues"

echo ""
echo "✨ Test suite complete!"
