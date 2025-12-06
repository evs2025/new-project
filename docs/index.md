# new-project Documentation

## Overview

Minimal Python project scaffold with best practices for quick development.

## Features

- ✅ Modern Python packaging with `pyproject.toml`
- ✅ Pre-commit hooks (black, isort, ruff)
- ✅ VS Code configuration
- ✅ Clean project structure
- ✅ MIT License

## Development Workflow

### 1. Initial Setup
```bash
./scripts/setup.sh
```

### 2. Development Cycle
```bash
# Activate environment
source .venv/bin/activate

# Make changes in src/
# Add tests in tests/

# Run tests
pytest -v

# Format code (automatic with pre-commit)
pre-commit run --all-files
```

### 3. Version Management
Update version in `pyproject.toml` and create git tag:
```bash
git tag -a v0.X.X -m "Version 0.X.X"
git push origin v0.X.X
```

## Project Structure Explained

```
new-project/
├── src/              # Your Python modules
│   └── __init__.py
├── tests/            # Unit tests (pytest)
│   ├── __init__.py
│   └── test_example.py
├── docs/             # Documentation
│   └── index.md
├── scripts/          # Helper scripts
│   ├── setup.sh      # Project setup
│   └── clean.sh      # Clean caches
├── .venv/            # Virtual environment (local, not in git)
├── .vscode/          # VS Code settings
├── pyproject.toml    # Project metadata
├── .pre-commit-config.yaml  # Code quality hooks
├── .gitignore        # Git exclusions
├── LICENSE           # MIT License
└── README.md         # Main documentation
```

## Dependencies

Managed in `pyproject.toml`:
- **Runtime**: Listed in `dependencies`
- **Development**: Pre-commit hooks (black, isort, ruff)
- **Testing**: pytest

## Code Quality

Pre-commit hooks run automatically on `git commit`:
- **black**: Code formatting
- **isort**: Import sorting
- **ruff**: Fast Python linter
- **trailing-whitespace**: Remove trailing spaces
- **end-of-file-fixer**: Ensure newline at EOF
- **check-yaml**: Validate YAML files

Run manually:
```bash
pre-commit run --all-files
```

## Testing

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_example.py

# Run with coverage
pytest --cov=src
```

## Maintenance

### Clean Caches
```bash
./scripts/clean.sh
```

### Update Dependencies
```bash
pip install --upgrade pip
pip install -e . --upgrade
pip freeze > requirements.txt
```

## License

MIT License - see LICENSE file for details.
