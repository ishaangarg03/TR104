# =============================================================================
# WEEK 9 - DAY 5: Final Project — AI Study Assistant Chatbot
# Intern: ISHAAN GARG
# Topic: Conversational chatbot with RAG + tools (no API key needed)
# =============================================================================

import re
import json
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

print("=" * 60)
print("  ISHAAN GARG — AI STUDY ASSISTANT CHATBOT")
print("=" * 60)

# ─── Knowledge Base ───────────────────────────────────────────────
KNOWLEDGE = [
    {"id":1,"topic":"Python Lists","text":"Lists are ordered, mutable collections. Created with []. Methods: append(), remove(), pop(), sort(), len(). Slicing: list[start:end]."},
    {"id":2,"topic":"Python Dicts","text":"Dictionaries store key-value pairs. Created with {}. Access with dict[key] or .get(). Methods: .keys(), .values(), .items(). Supports dict comprehension."},
    {"id":3,"topic":"OOP Classes","text":"Classes are blueprints for objects. __init__ is the constructor. self refers to the instance. Inheritance uses parentheses: class Child(Parent). Use super() to call parent methods."},
    {"id":4,"topic":"Machine Learning","text":"ML models learn patterns from data. Steps: load data, split train/test, scale features, train model, evaluate. Key metrics: accuracy, precision, recall, F1."},
    {"id":5,"topic":"Neural Networks","text":"Neural networks have input, hidden, and output layers. Activation functions: ReLU for hidden, sigmoid for binary, softmax for multiclass. Train with backprop and optimizer like Adam."},
    {"id":6,"topic":"NumPy","text":"NumPy arrays are fast numerical arrays. Create with np.array(). Operations are element-wise. Key functions: np.mean, np.std, np.sum, np.reshape, np.linspace."},
    {"id":7,"topic":"Pandas","text":"Pandas DataFrames are 2D tables. Filter with df[condition]. Group with groupby(). Handle nulls with fillna() and dropna(). Load CSV with read_csv(), save with to_csv()."},
    {"id":8,"topic":"Flask API","text":"Flask is a Python web framework. Define routes with @app.route(). Return JSON with jsonify(). Handle POST with request.get_json(). Use run(debug=True) in development only."},
    {"id":9,"topic":"Git","text":"Git tracks code changes. Key commands: git init, git add, git commit -m, git push, git pull, git branch, git merge, git log. Always write meaningful commit messages."},
    {"id":10,"topic":"SQL","text":"SQL queries data from tables. SELECT * FROM table; WHERE filters rows; GROUP BY aggregates; JOIN combines tables; INSERT adds rows; UPDATE modifies; DELETE removes rows."},
    {"id":11,"topic":"Docker","text":"Docker containers package apps. Dockerfile defines the image. docker build creates it, docker run starts a container. Use docker-compose for multi-service setups."},
    {"id":12,"topic":"Error Handling","text":"Python uses try/except to catch errors. except TypeError catches specific errors. else runs if no exception. finally always runs. Raise errors with raise ValueError('message')."},
]

# ─── Vector Index ─────────────────────────────────────────────────
corpus = [d["text"] for d in KNOWLEDGE]
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000)
vectors = vectorizer.fit_transform(corpus)

def retrieve(query, top_k=2):
    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, vectors).flatten()
    top_idx = scores.argsort()[-top_k:][::-1]
    return [(KNOWLEDGE[i], float(scores[i])) for i in top_idx if scores[i] > 0.01]

# ─── Tools ────────────────────────────────────────────────────────
def calc(expr):
    try:
        if not re.match(r"^[\d\s\+\-\*\/\.\(\)]+$", expr):
            return "Invalid expression"
        return str(round(eval(expr), 6))
    except:
        return "Calculation error"

def get_time():
    return datetime.now().strftime("%A, %d %B %Y — %H:%M:%S")

