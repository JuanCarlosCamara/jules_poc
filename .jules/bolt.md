## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python CLI `typing` module Fast-Path Optimization
**Learning:** For ultra-fast Python CLIs, even standard imports like `from typing import List, Optional` can contribute significant initialization overhead (~20-40ms). The `typing` module does significant work on import, which can slow down simple "fast-paths".
**Action:** Use Python 3.10+ style annotations (e.g., `list[str] | None`) combined with `from __future__ import annotations` (for backwards compatibility/deferred evaluation) to completely avoid importing the `typing` module for performance-critical fast-paths, preserving readability while improving startup speed.
