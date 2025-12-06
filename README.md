# new-project

> Minimal Python project scaffold v0.1.3

## 📁 Projektstruktur

```
new-project/
├── src/              # Source code
│   ├── __init__.py
│   └── example.py    # Example module
├── tests/            # Unit tests
│   ├── __init__.py
│   └── test_example.py
├── docs/             # Documentation
│   └── index.md
├── scripts/          # Helper scripts
│   ├── setup.sh      # Auto setup
│   ├── clean.sh      # Clean caches
│   └── demo.py       # Demo script
├── .venv/            # Virtual environment (local)
├── pyproject.toml    # Project metadata & dependencies
├── .pre-commit-config.yaml  # Code quality hooks
└── README.md
```

## 🚀 Quick Start

### Option 1: Automatisches Setup (Empfohlen)

```bash
# Einmal ausführen - installiert alles
./scripts/setup.sh

# Demo ausführen
python scripts/demo.py

# Tests ausführen
pytest -v
```

### Option 2: Manuelles Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pre-commit install
pytest -v
```

## 💻 Entwicklung

**VS Code öffnen** (venv ist bereits konfiguriert):
```bash
code .
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
| `./scripts/setup.sh` | Projekt setup (venv + deps + hooks) |
| `./scripts/clean.sh` | Caches löschen |
| `python scripts/demo.py` | Demo ausführen |
| `pytest` | Tests ausführen |
| `pytest -v` | Tests mit Details |
| `pytest --cov=src` | Tests mit Coverage |
| `pre-commit run --all-files` | Code formatieren |

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
