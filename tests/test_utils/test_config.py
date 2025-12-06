"""Tests for config utility."""

import tempfile
from pathlib import Path

import pytest

from src.utils.config import load_config, save_config


def test_save_and_load_json():
    """Test saving and loading JSON config."""
    config = {"key": "value", "number": 42}

    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / "config.json"

        save_config(config, config_path)
        assert config_path.exists()

        loaded = load_config(config_path)
        assert loaded == config


def test_load_nonexistent_file():
    """Test loading non-existent config file."""
    with pytest.raises(FileNotFoundError):
        load_config(Path("/nonexistent/config.json"))


def test_unsupported_format():
    """Test unsupported config format."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / "config.txt"
        config_path.write_text("test")

        with pytest.raises(ValueError, match="Unsupported config format"):
            load_config(config_path)


def test_save_creates_parent_dirs():
    """Test that save_config creates parent directories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / "subdir" / "config.json"
        config = {"test": True}

        save_config(config, config_path)
        assert config_path.exists()
        assert config_path.parent.exists()
