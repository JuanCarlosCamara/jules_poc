## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python Startup Optimization with __future__ annotations
**Learning:** The `typing` module in Python can add significant startup overhead (approx. 30ms). For simple CLI tools, this overhead might be noticeable.
**Action:** Use `from __future__ import annotations` to avoid the runtime import cost of the `typing` module while still allowing the use of modern type hint syntax (e.g., `list[str] | None`) for better readability and backward compatibility. Since `sys` is extremely lightweight and fast to import, move `import sys` to the module level instead of lazy-loading it.
