# =============================================================================
# WEEK 7 - DAY 5: Final Project — Threaded Web Data Pipeline
# Intern: ISHAAN GARG
# Topic: Scrape multiple endpoints concurrently, clean, save
# =============================================================================

import requests
import json
import re
import os
import time
import concurrent.futures
from datetime import datetime
import pandas as pd

print("=" * 60)
print("  ISHAAN GARG — THREADED WEB DATA PIPELINE")
print("=" * 60)

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_user(user_id):
    try:
        r = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  Error fetching user {user_id}: {e}")
        return None

def fetch_posts_for_user(user_id):
    try:
        r = requests.get(f"{BASE_URL}/posts", params={"userId": user_id}, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return []

def clean_user(user):
    if not user: return None
    return {
        "id":       user["id"],
        "name":     user["name"].strip().title(),
        "email":    user["email"].lower().strip(),
        "city":     user.get("address", {}).get("city", "Unknown"),
        "company":  user.get("company", {}).get("name", "Unknown"),
        "website":  user.get("website", "")
    }

# Step 1: Fetch all 10 users concurrently
print("\n--- Step 1: Fetch Users (Concurrent) ---")
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    raw_users = list(ex.map(fetch_user, range(1, 11)))
elapsed = time.time() - start
print(f"Fetched {len(raw_users)} users in {elapsed:.2f}s")

# Step 2: Clean users
users = [clean_user(u) for u in raw_users if u]
print(f"Cleaned {len(users)} users")

# Step 3: Fetch posts for all users concurrently
print("\n--- Step 2: Fetch Posts (Concurrent) ---")
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    all_posts = list(ex.map(fetch_posts_for_user, [u["id"] for u in users]))
elapsed = time.time() - start
total_posts = sum(len(p) for p in all_posts)
print(f"Fetched {total_posts} posts across {len(users)} users in {elapsed:.2f}s")

# Step 4: Enrich users with post stats
print("\n--- Step 3: Enrich with Post Stats ---")
for user, posts in zip(users, all_posts):
    user["post_count"] = len(posts)
    if posts:
        avg_title_len = sum(len(p["title"]) for p in posts) / len(posts)
        user["avg_title_length"] = round(avg_title_len, 1)
    else:
        user["avg_title_length"] = 0

# Step 5: Analysis
df = pd.DataFrame(users)
print("\nEnriched User Table:")
print(df[["name", "city", "company", "post_count", "avg_title_length"]].to_string(index=False))

print("\n--- Analysis ---")
print(f"Total posts         : {df['post_count'].sum()}")
print(f"Avg posts per user  : {df['post_count'].mean():.1f}")
print(f"Most prolific user  : {df.loc[df['post_count'].idxmax(), 'name']}")
print(f"Unique cities       : {df['city'].nunique()}")

print("\nUsers by city:")
print(df["city"].value_counts().head(5))

# Step 6: Save
df.to_csv("pipeline_output.csv", index=False)
print("\nSaved: pipeline_output.csv")

report = {
    "generated_at": datetime.now().isoformat(),
    "users": users,
    "stats": {
        "total_users": len(users),
        "total_posts": int(df["post_count"].sum()),
        "avg_posts": round(df["post_count"].mean(), 2),
    }
}
with open("pipeline_output.json", "w") as f:
    json.dump(report, f, indent=2)
print("Saved: pipeline_output.json")

for fname in ["pipeline_output.csv", "pipeline_output.json"]:
    if os.path.exists(fname): os.remove(fname)

print("\n✅ Week 7 Complete — Navkiran mastered Scraping, Automation & Concurrency!")
print("=" * 60)
