"""
Core Main Module for the Hello World application.
"""
from __future__ import annotations  # Optimization: avoid typing module overhead
import sys


def get_greeting(message: str = "Hello World") -> str:
    """
    Returns the greeting message.

    Args:
        message (str): The message to return. Defaults to "Hello World".

    Returns:
        str: The provided message.
    """
    return message


def main(args: list[str] | None = None) -> None:
    """
    Calls get_greeting and prints the result to standard output.

    Args:
        args (list[str] | None): Command line arguments.
    """
    if args is None:
        args = sys.argv[1:]

    # Fast-path for common invocations to avoid argparse import overhead
    if len(args) == 0:
        # Optimization: using sys.stdout.write instead of print for reduced I/O overhead
        sys.stdout.write(get_greeting() + '\n')
        return
    elif len(args) == 1 and not args[0].startswith("-"):
        sys.stdout.write(get_greeting(args[0]) + '\n')
        return

    import argparse
    parser = argparse.ArgumentParser(description="Prints a message.")
    parser.add_argument(
        "message",
        nargs="?",
        default="Hello World",
        help="The message to print (default: Hello World)"
    )

    parsed_args = parser.parse_args(args)

    greeting = get_greeting(parsed_args.message)
    sys.stdout.write(greeting + '\n')


if __name__ == "__main__":
    main()
