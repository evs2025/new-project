"""Configuration management utilities."""

import json
from pathlib import Path
from typing import Any, Dict

try:
    import yaml

    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


def load_config(config_path: Path) -> Dict[str, Any]:
    """
    Load configuration from JSON or YAML file.

    Args:
        config_path: Path to configuration file

    Returns:
        Configuration dictionary

    Raises:
        ValueError: If file format is not supported
        FileNotFoundError: If config file doesn't exist
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    suffix = config_path.suffix.lower()

    with open(config_path, "r", encoding="utf-8") as f:
        if suffix == ".json":
            return json.load(f)
        elif suffix in (".yaml", ".yml"):
            if not YAML_AVAILABLE:
                raise ValueError(
                    "PyYAML not installed. Install with: pip install pyyaml"
                )
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported config format: {suffix}")


def save_config(config: Dict[str, Any], config_path: Path) -> None:
    """
    Save configuration to JSON or YAML file.

    Args:
        config: Configuration dictionary
        config_path: Path to save configuration file

    Raises:
        ValueError: If file format is not supported
    """
    config_path.parent.mkdir(parents=True, exist_ok=True)
    suffix = config_path.suffix.lower()

    with open(config_path, "w", encoding="utf-8") as f:
        if suffix == ".json":
            json.dump(config, f, indent=2)
        elif suffix in (".yaml", ".yml"):
            if not YAML_AVAILABLE:
                raise ValueError(
                    "PyYAML not installed. Install with: pip install pyyaml"
                )
            yaml.dump(config, f, default_flow_style=False)
        else:
            raise ValueError(f"Unsupported config format: {suffix}")
