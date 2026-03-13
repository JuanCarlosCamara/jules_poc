"""
Core Main Module for the Hello World application.
"""


def get_greeting(message: str = "Hello World") -> str:
    """
    Returns the greeting message.

    Args:
        message (str): The message to return. Defaults to "Hello World".

    Returns:
        str: The provided message.
    """
    return message


# Optimization: Using Python 3.10+ native types avoids 'typing'
# import overhead (~20ms)
def main(args: list[str] | None = None) -> None:
    """
    Calls get_greeting and prints the result to standard output.

    Args:
        args (list[str] | None): Command line arguments.
    """
    if args is None:
        import sys
        args = sys.argv[1:]

    # Fast-path for common invocations to avoid argparse import
    # overhead (~20ms).
    # Optimization: Handles multi-word positional arguments
    # directly in the fast-path.
    if len(args) == 0:
        print(get_greeting())
        return
    elif len(args) > 0 and not any(arg.startswith("-") for arg in args):
        print(get_greeting(" ".join(args)))
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
