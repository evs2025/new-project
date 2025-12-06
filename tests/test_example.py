"""Tests for example module."""

from src.example import hello, add


def test_example():
    assert True


def test_hello():
    """Test hello function with default parameter."""
    assert hello() == "Hello, World!"


def test_hello_with_name():
    """Test hello function with custom name."""
    assert hello("Alice") == "Hello, Alice!"
    assert hello("Bob") == "Hello, Bob!"


def test_add():
    """Test add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

