# new-project

> Minimal Python project scaffold v0.1.1

## 📁 Projektstruktur

```
new-project/
├── src/              # Source code
├── tests/            # Unit tests
├── docs/             # Documentation
├── scripts/          # Helper scripts
├── .venv/            # Virtual environment (local)
├── pyproject.toml    # Project metadata & dependencies
├── .pre-commit-config.yaml  # Code quality hooks
└── README.md
```

## 🚀 Quick Start

### 1. Setup

```bash
# Use the setup script
./scripts/setup.sh

# Or manually:
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pre-commit install
```

### 2. Run Tests

```bash
pytest
```

### 3. Code Quality

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Or manually:
black .
isort .
ruff check . --fix
```

## 💻 VS Code Setup

- `.venv` interpreter is pre-configured in `.vscode/settings.json`
- Press `Cmd+Shift+P` → `Python: Select Interpreter` if needed

## 📝 Development

- Python ≥3.8
- Dependencies managed via `pyproject.toml`
- License: MIT
- Pre-commit hooks for code quality (black, isort, ruff)

## 🔗 Links

- GitHub: https://github.com/evs2025/new-project
- Issues: https://github.com/evs2025/new-project/issues
