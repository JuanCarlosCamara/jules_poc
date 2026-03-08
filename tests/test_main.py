"""
Unit tests for the Core Main Module.
"""
from hello_jules.main import get_greeting, main


def test_get_greeting() -> None:
    """
    Test that get_greeting returns the exact expected string with default and custom name.
    """
    assert get_greeting() == "Hello World"
    assert get_greeting("Jules") == "Hello Jules"


def test_main_default(capsys) -> None:
    """
    Test that main prints the correct default greeting to stdout.
    """
    main([])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"


def test_main_custom(capsys) -> None:
    """
    Test that main prints the correct custom greeting to stdout.
    """
    main(["Jules"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello Jules"
