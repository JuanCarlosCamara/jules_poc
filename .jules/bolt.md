## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - CLI Startup Overhead from `typing` Module
**Learning:** For small Python CLI tools, importing the `typing` module (e.g., `from typing import List, Optional`) adds measurable startup overhead (around 30-40ms). When combining fast-paths (bypassing argparse) to speed up common invocations, the `typing` module import becomes a primary bottleneck in CLI initialization.
**Action:** Use `from __future__ import annotations` and Python 3.10+ style union types (e.g., `list[str] | None`) instead of the `typing` module to completely eliminate its import overhead while maintaining robust type hinting.
