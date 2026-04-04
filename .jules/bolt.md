## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2025-01-22 - Python CLI typing module import overhead
**Learning:** Importing standard library modules like `typing` introduces significant startup overhead (40-290ms) in tiny Python CLI tools. Since speed is critical for CLIs, such imports should be avoided when possible.
**Action:** Use `from __future__ import annotations` and Python 3.10+ built-in type syntaxes (like `list[str] | None` instead of `Optional[List[str]]`) to maintain strict typing without the import cost.
