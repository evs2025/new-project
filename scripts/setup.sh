#!/bin/bash
set -e

echo "🚀 Setting up new-project..."

# Check if running from project root
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Run this script from the project root directory"
    exit 1
fi

# Create virtual environment if not exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip setuptools wheel -q

# Install project in editable mode
echo "📥 Installing project dependencies..."
pip install -e . -q

# Install pre-commit if config exists
if [ -f ".pre-commit-config.yaml" ]; then
    echo "🔧 Installing pre-commit hooks..."
    pip install pre-commit -q
    pre-commit install
fi

echo ""
echo "✨ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Activate environment: source .venv/bin/activate"
echo "   2. Run tests: pytest"
echo "   3. Start coding in src/"
echo ""
