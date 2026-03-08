"""
Core Main Module for the Hello World application.
"""
import argparse
from typing import List, Optional


def get_greeting(name: str = "World") -> str:
    """
    Returns a standard greeting string.

    Args:
        name (str): The name to greet. Defaults to "World".

    Returns:
        str: The greeting "Hello {name}".
    """
    return f"Hello {name}"


def main(args: Optional[List[str]] = None) -> None:
    """
    Calls get_greeting and prints the result to standard output.

    Args:
        args (Optional[List[str]]): Command line arguments.
    """
    parser = argparse.ArgumentParser(description="Greets the user.")
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="The name to greet (default: World)"
    )

    parsed_args = parser.parse_args(args)

    greeting = get_greeting(parsed_args.name)
    print(greeting)


if __name__ == "__main__":
    main()
