## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2026-03-12 - Typing Import Overhead Avoidance
**Learning:** For extremely fast CLI tools, importing from the `typing` module (e.g., `from typing import List, Optional`) can introduce ~20-30ms of startup overhead, which might double the execution time of simple path commands.
**Action:** Use Python 3.10+ native type hinting syntax (e.g., `list[str] | None`) for fast-path CLI tools to eliminate `typing` import delays completely.
