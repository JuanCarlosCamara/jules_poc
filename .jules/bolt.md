## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python Type Hint Import Overhead
**Learning:** Importing the `typing` module (e.g., `from typing import List, Optional`) adds significant startup overhead (roughly 0.25 seconds for 100 imports, or ~2.5ms per invocation) which can be a meaningful delay for simple CLI tools.
**Action:** Use Python 3.10+ built-in type hint syntax (e.g., `list[str] | None`) instead of importing from the `typing` module whenever possible to avoid unnecessary startup latency.
