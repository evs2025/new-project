# API Documentation

## Modules

### `src.example`

Basic example functions.

#### `hello(name: str = "World") -> str`

Return a greeting message.

**Parameters:**
- `name` (str): The name to greet (default: "World")

**Returns:**
- str: A greeting string

**Example:**
```python
from src.example import hello

print(hello())          # "Hello, World!"
print(hello("Alice"))   # "Hello, Alice!"
```

#### `add(a: int, b: int) -> int`

Add two numbers.

**Parameters:**
- `a` (int): First number
- `b` (int): Second number

**Returns:**
- int: The sum of a and b

**Example:**
```python
from src.example import add

result = add(2, 3)  # 5
```

---

### `src.utils.logger`

Logging utilities.

#### `setup_logging(level: str = "INFO", log_file: Optional[Path] = None, format_string: Optional[str] = None) -> None`

Setup logging configuration.

**Parameters:**
- `level` (str): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `log_file` (Optional[Path]): Optional file path to write logs to
- `format_string` (Optional[str]): Optional custom format string

**Example:**
```python
from pathlib import Path
from src.utils.logger import setup_logging

setup_logging(level="DEBUG", log_file=Path("app.log"))
```

#### `get_logger(name: str) -> logging.Logger`

Get a logger instance.

**Parameters:**
- `name` (str): Logger name (usually __name__)

**Returns:**
- logging.Logger: Configured logger instance

**Example:**
```python
from src.utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Application started")
```

---

### `src.utils.config`

Configuration management utilities.

#### `load_config(config_path: Path) -> Dict[str, Any]`

Load configuration from JSON or YAML file.

**Parameters:**
- `config_path` (Path): Path to configuration file

**Returns:**
- Dict[str, Any]: Configuration dictionary

**Raises:**
- ValueError: If file format is not supported
- FileNotFoundError: If config file doesn't exist

**Example:**
```python
from pathlib import Path
from src.utils.config import load_config

config = load_config(Path("config.json"))
print(config["app_name"])
```

#### `save_config(config: Dict[str, Any], config_path: Path) -> None`

Save configuration to JSON or YAML file.

**Parameters:**
- `config` (Dict[str, Any]): Configuration dictionary
- `config_path` (Path): Path to save configuration file

**Raises:**
- ValueError: If file format is not supported

---

### `src.cli.main`

Command-line interface.

#### `main(argv=None) -> int`

Main CLI entry point.

**Parameters:**
- `argv` (Optional[List[str]]): Command-line arguments (for testing)

**Returns:**
- int: Exit code (0 for success, non-zero for error)

**CLI Usage:**
```bash
# Hello command
new-project hello Alice

# Add command
new-project add 5 10

# Verbose mode
new-project --verbose hello Python
```
