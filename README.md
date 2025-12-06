# new-project

> Minimal Python project scaffold v0.1.4

## 📁 Projektstruktur

```
new-project/
├── src/              # Source code
│   ├── __init__.py
│   ├── example.py    # Example module
│   ├── cli/          # CLI interface
│   │   ├── __init__.py
│   │   └── main.py
│   └── utils/        # Utility modules
│       ├── __init__.py
│       ├── config.py
│       └── logger.py
├── tests/            # Unit tests (18 tests, 100% pass)
│   ├── __init__.py
│   ├── test_example.py
│   ├── test_cli/
│   │   └── test_main.py
│   └── test_utils/
│       ├── test_config.py
│       └── test_logger.py
├── examples/         # Usage examples
│   ├── basic_usage.py
│   ├── with_config.py
│   └── cli_demo.py
├── docs/             # Documentation
│   ├── index.md
│   ├── api.md
│   └── examples.md
├── scripts/          # Helper scripts
│   ├── setup.sh      # Auto setup
│   ├── clean.sh      # Clean caches
│   └── demo.py       # Demo script
├── .venv/            # Virtual environment (local)
├── Makefile          # Build automation
├── pyproject.toml    # Project metadata & dependencies
├── .pre-commit-config.yaml  # Code quality hooks
└── README.md
```

## 🚀 Quick Start

### Option 1: Automatisches Setup (Empfohlen)

```bash
# Einmal ausführen - installiert alles
make setup
# oder: ./scripts/setup.sh

# Demo ausführen
make demo

# CLI verwenden
new-project hello --name "World"
new-project add 5 3

# Tests ausführen
make test
```

### Option 2: Manuelles Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pre-commit install
pytest -v
```

## ✨ Features

- **CLI Interface**: Command-line tool with `hello` and `add` commands
- **Utils Module**: Logger and config management
- **Examples**: 3 working examples to get started
- **Comprehensive Tests**: 18 tests with 84% coverage
- **Makefile**: Automated commands for common tasks
- **Pre-commit Hooks**: Auto-formatting with black, isort, ruff

## 💻 Entwicklung

**VS Code öffnen** (venv ist bereits konfiguriert):
```bash
code .
```

**CLI verwenden:**
```bash
# Nach Installation (make setup)
new-project hello
new-project hello --name "Python"
new-project add 10 20
new-project --help
```

**Examples ausführen:**
```bash
make run-examples
# oder einzeln:
python examples/basic_usage.py
python examples/with_config.py
python examples/cli_demo.py
```

**Neues Modul erstellen:**
1. Datei in `src/` anlegen
2. Tests in `tests/` schreiben
3. `pytest -v` ausführen

**Code formatieren** (automatisch bei commit):
```bash
pre-commit run --all-files
```

## 📝 Development Workflow

```bash
# 1. Environment aktivieren
source .venv/bin/activate

# 2. Code schreiben in src/

# 3. Tests schreiben in tests/

# 4. Tests ausführen
pytest -v

# 5. Commit (formatiert automatisch)
git add .
git commit -m "feat: deine Änderung"
git push origin main
```

## 🔧 Verfügbare Befehle

| Befehl | Beschreibung |
|--------|--------------|
| `make setup` | Projekt setup (venv + deps + hooks) |
| `make test` | Tests ausführen mit Coverage |
| `make demo` | Demo script ausführen |
| `make run-examples` | Alle Examples ausführen |
| `make format` | Code formatieren (black + isort) |
| `make lint` | Code prüfen (ruff + black check) |
| `make clean` | Caches und temporäre Dateien löschen |
| `make coverage` | Detaillierte Coverage-Report |
| `./scripts/setup.sh` | Setup script (alternativ) |
| `./scripts/clean.sh` | Clean script (alternativ) |
| `pytest` | Tests ausführen |
| `pytest -v --cov=src` | Tests mit Coverage-Details |
| `new-project --help` | CLI Hilfe anzeigen |

## 📚 Dokumentation

- [API Documentation](docs/api.md) - Detaillierte API-Referenz
- [Examples Guide](docs/examples.md) - Usage examples und patterns
- [Project Index](docs/index.md) - Projekt-Übersicht

## 📦 Dependencies

- Python ≥3.8
- pytest (testing)
- black (formatting)
- isort (import sorting)
- ruff (linting)
- pre-commit (hooks)

## 🔗 Links

- GitHub: https://github.com/evs2025/new-project
- Issues: https://github.com/evs2025/new-project/issues
- Docs: [docs/index.md](docs/index.md)
