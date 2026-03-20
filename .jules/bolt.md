## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Avoiding `typing` Overhead in CLI Fast-Paths
**Learning:** For extremely fast, simple CLIs, even standard library imports like `typing` can add noticeable overhead (1-2ms) to startup time. This is especially true when `argparse` has already been deferred and `sys.argv` is being inspected directly.
**Action:** Use `from __future__ import annotations` and Python 3.10+ syntax (e.g., `list[str] | None` instead of `Optional[List[str]]`) to remove the need for `typing` imports at runtime in modules executed as CLI entry points, thereby reducing import overhead while retaining type checker compatibility.
