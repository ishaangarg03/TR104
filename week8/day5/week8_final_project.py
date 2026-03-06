# =============================================================================
# WEEK 8 - DAY 5: Final Project — Production-Ready ML API
# Intern: ISHAAN GARG
# Topic: Flask ML API with tests, logging, health check, Dockerfile
# =============================================================================

from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os, logging, json, unittest
from datetime import datetime

# --- App Setup ---
app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")

# --- Train Model on Startup ---
TRAIN_DATA = [
    ("This is amazing and wonderful!", "positive"),
    ("Absolutely love it. Best ever.", "positive"),
    ("Great quality, very happy.", "positive"),
    ("Fantastic product. Highly recommend.", "positive"),
    ("Terrible. Broke immediately.", "negative"),
    ("Worst purchase ever. Avoid.", "negative"),
    ("Very disappointing. Not worth it.", "negative"),
    ("Horrible quality. Waste of money.", "negative"),
    ("It is okay. Nothing special.", "neutral"),
    ("Average. Does the job.", "neutral"),
    ("Not bad, not great either.", "neutral"),
]

texts, labels = zip(*TRAIN_DATA)
MODEL = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("clf",   LogisticRegression(max_iter=500, random_state=42))
])
MODEL.fit(texts, labels)
logger.info("Sentiment model trained and ready.")

request_count = 0
start_time = datetime.utcnow()

# --- Routes ---

@app.route("/health")
def health():
    uptime = str(datetime.utcnow() - start_time).split(".")[0]
    return jsonify({"status": "healthy", "version": APP_VERSION,
                    "uptime": uptime, "requests_served": request_count})

@app.route("/api/v1/sentiment", methods=["POST"])
def predict_sentiment():
    global request_count
    body = request.get_json()
    if not body or "text" not in body:
        return jsonify({"error": "Missing 'text' field"}), 400
    text = str(body["text"]).strip()
    if not text:
        return jsonify({"error": "Text cannot be empty"}), 400
    if len(text) > 1000:
        return jsonify({"error": "Text too long (max 1000 chars)"}), 400

    prediction = MODEL.predict([text])[0]
    probs = MODEL.predict_proba([text])[0]
    classes = MODEL.classes_
    confidence = round(float(max(probs)), 4)
    request_count += 1
    logger.info(f"Predicted '{prediction}' with {confidence:.2f} confidence")
    return jsonify({
        "text":       text[:100],
        "sentiment":  prediction,
        "confidence": confidence,
        "scores":     {c: round(float(p), 4) for c, p in zip(classes, probs)}
    })

@app.route("/api/v1/batch", methods=["POST"])
def batch_predict():
    global request_count
    body = request.get_json()
    if not body or "texts" not in body:
        return jsonify({"error": "Missing 'texts' list"}), 400
    texts_input = body["texts"]
    if not isinstance(texts_input, list) or len(texts_input) == 0:
        return jsonify({"error": "'texts' must be a non-empty list"}), 400
    if len(texts_input) > 50:
        return jsonify({"error": "Max 50 texts per batch"}), 400
    results = []
    for t in texts_input:
        pred = MODEL.predict([t])[0]
        probs = MODEL.predict_proba([t])[0]
        results.append({"text": t[:60], "sentiment": pred,
                        "confidence": round(float(max(probs)), 4)})
    request_count += len(texts_input)
    return jsonify({"count": len(results), "results": results})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method Not Allowed"}), 405

# --- Tests ---

class TestSentimentAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        r = self.client.get("/health")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "healthy")

    def test_positive_sentiment(self):
        r = self.client.post("/api/v1/sentiment",
                             json={"text": "This is absolutely amazing!"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["sentiment"], "positive")

    def test_negative_sentiment(self):
        r = self.client.post("/api/v1/sentiment",
                             json={"text": "Horrible terrible worst ever."})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["sentiment"], "negative")

    def test_missing_field(self):
        r = self.client.post("/api/v1/sentiment", json={"wrong": "field"})
        self.assertEqual(r.status_code, 400)

    def test_batch_predict(self):
        r = self.client.post("/api/v1/batch",
                             json={"texts": ["Great!", "Terrible!", "It is okay."]})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["count"], 3)

    def test_batch_too_large(self):
        r = self.client.post("/api/v1/batch",
                             json={"texts": ["text"] * 100})
        self.assertEqual(r.status_code, 400)

# --- Dockerfile content printed for reference ---

DOCKERFILE = """
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir flask scikit-learn gunicorn
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "week8_final_project:app"]
"""

if __name__ == "__main__":
    print("=" * 60)
    print("  WEEK 8 FINAL PROJECT — Production ML API")
    print("  Intern: ISHAAN GARG")
    print("=" * 60)

    print("\n--- Running Tests ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSentimentAPI)
    unittest.TextTestRunner(verbosity=2).run(suite)

    print("\n--- Live API Demo ---")
    with app.test_client() as client:
        health_r = client.get("/health")
        print(f"\nGET /health → {health_r.get_json()}")

        tests_texts = [
            "This product is absolutely fantastic!",
            "Terrible quality, broke after one day.",
            "It's okay, nothing special.",
        ]
        for text in tests_texts:
            r = client.post("/api/v1/sentiment", json={"text": text})
            d = r.get_json()
            print(f"\nPOST /sentiment")
            print(f"  Text      : {text}")
            print(f"  Sentiment : {d['sentiment']} ({d['confidence']*100:.1f}% conf)")

        batch_r = client.post("/api/v1/batch",
                              json={"texts": ["Wonderful!", "Awful!", "Average."]})
        print(f"\nPOST /batch → {batch_r.get_json()}")

    print("\n--- Dockerfile for Deployment ---")
    print(DOCKERFILE)
    print("✅ Week 8 Complete — Navkiran knows Docker & Deployment!")
    print("=" * 60)
