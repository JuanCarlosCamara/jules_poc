## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2026-03-26 - Typing Module Startup Overhead
**Learning:** For extremely simple Python CLI tools where execution time is dominated by startup overhead, the standard library `typing` module can contribute significantly (around ~20-40ms) when imported at the module level.
**Action:** Use `from __future__ import annotations` combined with Python 3.10+ syntax (e.g., `list[str] | None` instead of `Optional[List[str]]`) to eliminate the `typing` module import overhead while maintaining code readability and backwards compatibility.
