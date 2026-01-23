"""
=============================================================
WEEK 1 - DAY 5
Topic: Setting Up GitHub Diary 
=============================================================

"""

import requests
import os
import json
from datetime import datetime

print("=" * 55)
print("WEEK 1 — FINAL PROJECT")
print("Internet Research Tool using HTTP Requests")
print("=" * 55)

print("""
This small project combines everything from Week 1:
  - Making HTTP requests (Day 1)
  - Understanding APIs and JSON (Day 1)
  - File operations (Day 3)
  - Organizing code properly (Day 3)
""")

# -------------------------------------------------------
# PROJECT: A simple "research assistant" that:
#   1. Fetches a random fact from an API
#   2. Fetches current weather for a city
#   3. Fetches a motivational quote
#   4. Saves everything to a research_report.txt file
# -------------------------------------------------------

class SimpleResearchTool:
    """
    A simple tool that gathers information from multiple APIs.

    This demonstrates:
    - Making HTTP requests to different APIs
    - Handling JSON responses
    - Error handling (what if API is down?)
    - Saving results to a file
    - Using a class to organize related functions
    """

    def __init__(self):
        # Store all gathered data here
        self.data = {}
        print("\nResearch Tool initialized!")

    def fetch_random_fact(self):
        """
        Fetches a random interesting fact from an API.
        API used: uselessfacts.jsph.pl (free, no key needed)
        """
        print("\n[1/3] Fetching random fact...")

        url = "https://uselessfacts.jsph.pl/api/v2/facts/random"

        try:
            # timeout=5 means "give up if no response in 5 seconds"
            response = requests.get(url, timeout=5)

            # Check if request was successful
            if response.status_code == 200:
                data = response.json()
                fact = data.get("text", "No fact available")
                self.data["random_fact"] = fact
                print(f"   Got it! Fact: {fact[:60]}...")
                return fact
            else:
                print(f"   API returned status {response.status_code}")
                self.data["random_fact"] = "Could not fetch fact"

        except requests.exceptions.Timeout:
            # What if the internet is slow?
            print("   Timeout! API took too long to respond.")
            self.data["random_fact"] = "Timeout error"

        except requests.exceptions.ConnectionError:
            # What if there's no internet?
            print("   Connection error! Check your internet.")
            self.data["random_fact"] = "Connection error"

        return None

    def fetch_quote(self):
        """
        Fetches a motivational quote from an API.
        API used: zenquotes.io (free, no key needed)
        """
        print("\n[2/3] Fetching motivational quote...")

        url = "https://zenquotes.io/api/random"

        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                # This API returns a list, first item is the quote
                quote_text = data[0].get("q", "No quote")
                quote_author = data[0].get("a", "Unknown")

                quote = f'"{quote_text}" — {quote_author}'
                self.data["quote"] = quote
                print(f"   Got it! By: {quote_author}")
                return quote
            else:
                self.data["quote"] = "Could not fetch quote"

        except Exception as e:
            # Catching ANY exception with 'Exception'
            # In production code, be more specific
            print(f"   Error: {e}")
            self.data["quote"] = f"Error: {e}"

        return None

    def fetch_joke(self):
        """
        Fetches a programming joke.
        API: official-joke-api.appspot.com (free, no key needed)
        """
        print("\n[3/3] Fetching a joke...")

        url = "https://official-joke-api.appspot.com/jokes/programming/random"

        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                # This API returns a list
                if isinstance(data, list) and len(data) > 0:
                    joke = data[0]
                    full_joke = f"{joke['setup']} ... {joke['punchline']}"
                    self.data["joke"] = full_joke
                    print(f"   Got it! Setup: {joke['setup'][:40]}...")
                    return full_joke

        except Exception as e:
            print(f"   Error: {e}")
            self.data["joke"] = f"Error: {e}"

        return None

    def save_report(self, filename="week1_research_report.txt"):
        """
        Saves all gathered data to a text file.
        This is our "output" — a file we can push to GitHub.
        """
        print(f"\n Saving report to {filename}...")

        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        


# -------------------------------------------------------
# RUNNING THE TOOL
# -------------------------------------------------------

# Create the tool
tool = SimpleResearchTool()

# Gather data from APIs
tool.fetch_random_fact()
tool.fetch_quote()
tool.fetch_joke()

# Save the report
tool.save_report("/tmp/week1/day5/week1_research_report.txt")

# Print the final summary
print("\n" + "=" * 55)
print("WEEK 1 COMPLETE!")
print("=" * 55)
print("""
 What I built this week:
  - how_internet_works.py  → HTTP requests, GET, POST, status codes
  - terminal_commands.py   → Terminal, file operations, os module
  - git_github_basics.py   → Git commits, .gitignore, GitHub workflow
  - python_environment.py  → venv, pip, requirements.txt, VS Code
  - what_is_ai_ml.py       → AI, ML, LLMs, tokens explained
  - week1_final_project.py → Research tool using 3 APIs (this file!)

""")
