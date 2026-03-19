## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python CLI Type Hinting Overhead
**Learning:** For fast Python CLIs, importing the `typing` module (e.g., `from typing import List, Optional`) can add significant startup overhead (e.g., ~20-40ms on slow systems, or general overhead) compared to executing the script itself.
**Action:** Use `from __future__ import annotations` and Python 3.10+ modern syntax (e.g., `list[str] | None`) to preserve type hints and readability while eliminating the startup cost of importing the `typing` module.
