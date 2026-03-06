# =============================================================================
# WEEK 10 - DAY 5: Final Project — Scalable URL Shortener Design
# Intern: ISHAAN GARG
# Topic: Apply system design, patterns, caching, queue concepts
# =============================================================================

import hashlib, time, json, os, threading, queue
from datetime import datetime
from collections import defaultdict
from flask import Flask, jsonify, request, redirect

print("=" * 60)
print("  ISHAAN GARG — SCALABLE URL SHORTENER")
print("=" * 60)

# ─── In-memory stores (replace with Redis + DB in production) ─────
url_store   = {}      # short_code → {url, created, clicks}
cache       = {}      # short_code → original_url (with TTL)
click_queue = queue.Queue()
analytics   = defaultdict(int)

# ─── Cache (simulated Redis with TTL) ─────────────────────────────
class SimpleCache:
    def __init__(self):
        self._data = {}
        self._expiry = {}

    def get(self, key):
        if key in self._expiry and time.time() > self._expiry[key]:
            self._data.pop(key, None); self._expiry.pop(key, None)
            return None
        return self._data.get(key)

    def set(self, key, value, ttl=300):
        self._data[key] = value
        if ttl: self._expiry[key] = time.time() + ttl

    def delete(self, key):
        self._data.pop(key, None); self._expiry.pop(key, None)

redis = SimpleCache()
cache_hits = 0; cache_misses = 0

# ─── Analytics Worker (async background processing) ───────────────
def analytics_worker():
    while True:
        try:
            event = click_queue.get(timeout=2)
            if event is None: break
            short_code = event["short_code"]
            analytics[f"clicks:{short_code}"] += 1
            analytics[f"total_clicks"] += 1
            click_queue.task_done()
        except queue.Empty:
            break

worker_thread = threading.Thread(target=analytics_worker, daemon=True)
worker_thread.start()

# ─── Core Functions ───────────────────────────────────────────────
def generate_short_code(url, length=7):
    """Generate deterministic short code using MD5 hash."""
    hash_val = hashlib.md5(url.encode()).hexdigest()
    return hash_val[:length]

def shorten_url(original_url, custom_code=None):
    """Store a URL and return short code."""
    if not original_url.startswith(("http://", "https://")):
        return None, "URL must start with http:// or https://"
    code = custom_code if custom_code else generate_short_code(original_url)
    if code in url_store and url_store[code]["url"] != original_url:
        return None, "Short code already taken"
    url_store[code] = {"url": original_url, "created": datetime.now().isoformat(), "clicks": 0}
    redis.set(code, original_url, ttl=600)
    return code, None

def resolve_url(short_code):
    """Look up original URL — cache-aside pattern."""
    global cache_hits, cache_misses
    cached = redis.get(short_code)
    if cached:
        cache_hits += 1
        click_queue.put({"short_code": short_code, "ts": time.time()})
        return cached, "cache"
    data = url_store.get(short_code)
    if data:
        cache_misses += 1
        redis.set(short_code, data["url"], ttl=600)
        click_queue.put({"short_code": short_code, "ts": time.time()})
        return data["url"], "db"
    return None, "not_found"

# ─── Flask App ────────────────────────────────────────────────────
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "urls_stored": len(url_store),
                    "version": "1.0.0"})

@app.route("/shorten", methods=["POST"])
def api_shorten():
    body = request.get_json()
    if not body or "url" not in body:
        return jsonify({"error": "Missing 'url' field"}), 400
    code, err = shorten_url(body["url"], body.get("custom_code"))
    if err:
        return jsonify({"error": err}), 400
    return jsonify({"short_code": code, "short_url": f"http://short.ly/{code}",
                    "original_url": body["url"]}), 201

@app.route("/<short_code>", methods=["GET"])
def api_redirect(short_code):
    url, source = resolve_url(short_code)
    if not url:
        return jsonify({"error": "URL not found"}), 404
    return jsonify({"redirect_to": url, "source": source}), 302

@app.route("/stats/<short_code>")
def api_stats(short_code):
    data = url_store.get(short_code)
    if not data:
        return jsonify({"error": "Not found"}), 404
    clicks = analytics.get(f"clicks:{short_code}", 0)
    return jsonify({"short_code": short_code, "url": data["url"],
                    "created": data["created"], "clicks": clicks})

@app.route("/analytics")
def api_analytics():
    click_queue.join()
    return jsonify({"total_clicks": analytics.get("total_clicks", 0),
                    "cache_hits": cache_hits, "cache_misses": cache_misses,
                    "urls_stored": len(url_store)})

# ─── Demo ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n--- Demo: URL Shortening + Caching + Analytics ---")
    with app.test_client() as client:
        test_urls = [
            "https://www.python.org/doc/",
            "https://docs.flask.palletsprojects.com/",
            "https://scikit-learn.org/stable/",
        ]
        codes = []
        for url in test_urls:
            r = client.post("/shorten", json={"url": url})
            d = r.get_json()
            codes.append(d["short_code"])
            print(f"  Shortened: {url[:40]:40s} → {d['short_code']}")

        r = client.post("/shorten", json={"url": "https://www.navkiran.dev", "custom_code": "navk"})
        codes.append("navk")
        print(f"  Custom:    https://www.navkiran.dev → {r.get_json()['short_code']}")

        print("\n--- Resolving URLs (cache-aside) ---")
        for code in codes * 2:
            r = client.get(f"/{code}")
            d = r.get_json()
            print(f"  /{code} → source={d['source']} | {d['redirect_to'][:50]}")

        time.sleep(0.2)
        r = client.get("/analytics")
        print("\n--- Analytics ---")
        print(json.dumps(r.get_json(), indent=2))

    click_queue.put(None)
    worker_thread.join()

    print("\n" + "=" * 60)
    print("SYSTEM DESIGN CHOICES MADE:")
    print("=" * 60)
    print("  Cache-aside    → Redis for fast URL lookups")
    print("  Async queue    → click events processed in background")
    print("  MD5 hash       → deterministic short code generation")
    print("  Health check   → /health endpoint for load balancer")
    print("  Input validation → reject non-HTTP URLs")
    print("  Custom codes   → support user-defined short codes")
    print("  In production: add rate limiting, persistence, CDN")
    print("\n✅ Week 10 Complete — System Design mastered, Navkiran!")
    print("=" * 60)
