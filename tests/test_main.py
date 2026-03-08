"""
Unit tests for the Core Main Module.
"""
from hello_jules.main import get_greeting, main


def test_get_greeting() -> None:
    """
    Test that get_greeting returns the exact expected string.
    """
    assert get_greeting() == "Hello World"
    assert get_greeting("Bye World") == "Bye World"


def test_main_default(capsys) -> None:
    """
    Test that main prints the correct default greeting to stdout.
    """
    main([])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"


def test_main_custom(capsys) -> None:
    """
    Test that main prints the correct custom message to stdout.
    """
    main(["Bye World"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Bye World"
