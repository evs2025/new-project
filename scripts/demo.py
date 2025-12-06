#!/usr/bin/env python3
"""
Demo script for new-project.

Run this to see the project in action!
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.example import hello, add


def main():
    """Main demo function."""
    print("=" * 50)
    print("🚀 new-project Demo")
    print("=" * 50)
    print()
    
    # Demo hello function
    print("📝 Testing hello() function:")
    print(f"   {hello()}")
    print(f"   {hello('Python')}")
    print(f"   {hello('Developer')}")
    print()
    
    # Demo add function
    print("🔢 Testing add() function:")
    numbers = [(2, 3), (10, 20), (-5, 5), (0, 100)]
    for a, b in numbers:
        result = add(a, b)
        print(f"   {a} + {b} = {result}")
    print()
    
    print("=" * 50)
    print("✅ All demos completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
