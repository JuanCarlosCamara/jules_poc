## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python CLI Type Hinting Overhead
**Learning:** Importing the `typing` module for type hints can introduce significant startup overhead (e.g., 40-290ms) in Python CLI applications. When speed is critical, relying on `typing` imports can negate other fast-path optimizations.
**Action:** Use `from __future__ import annotations` and modern Python 3.10+ type hint syntax (like `list[str] | None`) to provide type hints without incurring the startup penalty of importing the `typing` module.
