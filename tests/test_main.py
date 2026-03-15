"""
Unit tests for the Core Main Module.
"""
import pytest
from hello_jules.main import get_greeting, main


@pytest.mark.parametrize("message, expected", [
    (None, "Hello World"),
    ("Bye World", "Bye World"),
])
def test_get_greeting(message: str | None, expected: str) -> None:
    """
    Test that get_greeting returns the exact expected string.
    """
    if message is None:
        assert get_greeting() == expected
    else:
        assert get_greeting(message) == expected


@pytest.mark.parametrize("args, expected", [
    ([], "Hello World"),
    (["Bye World"], "Bye World"),
    (["Hello", "there,", "World"], "Hello there, World"),
])
def test_main_args(capsys, args: list[str], expected: str) -> None:
    """
    Test that main prints the correct message to stdout.
    """
    main(args)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


def test_main_sys_argv(monkeypatch, capsys) -> None:
    """
    Test that main correctly uses sys.argv when args is None.
    """
    monkeypatch.setattr("sys.argv", ["hello-jules", "Monkey", "Patch"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Monkey Patch"
