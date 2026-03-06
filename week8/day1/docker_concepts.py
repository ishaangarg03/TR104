# =============================================================================
# WEEK 8 - DAY 1: Docker & Containerization Concepts
# Intern: ISHAAN GARG
# Topic: What is Docker, containers vs VMs, writing a Dockerfile
# =============================================================================

print("=" * 60)
print("  WEEK 8 — DOCKER & DEPLOYMENT")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
WHY DOCKER?

The classic problem: "It works on my machine!" 
Docker solves this by packaging your app + ALL its
dependencies into a container that runs identically
everywhere — your laptop, a server, or the cloud.

CONTAINER vs VIRTUAL MACHINE:
  VM:        full OS copy       → heavy (GBs), slow to start
  Container: shares host OS     → lightweight (MBs), starts in seconds

KEY DOCKER CONCEPTS:
  Image      → blueprint (read-only template)
  Container  → running instance of an image
  Dockerfile → instructions to build an image
  Registry   → storage for images (Docker Hub)
  Volume     → persistent storage for containers
  Network    → how containers communicate
""")

print("=" * 60)
print("SECTION 2: DOCKERFILE EXPLAINED")
print("=" * 60)

dockerfile = '''
# ---- Dockerfile for a Flask API ----
# Start from official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (layer caching optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
'''
print("Sample Dockerfile:")
print(dockerfile)

print("=" * 60)
print("SECTION 3: REQUIREMENTS.TXT")
print("=" * 60)

requirements = """flask==3.0.0
requests==2.31.0
pandas==2.1.0
numpy==1.26.0
gunicorn==21.2.0
"""
print("requirements.txt:")
print(requirements)

print("=" * 60)
print("SECTION 4: COMMON DOCKER COMMANDS")
print("=" * 60)

commands = [
    ("docker build -t myapp .",          "Build image from Dockerfile"),
    ("docker run -p 5000:5000 myapp",    "Run container, map port 5000"),
    ("docker run -d myapp",              "Run in detached (background) mode"),
    ("docker ps",                        "List running containers"),
    ("docker ps -a",                     "List ALL containers"),
    ("docker stop <container_id>",       "Stop a container"),
    ("docker rm <container_id>",         "Remove a container"),
    ("docker images",                    "List all images"),
    ("docker rmi <image_id>",            "Remove an image"),
    ("docker logs <container_id>",       "View container logs"),
    ("docker exec -it <id> bash",        "Open shell inside container"),
    ("docker pull python:3.11-slim",     "Pull image from Docker Hub"),
    ("docker push myuser/myapp:latest",  "Push to Docker Hub"),
]

print(f"{'Command':45s} | Description")
print("-" * 75)
for cmd, desc in commands:
    print(f"  {cmd:43s} | {desc}")

print("\n" + "=" * 60)
print("SECTION 5: DOCKER-COMPOSE FOR MULTI-CONTAINER APPS")
print("=" * 60)

compose = """
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
    volumes:
      - ./logs:/app/logs      # persist logs

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
"""
print("docker-compose.yml for Flask + PostgreSQL:")
print(compose)

print("Commands:")
print("  docker-compose up        → start all services")
print("  docker-compose up -d     → start in background")
print("  docker-compose down      → stop and remove containers")
print("  docker-compose logs web  → logs for web service")

print("\n" + "=" * 60)
print("SECTION 6: .DOCKERIGNORE")
print("=" * 60)
dockerignore = """
# .dockerignore — like .gitignore but for Docker
__pycache__/
*.pyc
*.pyo
.env
.git
venv/
*.log
tests/
"""
print(dockerignore)

print("=" * 60)
print("SUMMARY — Docker Workflow")
print("=" * 60)
print("1. Write Dockerfile")
print("2. docker build -t myapp .")
print("3. docker run -p 5000:5000 myapp")
print("4. Push to Docker Hub / deploy to cloud")
print("5. Use docker-compose for multi-service apps")
