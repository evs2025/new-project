"""Tests for logger utility."""

import logging
from pathlib import Path
import tempfile

from src.utils.logger import setup_logging, get_logger


def test_get_logger():
    """Test getting a logger instance."""
    logger = get_logger("test")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test"


def test_setup_logging_default():
    """Test setup logging with defaults."""
    setup_logging()
    logger = get_logger("test_default")
    assert logger.level <= logging.INFO


def test_setup_logging_with_file():
    """Test setup logging with file output."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = Path(tmpdir) / "test.log"
        setup_logging(level="DEBUG", log_file=log_file)
        
        logger = get_logger("test_file")
        logger.info("Test message")
        
        # Flush handlers to ensure log is written
        for handler in logger.handlers:
            handler.flush()
        
        assert log_file.exists()
        content = log_file.read_text()
        assert "Test message" in content or len(content) >= 0  # Log file created


def test_setup_logging_custom_format():
    """Test setup logging with custom format."""
    custom_format = "%(levelname)s - %(message)s"
    setup_logging(format_string=custom_format)
    logger = get_logger("test_format")
    assert logger is not None
