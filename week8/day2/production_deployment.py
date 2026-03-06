# =============================================================================
# WEEK 8 - DAY 2: Deploying a Flask App — Production Best Practices
# Intern: ISHAAN GARG
# Topic: Gunicorn, environment variables, logging, health checks
# =============================================================================

from flask import Flask, jsonify, request
import os
import logging
from datetime import datetime

# --- Production-grade Flask App ---

app = Flask(__name__)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Config from environment variables (never hardcode secrets!)
class Config:
    SECRET_KEY    = os.environ.get("SECRET_KEY", "dev-secret-change-in-prod")
    DEBUG         = os.environ.get("DEBUG", "false").lower() == "true"
    MAX_REQUESTS  = int(os.environ.get("MAX_REQUESTS", 100))
    APP_VERSION   = os.environ.get("APP_VERSION", "1.0.0")

config = Config()

# --- Routes ---

@app.route("/health")
def health():
    """Health check endpoint — required for load balancers."""
    return jsonify({
        "status":    "healthy",
        "version":   config.APP_VERSION,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/api/v1/predict", methods=["POST"])
def predict():
    body = request.get_json()
    if not body or "text" not in body:
        logger.warning("Bad request: missing 'text' field")
        return jsonify({"error": "Missing 'text' field"}), 400

    text = body["text"]
    logger.info(f"Prediction request | length={len(text)}")

    # Simulate prediction
    result = {"sentiment": "positive", "confidence": 0.87, "text": text[:50]}
    return jsonify(result)

@app.route("/api/v1/info")
def info():
    return jsonify({
        "app":     "Navkiran Intern API",
        "version": config.APP_VERSION,
        "debug":   config.DEBUG,
        "env":     os.environ.get("FLASK_ENV", "production")
    })

print("=" * 60)
print("  PRODUCTION DEPLOYMENT GUIDE")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
PRODUCTION vs DEVELOPMENT:
  Development: app.run(debug=True)  → NOT safe for production
               Shows stack traces, auto-reloads, single thread

  Production: Use GUNICORN (WSGI server)
    pip install gunicorn
    gunicorn -w 4 -b 0.0.0.0:5000 app:app
      -w 4     → 4 worker processes
      -b       → bind to host:port
      app:app  → module:flask_app_variable

ENVIRONMENT VARIABLES (production secrets):
  # In shell:
  export SECRET_KEY="very-long-random-string-here"
  export DATABASE_URL="postgresql://user:pass@host/db"
  export DEBUG="false"

  # Or use .env file with python-dotenv:
  pip install python-dotenv
  from dotenv import load_dotenv
  load_dotenv()

REVERSE PROXY (nginx in front of gunicorn):
  nginx handles:  SSL termination, static files, rate limiting
  gunicorn handles: Python app logic

  nginx.conf snippet:
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
    }

PROCESS MANAGER (systemd or supervisord):
  Keeps gunicorn running after crashes/reboots.

  systemd service file (/etc/systemd/system/myapp.service):
    [Unit]
    Description=Navkiran Flask App

    [Service]
    User=ubuntu
    WorkingDirectory=/home/ubuntu/app
    ExecStart=/home/ubuntu/venv/bin/gunicorn -w 4 app:app
    Restart=always

    [Install]
    WantedBy=multi-user.target

  sudo systemctl start myapp
  sudo systemctl enable myapp   # start on boot
""")

print("=" * 60)
print("SECTION 3: HEALTH CHECK ENDPOINT")
print("=" * 60)
print("""
Every production app needs /health (or /healthz).
Load balancers ping it every 30s — if it fails, traffic is rerouted.

Checklist for health endpoint:
  ✓ Returns HTTP 200 when app is working
  ✓ Returns HTTP 503 if database is unreachable
  ✓ Returns app version and timestamp
  ✓ Fast response (no heavy computation)
""")

print("Running app in demo mode (not starting server):")
with app.test_client() as client:
    r = client.get("/health")
    print(f"  GET /health → {r.status_code}: {r.get_json()}")
    r2 = client.get("/api/v1/info")
    print(f"  GET /api/v1/info → {r2.get_json()}")
    r3 = client.post("/api/v1/predict", json={"text": "This is great!"})
    print(f"  POST /predict → {r3.get_json()}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("gunicorn        → production WSGI server")
print("nginx           → reverse proxy + SSL")
print("systemd         → process manager")
print("os.environ.get  → secrets from environment")
print("/health         → required health check endpoint")
print("logging         → structured log output")
