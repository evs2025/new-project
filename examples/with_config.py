#!/usr/bin/env python3
"""Example using configuration management."""

import sys
import tempfile
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.config import load_config, save_config

print("=" * 50)
print("⚙️  Configuration Example")
print("=" * 50)
print()

# Create a temporary config
config = {
    "app_name": "new-project",
    "version": "0.1.4",
    "settings": {
        "debug": True,
        "log_level": "INFO",
    },
}

# Save to JSON
with tempfile.TemporaryDirectory() as tmpdir:
    config_path = Path(tmpdir) / "config.json"

    print("1. Saving configuration to JSON...")
    save_config(config, config_path)
    print(f"   Saved to: {config_path}")
    print()

    print("2. Loading configuration...")
    loaded_config = load_config(config_path)
    print(f"   App name: {loaded_config['app_name']}")
    print(f"   Version: {loaded_config['version']}")
    print(f"   Debug: {loaded_config['settings']['debug']}")
    print()

print("=" * 50)
print("✅ Configuration example complete!")
print("=" * 50)
