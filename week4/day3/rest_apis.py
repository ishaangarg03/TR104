# =============================================================================
# WEEK 4 - DAY 3: Working with REST APIs
# Intern: ISHAAN GARG
# Topic: GET/POST requests, headers, auth, parsing JSON responses
# =============================================================================

# pip install requests

import requests
import json
import os

print("=" * 50)
print("SECTION 1: BASIC GET REQUEST")
print("=" * 50)

# Public API — no key needed
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Response JSON: {response.json()}")

print("\n" + "=" * 50)
print("SECTION 2: GET LIST OF RESOURCES")
print("=" * 50)

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
print(f"Fetched {len(users)} users")
for user in users[:3]:
    print(f"  {user['id']}. {user['name']} | {user['email']} | {user['address']['city']}")

print("\n" + "=" * 50)
print("SECTION 3: QUERY PARAMETERS")
print("=" * 50)

params = {"userId": 1, "_limit": 5}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
posts = response.json()
print(f"Posts by userId=1 (limit 5):")
for post in posts:
    print(f"  [{post['id']}] {post['title'][:50]}...")

print("\n" + "=" * 50)
print("SECTION 4: POST REQUEST — SEND DATA")
print("=" * 50)

new_post = {
    "title": "My First API Post",
    "body": "Learning REST APIs at TechCorp internship!",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post,
    headers={"Content-Type": "application/json"}
)

print(f"Status: {response.status_code}")  # 201 = Created
print("Created post:", response.json())

print("\n" + "=" * 50)
print("SECTION 5: ERROR HANDLING WITH APIS")
print("=" * 50)

def safe_get(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()   # raises exception for 4xx/5xx
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Connection Error: Check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None

data = safe_get("https://jsonplaceholder.typicode.com/posts/1")
print("Safe GET result:", data["title"] if data else "Failed")

bad = safe_get("https://jsonplaceholder.typicode.com/posts/9999")
print("Non-existent resource:", bad)

print("\n" + "=" * 50)
print("SECTION 6: HEADERS AND MOCK AUTH")
print("=" * 50)

headers = {
    "Authorization": "Bearer my_fake_token_12345",
    "Accept": "application/json",
    "User-Agent": "NavkiranIntern/1.0"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1",
    headers=headers
)
print("With custom headers, status:", response.status_code)
print("Response:", response.json())

print("\n" + "=" * 50)
print("SECTION 7: REAL PUBLIC API — COUNTRY INFO")
print("=" * 50)

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    data = safe_get(url)
    if data:
        c = data[0]
        print(f"\nCountry: {c['name']['common']}")
        print(f"  Capital   : {c.get('capital', ['N/A'])[0]}")
        print(f"  Population: {c.get('population', 0):,}")
        print(f"  Region    : {c.get('region', 'N/A')}")
        currencies = c.get("currencies", {})
        for code, details in currencies.items():
            print(f"  Currency  : {details['name']} ({code})")

get_country_info("india")
get_country_info("japan")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("requests.get(url)        → fetch data")
print("requests.post(url, json) → send data")
print("response.status_code     → HTTP status (200, 201, 404...)")
print("response.json()          → parse JSON response")
print("params={}                → URL query parameters")
print("headers={}               → auth tokens, content type")
print("raise_for_status()       → raise error on bad status")
print("timeout=10               → prevent hanging forever")
