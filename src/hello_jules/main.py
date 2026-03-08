"""
Core Main Module for the Hello World application.
"""


def get_greeting() -> str:
    """
    Returns a standard greeting string.

    Returns:
        str: The greeting "Hello World".
    """
    return "Hello World"


def main() -> None:
    """
    Calls get_greeting and prints the result to standard output.
    """
    greeting = get_greeting()
    print(greeting)


if __name__ == "__main__":
    main()
