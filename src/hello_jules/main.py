"""
Core Main Module for the Hello World application.
"""
from __future__ import annotations


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
        import sys
        args = sys.argv[1:]

    # Fast-path for common invocations to avoid argparse import overhead
    # Removing typing import and using __future__ saves ~20ms of startup time.
    if len(args) == 0:
        print(get_greeting())
        return
    elif len(args) == 1 and not args[0].startswith("-"):
        print(get_greeting(args[0]))
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
    print(greeting)


if __name__ == "__main__":
    main()
