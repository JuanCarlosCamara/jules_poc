## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2026-03-19 - Python CLI Typing Module Startup Overhead
**Learning:** In very simple Python CLI applications that leverage fast-paths, module-level standard library imports such as `typing` can add noticeable startup overhead (e.g., ~15-30ms) before the application even begins execution.
**Action:** To avoid the startup overhead of the `typing` module while preserving code readability and backwards compatibility, use `from __future__ import annotations` with Python 3.10+ syntax (e.g., `list[str] | None`) for type hinting instead of importing from the `typing` module.
