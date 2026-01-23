"""
=============================================================
WEEK 1 - DAY 4
Topic: What is AI? What is Machine Learning?
       Research notes + simple Python demonstrations
=============================================================

MY RESEARCH NOTES FROM TODAY'S WEB SURFING:
--------------------------------------------

ARTIFICIAL INTELLIGENCE (AI):
  - AI = making computers do things that normally need human intelligence
  - Examples: understanding language, recognizing images, making decisions
  - AI is the BIG category that contains Machine Learning

MACHINE LEARNING (ML):
  - ML = a TYPE of AI where computers LEARN from data
  - Instead of coding rules manually, you give the computer DATA
    and it figures out the rules itself
  - Example: Instead of writing "if email contains 'win money' → spam"
             you show it 10,000 emails labeled spam/not-spam
             and it learns the pattern on its own

DEEP LEARNING (DL):
  - DL = a TYPE of Machine Learning using "neural networks"
  - Inspired by how the human brain works (neurons connected to neurons)
  - Best for: images, audio, text
  - Requires a LOT of data and computing power

LARGE LANGUAGE MODELS (LLMs):
  - LLMs = Deep Learning models trained on HUGE amounts of text
  - They learn to predict "what word comes next"
  - After training on billions of sentences, they understand language
  - Examples: GPT-4, Llama, Gemini, Claude
  - THIS is what PodGen AI uses (Llama 3.3 70B via Groq)

RELATIONSHIP:
  AI
  └── Machine Learning
      └── Deep Learning
          └── Large Language Models (LLMs)
              └── ChatGPT, Claude, Llama, Gemini...

=============================================================
"""

# -------------------------------------------------------
# DEMONSTRATING AI CONCEPTS WITH SIMPLE PYTHON CODE
# No libraries needed — just pure Python logic
# -------------------------------------------------------

print("=" * 55)
print("AI & ML CONCEPTS — DEMONSTRATED WITH SIMPLE PYTHON")
print("=" * 55)

# -------------------------------------------------------
# CONCEPT 1: Rule-based system (OLD way — NOT machine learning)
# -------------------------------------------------------

print("\n--- CONCEPT 1: Old Way — Rule-Based System ---")
print("(This is NOT AI/ML — just if/else rules written by humans)\n")

def spam_detector_rules(email_text):
    """
    Old-fashioned spam detector.
    A human manually wrote these rules.
    Problem: hackers can easily bypass rules they know about.
    """
    email_lower = email_text.lower()

    # Rules written manually by a programmer
    spam_keywords = ["win money", "free prize", "click here", "urgent",
                     "congratulations you won", "bank account", "nigerian prince"]

    for keyword in spam_keywords:
        if keyword in email_lower:
            return "SPAM"

    return "NOT SPAM"

# Testing our rule-based detector
test_emails = [
    "Hi Navkiran, meeting at 3pm today?",
    "CONGRATULATIONS YOU WON $1,000,000! Click here to claim!",
    "Your order has been shipped. Track it here.",
    "URGENT: Your bank account needs verification NOW",
    "Let's catch up for lunch tomorrow?",
]

print("Testing rule-based spam detector:")
for email in test_emails:
    result = spam_detector_rules(email)
    icon = "🚫" if result == "SPAM" else "✓"
    print(f"  {icon} {result:10} | {email[:50]}...")

print("\n Problem: What if spammer writes 'w1n m0ney'? Rules fail!")

# -------------------------------------------------------
# CONCEPT 2: How ML learns from data (simplified simulation)
# -------------------------------------------------------

print("\n--- CONCEPT 2: How Machine Learning Works ---")
print("(Simplified simulation — real ML uses math and tensors)\n")

# In real ML:
# 1. You have TRAINING DATA (examples with correct answers)
# 2. The model learns PATTERNS from this data
# 3. It can then predict answers for NEW unseen data

# Simulating a very simple "learning" process
# Imagine teaching a child: "These are cats, these are dogs"

training_data = [
    # (features,                    label)
    # (has_fur, meows, barks, size) → animal
    ((True,  True,  False, "small"),  "cat"),
    ((True,  True,  False, "small"),  "cat"),
    ((True,  False, True,  "large"),  "dog"),
    ((True,  False, True,  "medium"), "dog"),
    ((True,  True,  False, "medium"), "cat"),
    ((True,  False, True,  "large"),  "dog"),
]

# "Learning" = counting patterns in training data
cat_patterns = {"meows": 0, "barks": 0}
dog_patterns = {"meows": 0, "barks": 0}

