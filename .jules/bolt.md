## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2026-03-17 - Typing Module Overhead in CLI Fast-Paths
**Learning:** The `typing` module itself carries a significant startup overhead (around 15-20ms) which is noticeable in extremely fast-loading CLI applications that aim to run in under 30ms.
**Action:** Use `from __future__ import annotations` and Python 3.10+ modern union types (`list[str] | None`) rather than importing standard classes (`List`, `Optional`) from the `typing` module to avoid this initialization cost entirely while still retaining fully descriptive type hints.
