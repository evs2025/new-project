# Examples

## Basic Usage

Simple example showing core functions:

```python
from src.example import hello, add

# Greet someone
print(hello("Alice"))  # "Hello, Alice!"

# Add numbers
result = add(10, 20)   # 30
```

**Run:**
```bash
python examples/basic_usage.py
```

---

## Configuration Management

Example using config utilities:

```python
from pathlib import Path
from src.utils.config import load_config, save_config

# Create config
config = {
    "app_name": "my-app",
    "version": "1.0.0",
    "settings": {
        "debug": True
    }
}

# Save to JSON
save_config(config, Path("config.json"))

# Load back
loaded = load_config(Path("config.json"))
print(loaded["app_name"])
```

**Run:**
```bash
python examples/with_config.py
```

---

## CLI Usage

Using the command-line interface:

```bash
# Show help
new-project --help

# Hello command
new-project hello Alice

# Add command
new-project add 15 27

# Verbose logging
new-project --verbose hello Python
```

**Programmatic:**
```python
from src.cli import main

# Run commands programmatically
main(["hello", "Alice"])
main(["add", "15", "27"])
```

**Run:**
```bash
python examples/cli_demo.py
```

---

## Logging

Setup and use logging:

```python
from pathlib import Path
from src.utils.logger import setup_logging, get_logger

# Setup logging
setup_logging(
    level="DEBUG",
    log_file=Path("app.log")
)

# Get logger
logger = get_logger(__name__)

# Use it
logger.info("Application started")
logger.debug("Debug information")
logger.error("An error occurred")
```

---

## Complete Workflow

```python
from pathlib import Path
from src.example import hello
from src.utils.logger import setup_logging, get_logger
from src.utils.config import load_config

# 1. Setup logging
setup_logging(level="INFO")
logger = get_logger(__name__)

# 2. Load configuration
config = load_config(Path("config.json"))
logger.info(f"Loaded config for: {config['app_name']}")

# 3. Run your code
name = config.get("user_name", "World")
greeting = hello(name)
print(greeting)

logger.info("Application complete")
```
