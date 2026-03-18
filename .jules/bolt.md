## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2025-02-12 - Python Typing Module Overhead
**Learning:** The `typing` module imports can add measurable overhead to CLI startup time (~5-10ms). While type hints are essential for code quality, the runtime cost of importing generic types like `List` or `Optional` can be mitigated.
**Action:** Use `from __future__ import annotations` and Python 3.10+ native typing syntax (e.g., `list[str] | None`) to preserve type hints while avoiding the runtime overhead of importing standard library `typing` generic classes.
