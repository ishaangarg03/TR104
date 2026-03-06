# =============================================================================
# WEEK 10 - DAY 1: System Design Fundamentals
# Intern: ISHAAN GARG
# Topic: How to design scalable systems — the concepts every dev needs
# =============================================================================

print("=" * 60)
print("  WEEK 10 — SYSTEM DESIGN & SOFTWARE ARCHITECTURE")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
WHAT IS SYSTEM DESIGN?
  Planning how software components work together at scale.
  Key question: "How do you build X for 1 million users?"

THE CORE CHALLENGES:
  Scalability  → handle more users/data without rewriting
  Reliability  → stay up even when parts fail
  Performance  → respond fast
  Maintainability → easy to change and debug
  Security     → protect data and prevent attacks
""")

print("=" * 60)
print("CONCEPT 1: HORIZONTAL vs VERTICAL SCALING")
print("=" * 60)

print("""
VERTICAL SCALING (Scale Up):
  Add more CPU/RAM to existing server.
  ✓ Simple — no code changes needed
  ✗ Limited — can't grow beyond biggest machine
  ✗ Single point of failure

HORIZONTAL SCALING (Scale Out):
  Add more servers and distribute traffic.
  ✓ Virtually unlimited growth
  ✓ No single point of failure
  ✗ More complex — need load balancer, state management

For most production systems: use horizontal scaling.
""")

print("=" * 60)
print("CONCEPT 2: LOAD BALANCERS")
print("=" * 60)

print("""
A load balancer distributes requests across multiple servers.

Algorithms:
  Round Robin    → server 1, server 2, server 3, server 1, ...
  Least Connections → send to server with fewest active requests
  IP Hash        → same client always goes to same server (sticky sessions)
  Weighted       → better servers get more traffic

Popular: Nginx, AWS ALB, HAProxy
""")

print("=" * 60)
print("CONCEPT 3: CACHING")
print("=" * 60)

print("""
Cache = fast temporary storage for frequently accessed data.
Avoids re-computing or re-fetching the same data.

Where to cache:
  Browser cache   → static files (CSS, JS, images)
  CDN             → globally cached static content (Cloudflare)
  Application     → in-memory dict/Redis for DB query results
  Database        → query cache

Cache strategies:
  Cache-aside     → app checks cache first, hits DB on miss, stores in cache
  Write-through   → write to cache AND DB simultaneously
  Write-back      → write to cache only, sync DB later (fast but risky)

Cache eviction:
  LRU (Least Recently Used) → remove least recently accessed
  LFU (Least Frequently Used) → remove least often accessed
  TTL (Time To Live) → expire after N seconds
""")

print("=" * 60)
print("CONCEPT 4: DATABASES AT SCALE")
print("=" * 60)

print("""
READ REPLICAS:
  Primary DB handles writes.
  Replicas (copies) handle reads.
  Great when reads >> writes (typical for most apps).

SHARDING (Horizontal Partitioning):
  Split data across multiple DB instances.
  Example: users A-M on shard 1, N-Z on shard 2.
  Complex but essential for very large datasets.

DATABASE TYPES:
  Relational (SQL):
    PostgreSQL, MySQL — structured data, ACID transactions
    Best for: financial data, user accounts, orders

  Document (NoSQL):
    MongoDB — flexible JSON-like documents
    Best for: content management, catalogs, logs

  Key-Value:
    Redis, DynamoDB — ultra-fast lookups by key
    Best for: caching, sessions, leaderboards

  Time-Series:
    InfluxDB, TimescaleDB — optimized for time-stamped data
    Best for: metrics, IoT, analytics

  Vector DB:
    Pinecone, Weaviate, Qdrant — similarity search
    Best for: AI/ML, RAG, recommendations
""")

print("=" * 60)
print("CONCEPT 5: MESSAGE QUEUES & ASYNC PROCESSING")
print("=" * 60)

print("""
Sync (direct):
  User → API → process → respond
  Problem: if processing takes 10s, user waits 10s.

Async (queue):
  User → API → put in queue → respond "accepted"
           Worker picks up job → processes → notifies user
  
Benefits:
  ✓ API responds instantly
  ✓ Spikes don't crash the system
  ✓ Workers can be scaled independently
  ✓ Failed jobs can be retried

Use cases:
  Sending emails, generating reports, ML inference,
  video transcoding, data pipelines

Popular queues: RabbitMQ, Apache Kafka, AWS SQS, Redis Queue
""")

print("=" * 60)
print("CONCEPT 6: CAP THEOREM")
print("=" * 60)

print("""
A distributed system can only guarantee 2 of 3:
  C — Consistency   (all nodes see same data at same time)
  A — Availability  (every request gets a response)
  P — Partition Tolerance (system works despite network splits)

Network partitions ALWAYS happen in distributed systems.
So you choose: CP or AP.

CP (Consistent + Partition Tolerant):
  → Some requests may fail if data isn't synced
  → Banks, financial systems
  Example: HBase, Zookeeper

AP (Available + Partition Tolerant):
  → Always responds, but data may be slightly stale
  → Social media, recommendation systems
  Example: Cassandra, DynamoDB

SQL databases are CA (not designed for partitions).
""")

print("=" * 60)
print("CONCEPT 7: API DESIGN BEST PRACTICES")
print("=" * 60)

print("""
VERSIONING:
  /api/v1/users       (URL versioning — most common)
  Accept: v1          (header versioning)

PAGINATION (never return all records):
  /api/v1/posts?page=2&limit=20
  /api/v1/posts?cursor=abc123   (cursor-based, better for large datasets)

RATE LIMITING:
  Limit requests per user/IP per minute.
  429 Too Many Requests when exceeded.
  Headers: X-RateLimit-Limit, X-RateLimit-Remaining

IDEMPOTENCY:
  PUT and DELETE must produce same result if called multiple times.
  POST creates new resource — NOT idempotent.

HTTP STATUS CODES:
  200 OK          | 201 Created     | 204 No Content
  400 Bad Request | 401 Unauthorized | 403 Forbidden
  404 Not Found   | 409 Conflict    | 422 Unprocessable
  429 Too Many    | 500 Server Error | 503 Unavailable
""")

print("=" * 60)
print("SUMMARY — System Design Checklist")
print("=" * 60)
print("1. Estimate scale (users, requests/sec, data size)")
print("2. Choose SQL vs NoSQL based on data model")
print("3. Add caching layer for repeated reads")
print("4. Use message queue for slow async tasks")
print("5. Load balance across multiple app servers")
print("6. Add read replicas for DB read scale")
print("7. Design API with versioning and rate limiting")
print("8. Add health checks, monitoring, alerting")
