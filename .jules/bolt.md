## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Avoiding `typing` Module Overhead for Fast CLIs
**Learning:** In simple Python CLIs, importing the `typing` module can introduce significant startup overhead (approx. 40ms). When performance is critical, this import time can be detrimental.
**Action:** Use `from __future__ import annotations` and Python 3.10+ native types (e.g., `list[str] | None`) instead of the `typing` module (e.g., `Optional[List[str]]`) to maintain static typing while entirely bypassing the module's initialization cost.
