#!/usr/bin/env python3
"""Example using the CLI interface."""

import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.cli import main

print("=" * 50)
print("🖥️  CLI Example")
print("=" * 50)
print()

# Example 1: Hello command
print("1. Running: new-project hello Alice")
main(["hello", "Alice"])
print()

# Example 2: Add command
print("2. Running: new-project add 15 27")
main(["add", "15", "27"])
print()

# Example 3: Verbose mode
print("3. Running: new-project --verbose hello Python")
main(["--verbose", "hello", "Python"])
print()

print("=" * 50)
print("✅ CLI example complete!")
print("=" * 50)
