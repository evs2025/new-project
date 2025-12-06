# new-project

Minimal Python project scaffold created for quick iteration.

## Setup (local development)

1. Create and activate the virtual environment (done already by this repo):

```bash
cd "$(dirname "$0")"
python3 -m venv .venv
source .venv/bin/activate
```

2. Install editable package and dependencies:

```bash
pip install --upgrade pip setuptools wheel
pip install -e .
```

3. (Optional) Recreate `requirements.txt` from the venv:

```bash
pip freeze > requirements.txt
```

## Run tests

```bash
pytest
```

## VS Code

- The project contains `.vscode/settings.json` configured to use the project `.venv` interpreter.
- If VS Code still shows another interpreter, open `Cmd+Shift+P` → `Python: Select Interpreter` and choose:

`/Users/bosko/Documents/Main/Projekte/play-dynamic/Apps/Bosko-Workspace/Project/new-project/.venv/bin/python`

## Git

- `.gitignore` is included and ignores `.venv`, cache files and builds.

If you want, I can also add a `pre-commit` config and a license.
