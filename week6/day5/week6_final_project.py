# =============================================================================
# WEEK 6 - DAY 5: Final Project — Sentiment Analysis App
# Intern: ISHAAN GARG
# Topic: Train a sentiment classifier + interactive prediction
# =============================================================================

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
import re

print("=" * 60)
print("  ISHAAN GARG — SENTIMENT ANALYSIS APP")
print("=" * 60)

# --- Dataset ---
reviews = [
    ("This product is absolutely amazing! Best purchase ever.", "positive"),
    ("Terrible quality. Broke after one day. Waste of money.", "negative"),
    ("Good value for money. Works as expected.", "positive"),
    ("Very disappointed. Did not match the description at all.", "negative"),
    ("Excellent! Fast shipping and great packaging.", "positive"),
    ("Stopped working after a week. Very poor quality.", "negative"),
    ("Decent product. Not the best but does the job.", "neutral"),
    ("Outstanding! Exceeded all my expectations.", "positive"),
    ("Okay product. Nothing special, nothing bad.", "neutral"),
    ("Horrible experience. Customer service was rude.", "negative"),
    ("Love it! Will definitely buy again.", "positive"),
    ("Average quality. Price is too high for what you get.", "neutral"),
    ("Fantastic! 5 stars without any hesitation.", "positive"),
    ("Worst purchase of my life. Complete junk.", "negative"),
    ("It's fine. Does what it says on the box.", "neutral"),
    ("Incredible product. Life-changing!", "positive"),
    ("Faulty item received. Very unhappy.", "negative"),
    ("Pretty good overall. Minor issues but manageable.", "positive"),
    ("Not impressed at all. Expected much better.", "negative"),
    ("Solid product. Reliable and well-built.", "positive"),
    ("Exactly what I needed. Very happy with this.", "positive"),
    ("Waste of money. Don't buy this.", "negative"),
    ("OK for the price. Nothing extraordinary.", "neutral"),
    ("Simply the best product in this category!", "positive"),
    ("Arrived broken. Very poor packaging.", "negative"),
    ("Works great after a few days of use.", "positive"),
    ("Meh. Expected better based on reviews.", "neutral"),
    ("Great product, fast delivery, easy setup.", "positive"),
    ("Doesn't work as described. Very misleading.", "negative"),
    ("Good enough for occasional use.", "neutral"),
]

texts, labels = zip(*reviews)
label_map = {"positive": 2, "neutral": 1, "negative": 0}
y = [label_map[l] for l in labels]

print(f"\nDataset: {len(reviews)} reviews")
print(f"Distribution: {pd.Series(labels).value_counts().to_dict()}")

# --- Preprocessing ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s!?]", "", text)
    return text.strip()

texts_clean = [clean_text(t) for t in texts]

# --- Train ---
X_tr, X_te, y_tr, y_te = train_test_split(texts_clean, y, test_size=0.25, random_state=42, stratify=y)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), max_features=500, sublinear_tf=True)),
    ("clf",   LogisticRegression(max_iter=500, C=1.0, random_state=42))
])
pipeline.fit(X_tr, y_tr)

y_pred = pipeline.predict(X_te)
acc = accuracy_score(y_te, y_pred)

print(f"\nTest Accuracy : {acc*100:.1f}%")
cv_scores = cross_val_score(pipeline, texts_clean, y, cv=5, scoring="accuracy")
print(f"CV Mean       : {cv_scores.mean()*100:.1f}% ± {cv_scores.std()*100:.1f}%")

print("\nClassification Report:")
print(classification_report(y_te, y_pred, target_names=["Negative","Neutral","Positive"]))

# --- Confusion matrix ---
cm = confusion_matrix(y_te, y_pred)
print("Confusion Matrix (rows=actual, cols=predicted):")
print(f"           Neg  Neu  Pos")
for i, row in enumerate(cm):
    name = ["Negative","Neutral ","Positive"][i]
    print(f"  {name}: {row}")

# --- Interactive predictor ---
def predict_sentiment(text):
    cleaned = clean_text(text)
    pred = pipeline.predict([cleaned])[0]
    probs = pipeline.predict_proba([cleaned])[0]
    label = ["Negative 😠", "Neutral 😐", "Positive 😊"][pred]
    confidence = max(probs)
    return label, confidence, probs

print("\n" + "=" * 60)
print("INTERACTIVE SENTIMENT PREDICTIONS")
print("=" * 60)

test_reviews = [
    "This is the best thing I have ever bought!",
    "Totally useless product. Never buying again.",
    "It is okay. Neither good nor bad.",
    "Absolutely love this! Highly recommend.",
    "Disappointed with the quality. Not worth it.",
    "Average product. Does its job sometimes.",
    "Top notch quality! Five stars!",
    "Broken on arrival. Terrible.",
]

print(f"\n{'Review':45s} | {'Sentiment':15s} | {'Confidence'}")
print("-" * 75)
for review in test_reviews:
    sentiment, conf, probs = predict_sentiment(review)
    print(f"  {review[:43]:43s} | {sentiment:15s} | {conf*100:.1f}%")

# --- Summary stats ---
all_preds = [predict_sentiment(t)[0] for t in test_reviews]
print("\nPrediction breakdown:")
from collections import Counter
print(Counter(all_preds))

print("\n✅ Week 6 Complete — Navkiran has mastered Deep Learning & NLP basics!")
print("=" * 60)
