import sys
import time
import subprocess

start = time.perf_counter()
subprocess.run([sys.executable, "-c", "import hello_jules.main; hello_jules.main.main(['Hi', 'Jules'])"], stderr=subprocess.DEVNULL)
print(f"Argparse with >1 args overhead: {(time.perf_counter() - start) * 1000:.2f} ms")

start = time.perf_counter()
subprocess.run([sys.executable, "-c", "import hello_jules.main; hello_jules.main.main([' '.join(['Hi', 'Jules'])])"])
print(f"Fast path with joined args overhead: {(time.perf_counter() - start) * 1000:.2f} ms")
