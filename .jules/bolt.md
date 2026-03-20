## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Avoiding `typing` Module Overhead for Fast CLI Execution
**Learning:** In simple Python CLI tools designed for instant execution, importing modules like `typing` (`from typing import List, Optional`) introduces unnecessary startup latency (up to 30ms or more).
**Action:** When working on CLI entry point files where extreme fast execution is a priority, use `from __future__ import annotations` and leverage Python 3.10+ built-in type syntax (e.g., `list[str] | None`) to avoid the performance penalty of importing the `typing` module, without sacrificing type safety and code readability.
