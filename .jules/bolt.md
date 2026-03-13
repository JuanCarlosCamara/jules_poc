## 2024-05-24 - Python CLI Fast-Path Optimization
**Learning:** For ultra-fast, simple Python CLIs, `import argparse` and `argparse.ArgumentParser` instantiation can contribute significantly (20-40ms) to startup overhead. When a CLI's core functionality is extremely straightforward (like printing a single string argument), the overhead of standard library imports like `argparse` can overshadow the execution time.
**Action:** When optimizing basic Python CLI tools, consider implementing a "fast-path" that directly inspects `sys.argv` for the most common, simple use cases (e.g., zero or one positional argument). Fall back to lazy-loading `argparse` only when more complex flag parsing (like `-h` or `--help`) or multiple arguments are encountered.

## 2024-05-25 - Python CLI Type Imports & Multi-word Arguments Overhead
**Learning:** For extremely fast CLIs, even `import typing` introduces measurable overhead (~20ms). Additionally, standard CLI setups using `argparse` fail or invoke slow paths for simple, multi-word positional arguments (e.g. `hello-jules Hello World`) if not explicitly designed for it.
**Action:** Use Python 3.10+ native types (e.g., `list`, `| None`) instead of `typing` module imports. Ensure fast-paths for CLI execution handle multi-word positional arguments directly by joining them with spaces, bypassing `argparse` completely for common simple inputs.
