## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2026-03-29 - Typing Module Import Overhead in CLIs
**Learning:** For extremely simple and fast Python CLIs, importing modules from `typing` (like `List` and `Optional`) can introduce a noticeable startup overhead (~40ms), which is significant when the execution time of the tool itself is very small.
**Action:** When optimizing fast-path CLIs in Python, eliminate `typing` module imports by using `from __future__ import annotations` and leveraging Python 3.10+ syntax (e.g., `list[str] | None`). This avoids the import overhead while preserving code readability, backwards compatibility, and type safety.