for features, label in training_data:
    has_fur, meows, barks, size = features
    if label == "cat":
        if meows: cat_patterns["meows"] += 1
        if barks: cat_patterns["barks"] += 1
    else:
        if meows: dog_patterns["meows"] += 1
        if barks: dog_patterns["barks"] += 1

print("What the model LEARNED from training data:")
print(f"  Cats: meow={cat_patterns['meows']} times, bark={cat_patterns['barks']} times")
print(f"  Dogs: meow={dog_patterns['meows']} times, bark={dog_patterns['barks']} times")

# Simple prediction based on learned patterns
def predict_animal(meows, barks):
    """
    Predict if animal is cat or dog based on what we learned.
    Real ML does this with mathematical weights, not if/else.
    """
    if meows and not barks:
        return "cat (learned: cats meow, don't bark)"
    elif barks and not meows:
        return "dog (learned: dogs bark, don't meow)"
    else:
        return "uncertain"

print("\nMaking predictions on NEW animals (never seen before):")
print(f"  Animal that meows, doesn't bark → {predict_animal(True, False)}")
print(f"  Animal that barks, doesn't meow → {predict_animal(False, True)}")

# -------------------------------------------------------
# CONCEPT 3: What tokens are (important for LLMs)
# -------------------------------------------------------

print("\n--- CONCEPT 3: What are Tokens? ---")
print("(LLMs don't read words — they read TOKENS)\n")

# Tokens are pieces of text. They can be:
# - A whole word: "cat" = 1 token
# - Part of a word: "un" + "believ" + "able" = 3 tokens
# - A punctuation mark: "!" = 1 token
# - A space + word: " the" = 1 token

def simple_tokenizer(text):
    """
    Very simplified tokenizer.
    Real LLM tokenizers (like BPE) are more sophisticated.
    """
    # Split by spaces and punctuation
    import re
    tokens = re.findall(r'\w+|[^\w\s]', text)
    return tokens

examples = [
    "Hello world!",
    "I love machine learning.",
    "PodGen AI generates podcasts automatically.",
]

print("How text becomes tokens (what the LLM actually reads):")
for example in examples:
    tokens = simple_tokenizer(example)
    print(f"\n  Text:   '{example}'")
    print(f"  Tokens: {tokens}")
    print(f"  Count:  {len(tokens)} tokens")

print("""
In real LLMs:
  - 1 token ≈ 0.75 words on average
  - GPT-4 has a 128,000 token context window
  - Llama 3.3 (used in PodGen AI) has 128,000 tokens
  - More tokens = more expensive API calls
  - "max_tokens" in API = max tokens in the RESPONSE
""")

# -------------------------------------------------------
# CONCEPT 4: Calling an actual LLM API
# -------------------------------------------------------

print("--- CONCEPT 4: What Calling an LLM API Looks Like ---")

print("""
When PodGen AI calls Groq, this is what happens:

  import os
  from groq import Groq

  client = Groq(api_key=os.getenv("GROQ_API_KEY"))

  response = client.chat.completions.create(
      model="llama-3.3-70b-versatile",    # which LLM to use
      messages=[
          {
              "role": "system",            # sets the AI's personality
              "content": "You are a podcast scriptwriter."
          },
          {
              "role": "user",              # our question/request
              "content": "Write a podcast script about AI."
          }
      ],
      max_tokens=2000,                     # max length of response
      temperature=0.7                      # 0=consistent, 1=creative
  )

  answer = response.choices[0].message.content
  print(answer)  # prints the generated script

This is EXACTLY what groq_service.py in PodGen AI does!
""")

# -------------------------------------------------------
# RESEARCH LINKS I VISITED TODAY
# -------------------------------------------------------

print("=" * 55)
print("WEBSITES I SURFED TODAY FOR RESEARCH")
print("=" * 55)

resources = [
    ("What is AI?",          "https://www.ibm.com/topics/artificial-intelligence"),
    ("What is ML?",          "https://www.ibm.com/topics/machine-learning"),
    ("What are LLMs?",       "https://www.cloudflare.com/learning/ai/what-is-a-large-language-model/"),
    ("Groq API docs",        "https://console.groq.com/docs/openai"),
    ("Tokenizer visualizer", "https://platform.openai.com/tokenizer"),
]

for title, url in resources:
    print(f"  {title}")
    print(f"    {url}\n")

print(" Day 4 Complete! AI and ML concepts understood.")
