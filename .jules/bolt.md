## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python CLI Type Hint Optimization
**Learning:** Even simple type hint imports like `from typing import List, Optional` can add measurable startup overhead (around 20-30ms) to a simple Python CLI, which can be significant when standard library imports are already optimized for fast-paths.
**Action:** When working on extreme fast-path optimizations for simple CLI tools, use `from __future__ import annotations` and rely on Python 3.10+ syntax (e.g., `list[str] | None`) to provide type hints without incurring the startup cost of loading the `typing` module.
