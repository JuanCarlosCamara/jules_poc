"""
Unit tests for the Core Main Module.
"""
from hello_jules.main import get_greeting, main


def test_get_greeting() -> None:
    """
    Test that get_greeting returns the exact expected string.
    """
    assert get_greeting() == "Hello World"


def test_main(capsys) -> None:
    """
    Test that main prints the correct greeting to stdout.
    """
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"
