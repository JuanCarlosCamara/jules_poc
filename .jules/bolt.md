## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python 3.10+ Type Hints for Performance
**Learning:** Using `from typing import List, Optional` adds startup overhead by loading the `typing` module, which can be detrimental in CLI tools where speed is a priority. Python 3.10 introduced `list[str] | None` syntax, which allows type hinting without needing to import `typing` at all.
**Action:** Always prefer native Python 3.10+ type hint syntax (`list`, `dict`, `|`) instead of importing from the `typing` module to avoid the startup penalty in short-lived CLI applications.
