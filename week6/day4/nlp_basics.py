# =============================================================================
# WEEK 6 - DAY 4: Natural Language Processing (NLP) Basics
# Intern: ISHAAN GARG
# Topic: Text preprocessing, TF-IDF, text classification
# =============================================================================

# pip install scikit-learn nltk

import re
import numpy as np
import pandas as pd
from collections import Counter

print("=" * 55)
print("SECTION 1: TEXT PREPROCESSING PIPELINE")
print("=" * 55)

sample_texts = [
    "Machine Learning is AMAZING! It's changing the world.",
    "Deep learning neural networks are very powerful tools.",
    "Natural Language Processing helps computers understand text.",
    "Python is the best programming language for AI/ML.",
    "Data Science requires statistics, programming and domain knowledge.",
]

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)     # remove non-alpha
    tokens = text.split()
    stopwords = {"is","are","the","a","an","for","and","to","it","very","of","in"}
    tokens = [t for t in tokens if t not in stopwords and len(t) > 2]
    return tokens

print("Preprocessing samples:")
all_tokens = []
for t in sample_texts:
    tokens = preprocess(t)
    print(f"  Original : {t[:50]}...")
    print(f"  Tokens   : {tokens}\n")
    all_tokens.extend(tokens)

freq = Counter(all_tokens)
print("Top 10 words:", freq.most_common(10))

print("\n" + "=" * 55)
print("SECTION 2: BAG OF WORDS (BOW)")
print("=" * 55)
print("""
Bag of Words: represent each document as a word frequency vector.
Order doesn't matter — just counts how many times each word appears.
""")

from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "I love machine learning",
    "machine learning is great",
    "deep learning neural networks",
    "I love deep learning and neural networks",
]

vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(corpus)

vocab = vectorizer.get_feature_names_out()
df_bow = pd.DataFrame(X_bow.toarray(), columns=vocab)
print("BoW Matrix:")
print(df_bow)

print("\n" + "=" * 55)
print("SECTION 3: TF-IDF")
print("=" * 55)
print("""
TF-IDF = Term Frequency × Inverse Document Frequency
  TF  : How often a word appears in THIS document
  IDF : How rare the word is across ALL documents
  
Common words like "the" get low IDF.
Rare important words get high IDF.
""")

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus)
df_tfidf = pd.DataFrame(X_tfidf.toarray().round(3), columns=tfidf.get_feature_names_out())
print("TF-IDF Matrix:")
print(df_tfidf)

print("\n" + "=" * 55)
print("SECTION 4: TEXT CLASSIFICATION — SPAM DETECTOR")
print("=" * 55)

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Mini spam dataset
spam_data = [
    ("Win a FREE iPhone now! Click here!", 1),
    ("You have won 1 million dollars. Claim now.", 1),
    ("CONGRATULATIONS! You are selected for a prize.", 1),
    ("Buy cheap medicines online — no prescription needed.", 1),
    ("Earn ₹50000 daily from home. Limited seats!", 1),
    ("Meeting rescheduled to 3pm tomorrow.", 0),
    ("Please review the attached report for Q3.", 0),
    ("Your package has been shipped. Track here.", 0),
    ("Team lunch is at 1pm in the cafeteria.", 0),
    ("Reminder: submit your timesheet by Friday.", 0),
    ("FREE gift card if you complete this survey.", 1),
    ("Can you please share the updated slides?", 0),
    ("Your account has been compromised. Act now!", 1),
    ("Happy birthday! Hope you have a great day.", 0),
    ("Get rich quick with this amazing investment.", 1),
    ("The project deadline is next Monday.", 0),
]

texts, labels = zip(*spam_data)
X_tr, X_te, y_tr, y_te = train_test_split(texts, labels, test_size=0.3, random_state=42)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("clf",   MultinomialNB())
])
pipeline.fit(X_tr, y_tr)
y_pred = pipeline.predict(X_te)

print(f"Accuracy: {accuracy_score(y_te, y_pred)*100:.1f}%")
print("\nClassification Report:")
print(classification_report(y_te, y_pred, target_names=["Ham", "Spam"]))

test_messages = [
    "You won a FREE prize! Click now!",
    "Please send me the meeting notes.",
    "Earn money fast — limited offer!",
    "See you at the standup tomorrow.",
]
print("\nLive predictions:")
for msg in test_messages:
    pred = pipeline.predict([msg])[0]
    prob = pipeline.predict_proba([msg])[0]
    label = "SPAM" if pred == 1 else "HAM"
    conf = max(prob)
    print(f"  [{label}] ({conf*100:.0f}%) — {msg}")

print("\n" + "=" * 55)
print("SUMMARY")
print("=" * 55)
print("Text preprocessing → lowercase, remove punctuation, stopwords")
print("Bag of Words        → word count matrix")
print("TF-IDF              → word importance score")
print("Pipeline            → chain vectorizer + classifier")
print("MultinomialNB       → fast text classifier")
print("ngram_range=(1,2)   → include single words and bigrams")
