#!/usr/bin/env python3
"""Basic usage example for new-project."""

import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.example import hello, add

print("=" * 50)
print("📝 Basic Usage Example")
print("=" * 50)
print()

# Use hello function
print("1. Hello function:")
print(f"   {hello()}")
print(f"   {hello('Alice')}")
print()

# Use add function
print("2. Add function:")
print(f"   2 + 3 = {add(2, 3)}")
print(f"   10 + 20 = {add(10, 20)}")
print()

print("=" * 50)
print("✅ Basic usage complete!")
print("=" * 50)
