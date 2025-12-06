"""Command-line interface for new-project."""

import argparse
import sys
from pathlib import Path

from src.example import hello, add
from src.utils import get_logger, setup_logging


logger = get_logger(__name__)


def cli() -> argparse.ArgumentParser:
    """
    Create CLI argument parser.
    
    Returns:
        Configured ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog="new-project",
        description="A minimal Python project scaffold",
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.4",
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Hello command
    hello_parser = subparsers.add_parser("hello", help="Print a greeting")
    hello_parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=int, help="First number")
    add_parser.add_argument("b", type=int, help="Second number")
    
    return parser


def main(argv=None) -> int:
    """
    Main CLI entry point.
    
    Args:
        argv: Command-line arguments (for testing)
        
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parser = cli()
    args = parser.parse_args(argv)
    
    # Setup logging
    log_level = "DEBUG" if args.verbose else "INFO"
    setup_logging(level=log_level)
    
    if not args.command:
        parser.print_help()
        return 0
    
    try:
        if args.command == "hello":
            result = hello(args.name)
            print(result)
            logger.info(f"Greeted: {args.name}")
            
        elif args.command == "add":
            result = add(args.a, args.b)
            print(f"{args.a} + {args.b} = {result}")
            logger.info(f"Calculated: {args.a} + {args.b} = {result}")
        
        return 0
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
