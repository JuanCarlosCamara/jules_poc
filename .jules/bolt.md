## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python CLI Typing Module Startup Overhead
**Learning:** For Python CLI applications where startup time is critical, importing the `typing` module (e.g., `from typing import List, Optional`) adds significant overhead (around 20-25ms) compared to the actual execution time.
**Action:** Use Python 3.10+ built-in type hinting syntax (e.g., `list[str] | None`) directly instead of importing generic types from the `typing` module to avoid this unnecessary startup penalty in performance-sensitive entry points.
