## 2024-05-15 - Initial Bolt Journal
**Learning:** Initializing journal.
**Action:** Keep tracking learnings.

## 2024-05-15 - Lazy Loading `argparse` for Faster CLI Startup
**Learning:** `import argparse` takes roughly ~13ms, which is a significant chunk of time for a very fast CLI tool. This application is a simple CLI where simple invocations do not need advanced argument parsing. A fast-path that bypasses `argparse` for `hello-jules` and `hello-jules <msg>` drops overhead.
**Action:** When a Python CLI tool has very simple default arguments, defer `import argparse` until after checking `sys.argv` manually to dramatically speed up typical execution times.
