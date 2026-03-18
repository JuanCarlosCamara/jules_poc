## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - typing Module Import Overhead in CLIs
**Learning:** In ultra-fast Python CLI applications, standard module-level imports such as `from typing import List, Optional` incur noticeable startup overhead.
**Action:** Use `from __future__ import annotations` and Python 3.10+ modern typing syntax (e.g. `list[str] | None`) to preserve the readability of type hints while completely avoiding the overhead of importing from the `typing` module.
