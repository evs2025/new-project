# Python Project Template

> Professional Python project starter with CLI, testing, and automation

## 🚀 Quick Start für neues Projekt

### 1. Template kopieren
```bash
cp -r new-project my-new-project
cd my-new-project
```

### 2. Projekt umbenennen
```bash
# Namen in allen Files ersetzen:
find . -type f -name "*.py" -o -name "*.toml" -o -name "*.md" | \
  xargs sed -i '' 's/new-project/my-new-project/g'
  
find . -type f -name "*.py" -o -name "*.toml" -o -name "*.md" | \
  xargs sed -i '' 's/new_project/my_new_project/g'
```

### 3. Git neu initialisieren
```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit from template"
```

### 4. GitHub Repository erstellen
```bash
# Auf GitHub: New Repository → my-new-project
git remote add origin https://github.com/DEIN_USERNAME/my-new-project.git
git branch -M main
git push -u origin main
```

### 5. Setup
```bash
make setup
make test
```

## 📦 Was ist drin?

### Structure
```
my-new-project/
├── src/              # Dein Code
│   ├── example.py    # Beispiel-Modul (umbenennen/löschen)
│   ├── cli/          # CLI commands
│   └── utils/        # Logger, Config
├── tests/            # Unit tests
├── examples/         # Usage examples
├── docs/             # Documentation
└── scripts/          # Automation scripts
```

### Features
- ✅ **CLI Tool** mit argparse
- ✅ **Logging** mit rotating file handler
- ✅ **Config Management** (JSON/YAML)
- ✅ **Testing** mit pytest (84% coverage)
- ✅ **Code Quality** (black, isort, ruff)
- ✅ **Pre-commit hooks** (auto-format)
- ✅ **Makefile** (automation)
- ✅ **GitHub** ready

## 🔧 Development Workflow

```bash
# 1. Code schreiben
vim src/my_module.py

# 2. Tests schreiben
vim tests/test_my_module.py

# 3. Tests laufen lassen
make test

# 4. Code formatieren
make format

# 5. Linting
make lint

# 6. Committen (pre-commit hooks laufen automatisch)
git add .
git commit -m "feat: add new feature"
git push
```

## 📝 Anpassungen

### pyproject.toml
```toml
[project]
name = "my-new-project"  # ← ÄNDERN
version = "0.1.0"
description = "My awesome project"  # ← ÄNDERN

[project.scripts]
my-command = "src.cli.main:main"  # ← ÄNDERN
```

### README.md
- Projekt-Beschreibung anpassen
- Features dokumentieren
- Installation-Instructions updaten

### src/example.py
- Umbenennen zu deinem Modul
- Eigenen Code schreiben
- In `__init__.py` exportieren

### tests/
- Tests für deine Module schreiben
- Naming: `test_<modul>.py`

## 🎯 Makefile Commands

| Command | Beschreibung |
|---------|--------------|
| `make setup` | Virtual env + dependencies + hooks |
| `make test` | Run tests with coverage |
| `make coverage` | HTML coverage report |
| `make format` | Format code (black + isort) |
| `make lint` | Lint code (ruff) |
| `make demo` | Run demo script |
| `make clean` | Clean caches |
| `make run-examples` | Run all examples |

## 📚 File Descriptions

- `.coveragerc` - Coverage config
- `.gitignore` - Git ignore patterns
- `.pre-commit-config.yaml` - Git hooks
- `pyrightconfig.json` - Type checker config
- `.vscode/settings.json` - VS Code settings
- `pyproject.toml` - Project metadata
- `requirements.txt` - Python dependencies
- `Makefile` - Automation commands
- `LICENSE` - MIT License

## 🔄 Updates vom Template holen

```bash
# Template updates mergen
git remote add template /path/to/new-project
git fetch template
git merge template/main --allow-unrelated-histories
```

## 💡 Best Practices

1. **Versionierung**: Semantic Versioning (0.1.0 → 0.2.0 → 1.0.0)
2. **Commits**: Conventional Commits (`feat:`, `fix:`, `chore:`)
3. **Tests**: Immer tests schreiben (Ziel: >80% coverage)
4. **Documentation**: README + docstrings aktuell halten
5. **CI/CD**: GitHub Actions für Tests (optional)

## 🚀 Deployment

### PyPI Package
```bash
python -m build
python -m twine upload dist/*
```

### Docker
```dockerfile
FROM python:3.14-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["my-command"]
```

## 📄 License

MIT License - siehe LICENSE file

---

**Happy Coding! 🎉**
