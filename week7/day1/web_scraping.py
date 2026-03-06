# =============================================================================
# WEEK 7 - DAY 1: Web Scraping with BeautifulSoup
# Intern: ISHAAN GARG
# Topic: Parse HTML, extract data, scrape tables and text
# =============================================================================

# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time

print("=" * 55)
print("SECTION 1: HTML PARSING BASICS")
print("=" * 55)

html_sample = """
<html>
  <head><title>Navkiran's Blog</title></head>
  <body>
    <h1 class="title">Welcome to My Intern Blog</h1>
    <p id="intro">I'm learning Python at TechCorp.</p>
    <ul class="skills">
      <li class="skill">Python</li>
      <li class="skill">Machine Learning</li>
      <li class="skill">APIs</li>
    </ul>
    <a href="https://github.com/navkiran" class="link">My GitHub</a>
    <table>
      <tr><th>Week</th><th>Topic</th><th>Score</th></tr>
      <tr><td>1</td><td>Python Basics</td><td>95</td></tr>
      <tr><td>2</td><td>OOP</td><td>88</td></tr>
      <tr><td>3</td><td>Data Science</td><td>92</td></tr>
    </table>
  </body>
</html>
"""

soup = BeautifulSoup(html_sample, "html.parser")

print("Title:", soup.title.text)
print("H1:", soup.h1.text)
print("Intro (by id):", soup.find("p", id="intro").text)

skills = soup.find_all("li", class_="skill")
print("Skills:", [s.text for s in skills])

link = soup.find("a")
print(f"Link text: {link.text} | href: {link['href']}")

# Parse table
rows = soup.find("table").find_all("tr")
print("\nTable data:")
for row in rows:
    cells = row.find_all(["th", "td"])
    print("  ", [c.text for c in cells])

print("\n" + "=" * 55)
print("SECTION 2: SCRAPE A REAL WEBSITE")
print("=" * 55)

def scrape_quotes():
    """Scrape quotes from books.toscrape.com (a practice scraping site)."""
    url = "http://books.toscrape.com/"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Educational Scraper — Navkiran Intern)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        books = []
        for book in soup.select("article.product_pod")[:5]:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            rating_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
            rating_text = book.p["class"][1]
            rating = rating_map.get(rating_text, 0)
            books.append({"title": title, "price": price, "rating": rating})

        print("Top 5 books from toscrape.com:")
        for b in books:
            print(f"  [{b['rating']}★] {b['title'][:40]:40s} {b['price']}")
        return books
    except Exception as e:
        print(f"Could not scrape (offline?): {e}")
        return []

books = scrape_quotes()

print("\n" + "=" * 55)
print("SECTION 3: SCRAPING ETHICS & BEST PRACTICES")
print("=" * 55)
print("""
ALWAYS follow these rules:
  1. Check robots.txt before scraping
     → https://example.com/robots.txt
  2. Add delays between requests (be polite)
     → time.sleep(1) between pages
  3. Set a descriptive User-Agent header
  4. Respect rate limits
  5. Don't scrape login-protected pages
  6. Use official APIs when available
  7. Don't redistribute scraped data commercially
""")

print("=" * 55)
print("SECTION 4: EXTRACT DATA TO DATAFRAME AND SAVE")
print("=" * 55)

html_table = """
<table>
  <tr><th>Name</th><th>Score</th><th>Dept</th></tr>
  <tr><td>Navkiran</td><td>88</td><td>AI</td></tr>
  <tr><td>Alice</td><td>92</td><td>Web</td></tr>
  <tr><td>Bob</td><td>78</td><td>Data</td></tr>
</table>
"""
soup2 = BeautifulSoup(html_table, "html.parser")
headers = [th.text for th in soup2.find_all("th")]
rows_data = []
for row in soup2.find_all("tr")[1:]:
    rows_data.append([td.text for td in row.find_all("td")])

df = pd.DataFrame(rows_data, columns=headers)
print("Extracted table:\n", df)
df.to_csv("scraped_data.csv", index=False)
print("Saved to scraped_data.csv")

import os; os.remove("scraped_data.csv")

print("\n" + "=" * 55)
print("SUMMARY")
print("=" * 55)
print("BeautifulSoup(html, 'html.parser') → parse HTML")
print("soup.find(tag, class_/id=)         → find one element")
print("soup.find_all(tag)                 → find all elements")
print("soup.select('css.selector')        → CSS selector")
print("tag['attribute']                   → get attribute value")
print("tag.text                           → get text content")
print("time.sleep(1)                      → be polite between requests")
