# WEEK 8 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — Docker & Containerization

Docker solves the "works on my machine" problem elegantly. A Dockerfile is just a recipe: start from a base image, copy your code, install dependencies, expose a port, run the app. The layered caching (copying requirements.txt before the code) means rebuilds are fast unless dependencies change.

**Ran today:** `day1/docker_concepts.py`

---

## Day 2 — Production Deployment

Development Flask with `debug=True` is NOT safe for production. Today I learned about Gunicorn (the production WSGI server), nginx as a reverse proxy, and systemd to keep the process alive after reboots. The health check endpoint is something I'll always include now — load balancers need it.

**Ran today:** `day2/production_deployment.py`

---

## Day 3 — Testing & CI/CD

Writing tests before thinking about CI/CD made me realize how important tests are. When all 10 unit tests pass, you can deploy with confidence. GitHub Actions running tests automatically on every push is how professional teams prevent regressions.

**Ran today:** `day3/testing_cicd.py`

---

## Day 4 — Cloud Services

AWS has a service for everything. The mental model that clicked for me: EC2 = renting a computer, S3 = renting unlimited storage, Lambda = renting a function (no computer needed). IAM is the security layer tying everything together. The boto3 SDK makes all of this scriptable from Python.

**Ran today:** `day4/cloud_services.py`

---

## Day 5 — Week 8 Final Project: Production ML API

Built a complete production-grade sentiment API with health check, batch endpoint, input validation, logging, and a full test suite — all in one file. Added a Dockerfile for containerization. This is what a real ML microservice looks like.

**Ran today:** `day5/week8_final_project.py`