# ─── Response Generator (rule-based LLM simulator) ────────────────
class StudyAssistant:
    def __init__(self):
        self.history = []
        self.session_questions = 0

    def chat(self, user_input):
        self.session_questions += 1
        ui = user_input.strip().lower()
        self.history.append({"role":"user","content":user_input})

        # Greetings
        if any(w in ui for w in ["hello","hi","hey","namaste"]):
            reply = "Hello Navkiran! 👋 I'm your Study Assistant. Ask me anything about Python, ML, Flask, SQL, Git, or Docker!"

        # Time
        elif any(w in ui for w in ["time","date","today"]):
            reply = f"🕐 {get_time()}"

        # Calculator
        elif any(w in ui for w in ["calculate","compute","what is"]) and re.search(r"\d[\d\s\+\-\*\/\.\(\)]+\d", user_input):
            nums = re.search(r"[\d\s\+\-\*\/\.\(\)]+", user_input).group()
            result = calc(nums.strip())
            reply = f"🔢 {nums.strip()} = **{result}**"

        # Quiz mode
        elif "quiz" in ui or "test me" in ui:
            questions = [
                ("What method adds an item to the end of a list?", "append()"),
                ("What does OOP stand for?", "Object Oriented Programming"),
                ("What is the Python keyword to define a function?", "def"),
                ("What does CSV stand for?", "Comma Separated Values"),
                ("Which ML metric measures false negative rate?", "Recall"),
            ]
            import random
            q, a = random.choice(questions)
            reply = f"📝 **Quiz Time!**\n\nQuestion: {q}\n\n(Think of your answer, then ask me to reveal it!)\n_Hint: The answer is {len(a)} characters long._"

        # Help / menu
        elif any(w in ui for w in ["help","what can","menu","topics"]):
            topics = ", ".join(d["topic"] for d in KNOWLEDGE)
            reply = f"📚 I can help with: {topics}\n\nAlso try: 'quiz me', 'calculate 25*4', 'what time is it'"

        # Stats
        elif any(w in ui for w in ["stat","history","how many","session"]):
            reply = f"📊 Session stats:\n  Questions asked: {self.session_questions}\n  Topics in knowledge base: {len(KNOWLEDGE)}"

        # RAG knowledge lookup
        else:
            docs = retrieve(user_input, top_k=2)
            if docs and docs[0][1] > 0.05:
                best_doc, score = docs[0]
                context = best_doc["text"]
                if len(docs) > 1 and docs[1][1] > 0.05:
                    context += "\n\nAdditional context: " + docs[1][0]["text"]
                reply = f"📖 **{best_doc['topic']}**\n\n{context}"
                if score < 0.3:
                    reply += "\n\n_(Confidence: moderate — ask more specifically for better results)_"
            else:
                reply = ("🤔 I'm not sure about that. Try asking about: Python, ML, Flask, "
                         "SQL, Git, Docker, NumPy, Pandas, OOP, or Error Handling.")

        self.history.append({"role":"assistant","content":reply})
        return reply

    def show_history(self):
        print("\n" + "=" * 60)
        print("CONVERSATION HISTORY")
        print("=" * 60)
        for msg in self.history:
            role = "You" if msg["role"] == "user" else "Assistant"
            print(f"\n[{role}]: {msg['content'][:200]}")

# ─── Demo Conversation ────────────────────────────────────────────
assistant = StudyAssistant()

conversations = [
    "Hello!",
    "What topics can you help me with?",
    "Explain Python lists to me",
    "How do I handle errors in Python?",
    "Tell me about machine learning",
    "How do neural networks work?",
    "What is Flask used for?",
    "Calculate 128 * 256 + 1024",
    "What time is it?",
    "Quiz me!",
    "Tell me about Docker",
    "How does SQL JOIN work?",
    "Session stats",
]

print("\n" + "─" * 60)
print("DEMO CONVERSATION")
print("─" * 60)

for question in conversations:
    print(f"\n🧑 You: {question}")
    response = assistant.chat(question)
    print(f"🤖 Assistant: {response[:300]}")
    if len(response) > 300:
        print("   ...")

assistant.show_history()
print(f"\n✅ Week 9 Complete — Navkiran built an AI chatbot with RAG + tools!")
print("=" * 60)
