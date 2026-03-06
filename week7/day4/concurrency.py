# =============================================================================
# WEEK 7 - DAY 4: Concurrency — Threading & Multiprocessing
# Intern: ISHAAN GARG
# Topic: Run tasks in parallel to speed up Python programs
# =============================================================================

import threading
import multiprocessing
import concurrent.futures
import time
import requests

print("=" * 55)
print("SECTION 1: WHY CONCURRENCY?")
print("=" * 55)
print("""
Python by default runs one thing at a time (sequential).
For slow tasks (network calls, file I/O, heavy computation)
you can run things in parallel.

Two main tools:
  threading       → parallel I/O (network, files)
  multiprocessing → parallel CPU work (number crunching)

GIL (Global Interpreter Lock):
  Python only runs one thread at a time for CPU work.
  → Threading is good for I/O (waiting), not CPU.
  → Multiprocessing spawns separate processes → no GIL.
""")

print("=" * 55)
print("SECTION 2: SEQUENTIAL vs THREADED SIMULATION")
print("=" * 55)

def fake_api_call(url_id, results, index):
    """Simulate a slow API call (0.5 second delay)."""
    time.sleep(0.5)
    results[index] = f"Response from URL {url_id}"

# Sequential
start = time.time()
results_seq = [None] * 5
for i in range(5):
    fake_api_call(i, results_seq, i)
sequential_time = time.time() - start
print(f"Sequential (5 calls): {sequential_time:.2f}s")

# Threaded
start = time.time()
results_thr = [None] * 5
threads = []
for i in range(5):
    t = threading.Thread(target=fake_api_call, args=(i, results_thr, i))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
threaded_time = time.time() - start
print(f"Threaded  (5 calls): {threaded_time:.2f}s")
print(f"Speedup: {sequential_time/threaded_time:.1f}x faster")

print("\n" + "=" * 55)
print("SECTION 3: THREADPOOLEXECUTOR — CLEANER APPROACH")
print("=" * 55)

def fetch_mock(task_id):
    time.sleep(0.3)
    return f"Task {task_id} completed"

start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(fetch_mock, i) for i in range(10)]
    results = [f.result() for f in concurrent.futures.as_completed(futures)]
elapsed = time.time() - start

print(f"10 tasks with ThreadPoolExecutor: {elapsed:.2f}s")
print("Results sample:", results[:3])

print("\n" + "=" * 55)
print("SECTION 4: MULTIPROCESSING FOR CPU TASKS")
print("=" * 55)

def compute_squares(numbers):
    return [x**2 for x in numbers]

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

numbers = list(range(1, 100001))

# Sequential prime count
start = time.time()
prime_count_seq = sum(1 for n in numbers if is_prime(n))
seq_time = time.time() - start
print(f"Sequential prime count: {prime_count_seq} | Time: {seq_time:.2f}s")

# ProcessPoolExecutor
def count_primes_in_range(args):
    start_n, end_n = args
    return sum(1 for n in range(start_n, end_n) if is_prime(n))

cpu_count = multiprocessing.cpu_count()
print(f"\nCPU cores available: {cpu_count}")

chunk_size = len(numbers) // cpu_count
chunks = [(i * chunk_size + 1, (i+1) * chunk_size + 1) for i in range(cpu_count)]

start = time.time()
with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count) as executor:
    counts = list(executor.map(count_primes_in_range, chunks))
prime_count_par = sum(counts)
par_time = time.time() - start

print(f"Parallel  prime count: {prime_count_par} | Time: {par_time:.2f}s")
if par_time > 0:
    print(f"Speedup: {seq_time/par_time:.1f}x faster")

print("\n" + "=" * 55)
print("SECTION 5: THREAD SAFETY — LOCKS")
print("=" * 55)

counter = 0
lock = threading.Lock()

def increment_safe(n):
    global counter
    for _ in range(n):
        with lock:           # only one thread at a time can modify counter
            counter += 1

counter = 0
threads = [threading.Thread(target=increment_safe, args=(1000,)) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Thread-safe counter (expected 5000): {counter}")

print("\n" + "=" * 55)
print("SUMMARY")
print("=" * 55)
print("threading           → parallel I/O tasks")
print("multiprocessing     → parallel CPU tasks")
print("ThreadPoolExecutor  → managed thread pool")
print("ProcessPoolExecutor → managed process pool")
print("Lock                → prevent race conditions")
print("join()              → wait for thread/process to finish")
