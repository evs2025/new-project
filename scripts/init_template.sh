#!/bin/bash
# Template initialization script for new projects

set -e

echo "🎯 Python Project Template - Initialization"
echo ""

# 1. Ask for project name
read -p "📝 New project name (lowercase-with-dashes): " PROJECT_NAME

if [ -z "$PROJECT_NAME" ]; then
    echo "❌ Project name is required"
    exit 1
fi

PROJECT_NAME_UNDERSCORE=$(echo "$PROJECT_NAME" | tr '-' '_')

echo ""
echo "📦 Creating project: $PROJECT_NAME"
echo ""

# 2. Replace all occurrences
echo "🔄 Replacing 'new-project' with '$PROJECT_NAME'..."
find . -type f \( -name "*.py" -o -name "*.toml" -o -name "*.md" -o -name "*.json" -o -name "Makefile" \) \
    -not -path "./.venv/*" -not -path "./.git/*" \
    -exec sed -i '' "s/new-project/$PROJECT_NAME/g" {} \;

echo "🔄 Replacing 'new_project' with '$PROJECT_NAME_UNDERSCORE'..."
find . -type f \( -name "*.py" -o -name "*.toml" \) \
    -not -path "./.venv/*" -not -path "./.git/*" \
    -exec sed -i '' "s/new_project/$PROJECT_NAME_UNDERSCORE/g" {} \;

# 3. Clean git history
echo "🧹 Cleaning git history..."
rm -rf .git
git init -q
git add .
git commit -q -m "Initial commit from template"

# 4. Clean old build artifacts
echo "🧹 Cleaning build artifacts..."
rm -rf .pytest_cache .ruff_cache .coverage src/*.egg-info
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

# 5. Setup virtual environment
echo "📦 Setting up virtual environment..."
python3 -m venv .venv
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q -e .

# 6. Install pre-commit hooks
echo "🪝 Installing pre-commit hooks..."
pre-commit install -q

echo ""
echo "✅ Project initialized successfully!"
echo ""
echo "📝 Next steps:"
echo "  1. Update description in pyproject.toml"
echo "  2. Update README.md with your project details"
echo "  3. Create GitHub repository:"
echo "     git remote add origin https://github.com/YOUR_USERNAME/$PROJECT_NAME.git"
echo "     git push -u origin main"
echo ""
echo "🚀 Start developing:"
echo "  source .venv/bin/activate"
echo "  make test"
echo ""
