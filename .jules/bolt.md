## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-24 - Typing Module Import Overhead in CLIs
**Learning:** The `typing` module can introduce a noticeable startup overhead (e.g. 40-290ms) which makes up a significant portion of execution time for extremely simple CLIs.
**Action:** When working with Python 3.10+ syntax in contexts where startup speed is critical, replace `typing` imports (like `List`, `Optional`) with `from __future__ import annotations` and use native pipe/list syntax (`list[str] | None`) to avoid the module load time overhead.
