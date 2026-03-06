# =============================================================================
# WEEK 10 - DAY 2: Design Patterns in Python
# Intern: ISHAAN GARG
# Topic: Singleton, Factory, Observer, Strategy, Decorator patterns
# =============================================================================

print("=" * 60)
print("  WEEK 10 DAY 2: DESIGN PATTERNS")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
Design patterns are reusable solutions to common software problems.
They are NOT code — they are blueprints.
""")

print("=" * 60)
print("PATTERN 1: SINGLETON")
print("=" * 60)
print("Ensures only ONE instance of a class ever exists.")

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
            cls._instance.host = "localhost"
        return cls._instance

    def connect(self, host):
        self.host = host
        self.connected = True
        print(f"Connected to {self.host}")

    def execute(self, query):
        if not self.connected:
            raise RuntimeError("Not connected!")
        print(f"Executing: {query}")

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance? {db1 is db2}")  # True
db1.connect("prod-db.example.com")
db2.execute("SELECT * FROM users")
print(f"db2.host = {db2.host}")  # Same as db1

print("\n" + "=" * 60)
print("PATTERN 2: FACTORY")
print("=" * 60)
print("Creates objects without specifying exact class — use a factory method.")

class Notification:
    def send(self, message): raise NotImplementedError

class EmailNotification(Notification):
    def send(self, message): print(f"📧 Email: {message}")

class SMSNotification(Notification):
    def send(self, message): print(f"📱 SMS: {message}")

class PushNotification(Notification):
    def send(self, message): print(f"🔔 Push: {message}")

class NotificationFactory:
    _types = {"email": EmailNotification, "sms": SMSNotification, "push": PushNotification}

    @classmethod
    def create(cls, notification_type):
        cls_type = cls._types.get(notification_type.lower())
        if not cls_type:
            raise ValueError(f"Unknown type: {notification_type}")
        return cls_type()

for ntype in ["email", "sms", "push"]:
    n = NotificationFactory.create(ntype)
    n.send(f"Hello Navkiran! [{ntype}]")

print("\n" + "=" * 60)
print("PATTERN 3: OBSERVER")
print("=" * 60)
print("Objects subscribe to events. When event fires, all subscribers notified.")

class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        self._subscribers.setdefault(event, []).append(callback)

    def publish(self, event, data=None):
        print(f"\nEvent '{event}' fired with data: {data}")
        for cb in self._subscribers.get(event, []):
            cb(data)

bus = EventBus()
bus.subscribe("user.signup", lambda d: print(f"  📧 Send welcome email to {d['email']}"))
bus.subscribe("user.signup", lambda d: print(f"  📊 Log signup event for {d['name']}"))
bus.subscribe("user.signup", lambda d: print(f"  🎁 Create free trial for {d['name']}"))
bus.subscribe("order.placed", lambda d: print(f"  📦 Process order #{d['order_id']}"))

bus.publish("user.signup",  {"name": "Navkiran", "email": "nav@mail.com"})
bus.publish("order.placed", {"order_id": 12345, "amount": 999})

print("\n" + "=" * 60)
print("PATTERN 4: STRATEGY")
print("=" * 60)
print("Define a family of algorithms, make them interchangeable.")

class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy(data)

import random
data = [random.randint(1, 100) for _ in range(8)]
print("Original:", data)

sorter = Sorter(sorted)
print("Ascending:", sorter.sort(data))

sorter._strategy = lambda x: sorted(x, reverse=True)
print("Descending:", sorter.sort(data))

sorter._strategy = lambda x: sorted(x, key=lambda n: abs(n - 50))
print("Closest to 50:", sorter.sort(data))

print("\n" + "=" * 60)
print("PATTERN 5: DECORATOR PATTERN")
print("=" * 60)
print("Add behavior to functions/classes without modifying them.")

import time, functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  ⏱ {func.__name__} took {elapsed*1000:.2f}ms")
        return result
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  📝 Calling {func.__name__} with args={args}")
        result = func(*args, **kwargs)
        print(f"  📝 {func.__name__} returned {result}")
        return result
    return wrapper

def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  ⚠️ Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

@timer
@logger
def compute_sum(n):
    return sum(range(n))

result = compute_sum(10000)

call_count = 0
@retry(max_attempts=3)
def flaky_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Network hiccup!")
    return "Success!"

print(f"\n  Result: {flaky_function()}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("Singleton  → one instance only (DB connections, config)")
print("Factory    → create objects by type name")
print("Observer   → event-driven publish/subscribe")
print("Strategy   → swap algorithms at runtime")
print("Decorator  → add behavior without changing original code")
