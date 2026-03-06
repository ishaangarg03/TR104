# WEEK 10 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — System Design Fundamentals

System design is the "thinking big" skill of engineering. Understanding horizontal vs vertical scaling, CAP theorem, caching strategies, and message queues explained why large systems are built the way they are. The CAP theorem tradeoff — you can't have all three — was the most important conceptual insight.

**Ran today:** `day1/system_design.py`

---

## Day 2 — Design Patterns

Design patterns solve recurring problems elegantly. The Observer pattern clicked immediately — it's exactly how event systems work in JavaScript frontends too. The Decorator pattern as Python `@decorators` made me realize I've been using patterns all along without knowing it.

**Ran today:** `day2/design_patterns.py`

---

## Day 3 — Redis & Caching

Redis being 50x faster than disk databases is significant. The cache-aside pattern is now my default approach for any read-heavy data. The rate limiting simulation showed how a few lines can protect an API from abuse. Sorted sets for leaderboards were elegant.

**Ran today:** `day3/redis_caching.py`

---

## Day 4 — Message Queues

The key insight: decouple slow work from the HTTP request cycle. A user shouldn't wait 5 seconds for a report to generate — submit to queue, return immediately, process in background. The Celery + Redis setup is the standard Python pattern I'll use in real projects.

**Ran today:** `day4/message_queues.py`

---

## Day 5 — Week 10 Final Project: URL Shortener

Applying system design concepts to build a URL shortener was satisfying. Cache-aside for lookups, async queue for analytics, deterministic hash for short code generation, health endpoint, input validation — every design decision was conscious and justified. This is how production systems are built.

**Ran today:** `day5/week10_final_project.py`
