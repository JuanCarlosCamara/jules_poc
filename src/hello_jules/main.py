"""
Core Main Module for the Hello World application.
"""
import sys
from typing import List, Optional


def get_greeting(message: str = "Hello World") -> str:
    """
    Returns the greeting message.

    Args:
        message (str): The message to return. Defaults to "Hello World".

    Returns:
        str: The provided message.
    """
    return message


def main(args: Optional[List[str]] = None) -> None:
    """
    Calls get_greeting and prints the result to standard output.

    Args:
        args (Optional[List[str]]): Command line arguments.
    """
    # Fast path for simple invocations to save ~13ms of argparse import time
    check_args = sys.argv[1:] if args is None else args

    if len(check_args) == 0:
        print(get_greeting())
        return
    elif len(check_args) == 1 and check_args[0] not in ("-h", "--help"):
        print(get_greeting(check_args[0]))
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
