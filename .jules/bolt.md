## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2025-01-20 - Python typing module import overhead
**Learning:** For extremely fast CLIs, the `typing` module import overhead can be unexpectedly high (approx. 40-290ms).
**Action:** When working on CLI entry points or scripts that need to load very fast, use `from __future__ import annotations` and Python 3.10+ type hinting syntax (e.g. `list[str] | None` instead of `Optional[List[str]]`) to eliminate the need to import `typing` module while still maintaining type checking.
