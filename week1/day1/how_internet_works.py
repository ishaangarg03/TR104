"""
=============================================================
WEEK 1 - DAY 1
Topic: How the Internet Works
=============================================================

WHAT I LEARNED TODAY (notes):
-------------------------------
- Internet = computers talking to each other using rules called "protocols"
- HTTP  = HyperText Transfer Protocol = the rules browsers use to ask for webpages
- HTTPS = Secure version of HTTP (the S = SSL encryption)
- URL   = Uniform Resource Locator = the address of a webpage
         Example: https://www.google.com/search?q=hello
                  |_____|  |_____________| |______| |_____|
                  protocol    domain        path     query

- When you type a URL in browser:
  1. Browser asks DNS: "what is the IP address of google.com?"
  2. DNS replies: "it's 142.250.195.46"
  3. Browser sends HTTP GET request to that IP address
  4. Google's server sends back HTML/CSS/JS files
  5. Browser renders those files as the webpage you see

STATUS CODES (what servers reply with):
  200 = OK (success)
  404 = Not Found (wrong URL)
  500 = Server Error (something broke on server side)
  403 = Forbidden (you don't have permission)
  301 = Redirect (page moved to new URL)
=============================================================
"""

# -------------------------------------------------------
# Let's use Python to make a real HTTP request
# This is exactly what your browser does when you visit a site
# -------------------------------------------------------

# 'requests' is a Python library that lets us make HTTP requests
# Install it by running: pip install requests
import requests

# -------------------------------------------------------
# MAKING A SIMPLE GET REQUEST
# GET = "please give me data from this URL"
# -------------------------------------------------------

print("=" * 50)
print("MAKING AN HTTP GET REQUEST")
print("=" * 50)

# We are calling a free public API that returns a random joke
# This is exactly what happens when your browser visits a URL
url = "https://official-joke-api.appspot.com/random_joke"

# requests.get() sends a GET request to the URL
# The server sends back a "response" object
response = requests.get(url)

# -------------------------------------------------------
# READING THE RESPONSE
# -------------------------------------------------------

# .status_code tells us if request was successful
# 200 = success, 404 = not found, 500 = server error
print(f"\nStatus Code: {response.status_code}")

if response.status_code == 200:
    print("Request was SUCCESSFUL!")
else:
    print("Something went wrong!")

# .headers tells us information about the response
# (like content type, server info, etc.)
print(f"\nContent Type: {response.headers.get('Content-Type')}")

# .text gives us the raw response as a string
print(f"\nRaw Response Text:\n{response.text}")

# .json() converts the JSON response into a Python dictionary
# JSON = JavaScript Object Notation = a format for sending data
data = response.json()
print(f"\nParsed as Python Dictionary:")
print(f"  Type of data: {type(data)}")
print(f"  Keys in data: {list(data.keys())}")

# Now we can access individual fields like a dictionary
print(f"\n--- JOKE OF THE DAY ---")
print(f"Setup:     {data['setup']}")
print(f"Punchline: {data['punchline']}")
print("-" * 30)

# -------------------------------------------------------
# UNDERSTANDING URLs
# -------------------------------------------------------

print("\n" + "=" * 50)
print("UNDERSTANDING URLs")
print("=" * 50)

# We can break a URL into parts using Python
from urllib.parse import urlparse, urlencode

sample_url = "https://www.google.com/search?q=python+tutorial&lang=en"

# urlparse breaks the URL into components
parsed = urlparse(sample_url)

print(f"\nFull URL:  {sample_url}")
print(f"Scheme:    {parsed.scheme}")    # https
print(f"Domain:    {parsed.netloc}")    # www.google.com
print(f"Path:      {parsed.path}")      # /search
print(f"Query:     {parsed.query}")     # q=python+tutorial&lang=en

# -------------------------------------------------------
# DIFFERENT HTTP METHODS
# -------------------------------------------------------

print("\n" + "=" * 50)
print("HTTP METHODS EXPLAINED")
print("=" * 50)

# GET    = Read/fetch data (like visiting a webpage)
# POST   = Send/create new data (like submitting a form)
# PUT    = Update existing data
# DELETE = Delete data

print("""
HTTP Methods:
  GET    → Read data      (Example: loading your Instagram feed)
  POST   → Create data    (Example: posting a new photo)
  PUT    → Update data    (Example: editing your bio)
  DELETE → Delete data    (Example: deleting a post)
""")

# Let's try a POST request to a testing API
# JSONPlaceholder is a fake API for practice
post_url = "https://jsonplaceholder.typicode.com/posts"

# This is data we want to SEND to the server
# In real apps this could be a signup form, a new post, etc.
new_post = {
    "title": "My First API Post",
    "body": "I learned how to make HTTP requests today!",
    "userId": 1
}

# requests.post() sends a POST request with our data
post_response = requests.post(post_url, json=new_post)

print(f"POST Request Status: {post_response.status_code}")
# 201 = Created (server made a new resource)

created_data = post_response.json()
print(f"Server gave our post an ID: {created_data['id']}")
print(f"Title confirmed: {created_data['title']}")

print("\n Day 1 Complete! HTTP requests understood.")
