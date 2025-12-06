.PHONY: help setup test clean demo format lint install

# Default target
help:
	@echo "🚀 new-project - Available commands:"
	@echo ""
	@echo "  make setup    - Setup project (venv + deps + hooks)"
	@echo "  make install  - Install dependencies"
	@echo "  make test     - Run tests with coverage"
	@echo "  make demo     - Run demo script"
	@echo "  make format   - Format code (black, isort)"
	@echo "  make lint     - Lint code (ruff)"
	@echo "  make clean    - Clean caches and build artifacts"
	@echo ""

# Setup project
setup:
	@echo "🚀 Setting up project..."
	@./scripts/setup.sh

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	@. .venv/bin/activate && pip install -e . -q
	@echo "✅ Dependencies installed"

# Run tests
test:
	@echo "🧪 Running tests..."
	@./scripts/test.sh

# Run demo
demo:
	@echo "🎬 Running demo..."
	@. .venv/bin/activate && python scripts/demo.py

# Format code
format:
	@echo "✨ Formatting code..."
	@. .venv/bin/activate && black . && isort .
	@echo "✅ Code formatted"

# Lint code
lint:
	@echo "🔍 Linting code..."
	@. .venv/bin/activate && ruff check .

# Clean caches
clean:
	@echo "🧹 Cleaning..."
	@./scripts/clean.sh
