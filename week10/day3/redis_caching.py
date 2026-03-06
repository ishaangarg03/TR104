# =============================================================================
# WEEK 10 - DAY 3: Redis — Caching, Sessions, Queues
# Intern: ISHAAN GARG
# Topic: Redis data structures and patterns (simulated without real Redis)
# =============================================================================

import time
import json
from datetime import datetime
from collections import OrderedDict

print("=" * 60)
print("  WEEK 10 DAY 3: REDIS & CACHING")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
WHAT IS REDIS?
  Redis = Remote Dictionary Server
  In-memory key-value store — MUCH faster than disk DBs.
  Used for: caching, sessions, rate limiting, queues, leaderboards.

  Speed comparison:
    Disk DB (PostgreSQL): ~5ms per query
    Redis (memory):       ~0.1ms per query  (50x faster!)

REDIS DATA TYPES:
  String  → simple value, counters
  List    → ordered queue/stack
  Hash    → dict-like object
  Set     → unique values
  Sorted Set → leaderboard, ranking
  TTL     → automatic key expiration
""")

print("=" * 60)
print("SECTION 1: CACHE-ASIDE PATTERN (simulated)")
print("=" * 60)

class MockRedis:
    """Simulates Redis in memory for learning purposes."""
    def __init__(self):
        self._store = {}
        self._expiry = {}
        self.hits = 0
        self.misses = 0

    def get(self, key):
        if key in self._expiry and time.time() > self._expiry[key]:
            del self._store[key]; del self._expiry[key]
            return None
        val = self._store.get(key)
        if val: self.hits += 1
        else:   self.misses += 1
        return val

    def set(self, key, value, ttl=None):
        self._store[key] = value
        if ttl: self._expiry[key] = time.time() + ttl

    def delete(self, key):
        self._store.pop(key, None)
        self._expiry.pop(key, None)

    def incr(self, key):
        val = int(self._store.get(key, 0)) + 1
        self._store[key] = val
        return val

    def exists(self, key): return key in self._store
    def keys(self): return list(self._store.keys())

redis = MockRedis()

def slow_db_query(user_id):
    """Simulates a slow database query (0.1s delay)."""
    time.sleep(0.1)
    return {"id": user_id, "name": f"User_{user_id}", "score": user_id * 11 % 100}

def get_user_cached(user_id, ttl=60):
    """Cache-aside: check cache first, hit DB on miss."""
    cache_key = f"user:{user_id}"
    cached = redis.get(cache_key)
    if cached:
        return json.loads(cached), "cache"
    user = slow_db_query(user_id)
    redis.set(cache_key, json.dumps(user), ttl=ttl)
    return user, "db"

print("Fetching users (1st time = DB, 2nd time = cache):")
for user_id in [1, 2, 3, 1, 2, 3]:  # 1,2,3 repeat
    start = time.time()
    user, source = get_user_cached(user_id)
    ms = (time.time() - start) * 1000
    print(f"  User {user_id} from {source:5s} | {ms:.1f}ms | {user['name']}")

print(f"\nCache stats: {redis.hits} hits, {redis.misses} misses")
print(f"Cache hit rate: {redis.hits/(redis.hits+redis.misses)*100:.0f}%")

print("\n" + "=" * 60)
print("SECTION 2: RATE LIMITING WITH REDIS")
print("=" * 60)

redis2 = MockRedis()

def check_rate_limit(user_id, max_requests=5, window_seconds=60):
    """Allow max N requests per user per time window."""
    key = f"rate:{user_id}:{int(time.time() // window_seconds)}"
    count = redis2.incr(key)
    allowed = count <= max_requests
    return allowed, count, max_requests

print("Rate limiting (max 5 requests per window):")
for i in range(8):
    allowed, count, limit = check_rate_limit("navkiran", max_requests=5)
    status = "✓ ALLOWED" if allowed else "✗ BLOCKED"
    print(f"  Request {i+1}: {status} ({count}/{limit})")

print("\n" + "=" * 60)
print("SECTION 3: SORTED SET — LEADERBOARD")
print("=" * 60)

class Leaderboard:
    def __init__(self):
        self._scores = {}

    def add_score(self, player, score):
        self._scores[player] = max(self._scores.get(player, 0), score)

    def top_n(self, n):
        sorted_scores = sorted(self._scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:n]

    def rank_of(self, player):
        sorted_players = sorted(self._scores.items(), key=lambda x: x[1], reverse=True)
        for rank, (p, s) in enumerate(sorted_players, 1):
            if p == player:
                return rank, s
        return None, None

lb = Leaderboard()
players = [("Navkiran", 850), ("Alice", 920), ("Bob", 780), ("Charlie", 950),
           ("Diana", 870), ("Eve", 810), ("Frank", 900), ("Navkiran", 890)]
for player, score in players:
    lb.add_score(player, score)

print("Top 5 Leaderboard:")
for rank, (player, score) in enumerate(lb.top_n(5), 1):
    print(f"  #{rank}  {player:12s}: {score}")

rank, score = lb.rank_of("Navkiran")
print(f"\nNavkiran's rank: #{rank} with score {score}")

print("\n" + "=" * 60)
print("SECTION 4: REDIS COMMANDS REFERENCE")
print("=" * 60)

print("""
String:
  SET key value [EX seconds]   → set with optional expiry
  GET key                      → get value
  INCR key                     → increment counter
  EXPIRE key seconds           → set TTL

List (queue/stack):
  RPUSH key value              → add to right (end)
  LPUSH key value              → add to left (front)
  RPOP key                     → remove from right
  LPOP key                     → remove from left
  LRANGE key 0 -1              → get all elements

Hash (dict):
  HSET key field value         → set field
  HGET key field               → get field
  HGETALL key                  → get all fields
  HDEL key field               → delete field

Sorted Set (leaderboard):
  ZADD key score member        → add with score
  ZRANK key member             → rank (0-indexed)
  ZRANGE key 0 -1 WITHSCORES  → all sorted ascending
  ZREVRANGE key 0 9 WITHSCORES → top 10 descending

Key management:
  DEL key                      → delete key
  EXISTS key                   → check if exists
  TTL key                      → time to live
  KEYS pattern                 → find matching keys
  FLUSHDB                      → clear all (careful!)
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("Redis = ultra-fast in-memory key-value store")
print("Cache-aside = check cache → miss → DB → store in cache")
print("TTL = auto-expire cached data")
print("Rate limiting = INCR key, check against limit")
print("Sorted sets = perfect for leaderboards and rankings")
