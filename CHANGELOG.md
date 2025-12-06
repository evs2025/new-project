# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4] - 2025-12-06

### Added
- **CLI Module** (`src/cli/`): Command-line interface with argparse
  - `hello` command with optional name parameter
  - `add` command for adding two numbers
  - Verbose flag for debugging output
  - Entry point: `new-project` command installed globally
- **Utils Module** (`src/utils/`):
  - `logger.py`: Logging setup and logger factory with file/console support
  - `config.py`: JSON/YAML config management with save/load functions
- **Examples** (`examples/`): 3 working example scripts
  - `basic_usage.py`: Demo of hello and add functions
  - `with_config.py`: Config load/save demonstration
  - `cli_demo.py`: CLI interface examples
- **Comprehensive Tests** (`tests/`):
  - `test_cli/test_main.py`: 6 tests for CLI interface
  - `test_utils/test_logger.py`: 4 tests for logging setup
  - `test_utils/test_config.py`: 4 tests for config management
  - Total: 18 tests, 100% pass rate, 84% code coverage
- **Documentation**:
  - `docs/api.md`: Complete API reference with examples
  - `docs/examples.md`: Usage patterns and best practices
- **Configuration**:
  - `.coveragerc`: Coverage configuration for pytest-cov
  - Updated `Makefile` with `coverage` and `run-examples` targets

### Changed
- `pyproject.toml`: Bumped version to 0.1.4, added CLI entry point
- `README.md`: Updated with new features, CLI usage, and examples
- Test coverage improved from 71% to 84%
- Project structure expanded from 2 to 8 source files

### Improved
- More modular code organization with utils and cli packages
- Better separation of concerns (logging, config, CLI)
- Executable examples for quick start
- Enhanced test suite (4 → 18 tests)

## [0.1.3] - 2025-12-06

### Added
- Makefile for easy command execution (make test, make demo, etc.)
- `scripts/test.sh` with coverage support and linting
- `scripts/demo.py` to demonstrate project features
- Example code in `src/example.py` (hello, add functions)
- Comprehensive tests in `tests/test_example.py` (4 tests, 100% pass)
- pytest-cov dependency for test coverage
- Complete automation workflow

### Changed
- Improved README with detailed workflow and commands table
- Enhanced documentation with Makefile commands
- Updated development workflow to be fully automated

### Improved
- Pre-commit hooks now run automatically on commit
- Test suite includes coverage reporting (71% coverage)
- All scripts are executable and tested

## [0.1.2] - 2025-12-06

### Fixed
- Improved `.gitignore` with complete Python best practices
- Removed `.vscode/` from git tracking (IDE-specific)
- Cleaned up `*.egg-info` and `__pycache__` from repository

### Changed
- More comprehensive `.gitignore` patterns
- Better coverage for virtual environments, caches, IDEs

## [0.1.1] - 2025-12-06

### Added
- Project structure with `docs/` and `scripts/` folders
- Setup script (`scripts/setup.sh`) for easy project initialization
- Clean script (`scripts/clean.sh`) for removing caches
- Comprehensive documentation in `docs/index.md`
- Better README with emojis and clearer structure

### Removed
- GitHub Actions workflow (to avoid costs)

### Changed
- Improved `.gitignore` (added `.ruff_cache`)
- Updated README with better Quick Start guide

## [0.1.0] - 2025-12-06

### Added
- Initial project structure
- Python packaging with `pyproject.toml`
- Pre-commit hooks (black, isort, ruff)
- VS Code configuration
- MIT License
- Basic test setup with pytest
- GitHub repository integration
