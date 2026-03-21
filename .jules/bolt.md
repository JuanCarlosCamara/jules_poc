## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python CLI Type Hinting Overhead
**Learning:** For ultra-fast, simple Python CLIs, importing modules like `typing` at the module level can contribute significantly to startup overhead. In this codebase, the initialization of `typing` adds measurable time before the core execution begins.
**Action:** Use `from __future__ import annotations` in conjunction with standard Python 3.10+ types (like `list[str] | None`) to provide necessary type hints without the cost of loading the `typing` module, ensuring strict PEP 8 compliance and backwards compatibility with low execution overhead.
