## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2025-02-28 - Avoid typing module startup overhead in simple CLIs
**Learning:** Importing the `typing` module in Python (e.g., `from typing import List, Optional`) incurs a measurable startup overhead (approx. 20ms). In lightweight CLI applications where execution speed is critical, this import delay can represent a significant portion of the total runtime.
**Action:** Replace `typing` imports with `from __future__ import annotations` and use native Python 3.10+ type hinting syntax (e.g., `list[str] | None`) to maintain strict typing without the startup performance penalty.
