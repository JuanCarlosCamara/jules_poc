## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python Typing Import Overhead
**Learning:** In ultra-fast Python CLI fast-paths (like those skipping `argparse`), simply importing the `typing` module (e.g., `from typing import List, Optional`) can introduce ~26ms of overhead, completely defeating the purpose of the fast-path. In modern Python (3.10+), type hints can be written natively (e.g., `list[str] | None`) without importing anything from `typing`.
**Action:** Remove `typing` imports in performance-critical CLI entry points and replace them with modern built-in type syntax (`list`, `dict`, `|` union operator) to eliminate import overhead.
