"""
Core Main Module for the Hello World application.
"""
import argparse
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
