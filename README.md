# hello-jules

`hello-jules` is a simple "Hello World" application and command-line tool implemented in Python.

## Installation

You can install the package using `pip` from the repository root:

```bash
pip install .
```

This will install the package and its dependencies, making the `hello-jules` command available in your environment.

## Usage

Once installed, you can run the CLI tool from anywhere:

```bash
# Prints the default greeting
hello-jules

# Prints a custom greeting
hello-jules "Hi Jules"
```

The tool accepts an optional positional argument for the greeting message. By default, it prints "Hello World".

## Development

The project uses a `src`-layout and requires `pytest` for unit testing and `flake8` for PEP 8 style enforcement. Dependencies are managed via `requirements.txt`.

### Setup

To set up the development environment, install the dependencies:

```bash
pip install -r requirements.txt
```

### Running Tests

To run the unit tests without prior installation of the package, use:

```bash
PYTHONPATH=src pytest
```

### Linting

To check the code for PEP 8 compliance, run:

```bash
flake8 src tests
```

### Architecture

- Core main logic is found in `src/hello_jules/main.py`.
- Tests are located in the `tests/` directory.
- Build artifacts are excluded via `.gitignore`.
- Configuration and entry points are defined in `pyproject.toml`.
