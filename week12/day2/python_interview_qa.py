# =============================================================================
# WEEK 12 - DAY 2: Python-Specific Interview Questions
# Intern: ISHAAN GARG
# Topic: Advanced Python concepts that come up in interviews
# =============================================================================

print("=" * 60)
print("  WEEK 12 DAY 2: PYTHON INTERVIEW QUESTIONS")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("=" * 60)
print("TOPIC 1: GENERATORS & ITERATORS")
print("=" * 60)

# Iterator protocol
class Counter:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

print("Custom iterator:")
for n in Counter(1, 6):
    print(n, end=" ")
print()

# Generator function (lazy evaluation — saves memory)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(gen, n):
    return [next(gen) for _ in range(n)]

fib = fibonacci()
print(f"\nFirst 10 Fibonacci: {take(fib, 10)}")

# Generator expression (like list comprehension but lazy)
squares_gen = (x**2 for x in range(1000000))  # uses almost no memory!
print(f"Sum of first 10 squares (generator): {sum(x**2 for x in range(11))}")

print("\n" + "=" * 60)
print("TOPIC 2: DECORATORS IN DEPTH")
print("=" * 60)

import functools, time

def memoize(func):
    """Cache function results to avoid redundant computation."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib_memoized(n):
    if n <= 1: return n
    return fib_memoized(n-1) + fib_memoized(n-2)

start = time.time()
print(f"fib(35) = {fib_memoized(35)} in {(time.time()-start)*1000:.2f}ms")

# Class-based decorator
class Retry:
    def __init__(self, max_attempts=3, exceptions=(Exception,)):
        self.max_attempts = max_attempts
        self.exceptions = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, self.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except self.exceptions as e:
                    if attempt == self.max_attempts:
                        raise
                    print(f"  Attempt {attempt} failed: {e}. Retrying...")
        return wrapper

attempt_count = 0

@Retry(max_attempts=3, exceptions=(ValueError,))
def flaky():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ValueError("Not ready yet")
    return "Success!"

attempt_count = 0
print(f"\nRetry decorator: {flaky()}")

print("\n" + "=" * 60)
print("TOPIC 3: CONTEXT MANAGERS")
print("=" * 60)

import contextlib

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        print(f"  Elapsed: {self.elapsed*1000:.2f}ms")
        return False  # don't suppress exceptions

with Timer():
    total = sum(range(1_000_000))
    print(f"  Sum = {total}")

# contextlib.contextmanager decorator
@contextlib.contextmanager
def managed_resource(name):
    print(f"  Acquiring {name}")
    try:
        yield name
    finally:
        print(f"  Releasing {name}")

with managed_resource("database_connection") as resource:
    print(f"  Using: {resource}")

print("\n" + "=" * 60)
print("TOPIC 4: METACLASSES & DESCRIPTORS (Advanced)")
print("=" * 60)

print("""
Metaclass: the class of a class. Controls how classes are created.

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.debug = False

c1 = Config()
c2 = Config()
print(c1 is c2)  # True — same instance!

Descriptor: controls attribute access with __get__, __set__, __delete__.
Used in Django models, SQLAlchemy columns, property decorators.
""")

# Property descriptor (most common)
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(f"Temperature: {t.celsius}°C = {t.fahrenheit}°F")
t.celsius = 100
print(f"Temperature: {t.celsius}°C = {t.fahrenheit}°F")

print("\n" + "=" * 60)
print("TOPIC 5: COMMON PYTHON GOTCHAS")
print("=" * 60)

# Mutable default argument (classic bug!)
def add_to_list_BAD(item, lst=[]):   # BUG: lst shared across calls!
    lst.append(item)
    return lst

def add_to_list_GOOD(item, lst=None):  # FIX: use None as sentinel
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("Mutable default bug:")
r1 = add_to_list_BAD(1)
r2 = add_to_list_BAD(2)
print(f"  BAD  call1={r1}, call2={r2}")  # both share same list!

r1 = add_to_list_GOOD(1)
r2 = add_to_list_GOOD(2)
print(f"  GOOD call1={r1}, call2={r2}")  # independent lists

# Late binding closures
print("\nLate binding gotcha:")
funcs_bad  = [lambda: i for i in range(5)]
funcs_good = [lambda i=i: i for i in range(5)]  # capture i at creation
print(f"  BAD  (all same): {[f() for f in funcs_bad]}")
print(f"  GOOD (distinct): {[f() for f in funcs_good]}")

# is vs ==
print("\nis vs ==:")
a, b = [1,2,3], [1,2,3]
print(f"  a == b: {a == b}  (same values)")
print(f"  a is b: {a is b}  (different objects)")
print(f"  Use == for value comparison, 'is' only for None/True/False")

print("\n" + "=" * 60)
print("TOPIC 6: QUICK REFERENCE — PYTHON INTERVIEW ANSWERS")
print("=" * 60)

qa = [
    ("What is GIL?", "Global Interpreter Lock — prevents true multi-threading for CPU work. Use multiprocessing for CPU tasks."),
    ("List vs Tuple?", "List is mutable. Tuple is immutable. Tuples are faster and hashable (can be dict keys)."),
    ("*args vs **kwargs?", "*args = variable positional args as tuple. **kwargs = variable keyword args as dict."),
    ("@staticmethod vs @classmethod?", "static: no self/cls param. classmethod: receives cls, can create instances."),
    ("What is __slots__?", "Restricts attributes, saves memory by replacing __dict__ with fixed array."),
    ("shallow vs deep copy?", "Shallow: new container, same objects inside. Deep: new container AND new nested objects."),
    ("What are comprehensions?", "[x for x in lst], {k:v for k,v in d.items()}, {x for x in lst}, (x for x in lst)"),
    ("What is a generator?", "Function with yield. Lazy — produces values one at a time. Memory efficient."),
    ("What is duck typing?", "If it walks like a duck and quacks like a duck — Python cares about behavior, not type."),
    ("What is LEGB?", "Local → Enclosing → Global → Built-in — Python's variable lookup order."),
]

for q, a in qa:
    print(f"\n  Q: {q}")
    print(f"  A: {a}")
