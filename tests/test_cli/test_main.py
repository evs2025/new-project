"""Tests for CLI main module."""

from src.cli.main import cli, main


def test_cli_parser():
    """Test CLI parser creation."""
    parser = cli()
    assert parser is not None
    assert parser.prog == "new-project"


def test_main_no_command():
    """Test main with no command."""
    result = main([])
    assert result == 0


def test_main_hello_default():
    """Test hello command with default name."""
    result = main(["hello"])
    assert result == 0


def test_main_hello_with_name():
    """Test hello command with custom name."""
    result = main(["hello", "Alice"])
    assert result == 0


def test_main_add():
    """Test add command."""
    result = main(["add", "5", "10"])
    assert result == 0


def test_main_verbose():
    """Test verbose flag."""
    result = main(["--verbose", "hello", "Test"])
    assert result == 0
