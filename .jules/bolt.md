## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2025-02-28 - Typing Module Import Overhead
**Learning:** In simple CLI applications, importing objects like `List` and `Optional` from the `typing` module can incur a measurable startup overhead (around ~16-20ms). For a micro-CLI tool, this overhead represents a significant percentage of the total execution time.
**Action:** Use `from __future__ import annotations` and the native Python 3.10+ types (like `list[str] | None`) to provide clear type hints without incurring the runtime penalty of loading the `typing` module.
