# =============================================================================
# WEEK 10 - DAY 4: Message Queues & Async Task Processing
# Intern: ISHAAN GARG
# Topic: Decouple services with queues, background workers
# =============================================================================

import threading
import queue
import time
import json
import uuid
from datetime import datetime
from enum import Enum

print("=" * 60)
print("  WEEK 10 DAY 4: MESSAGE QUEUES")
print("  Intern: ISHAAN GARG")
print("=" * 60)

class TaskStatus(Enum):
    PENDING    = "pending"
    PROCESSING = "processing"
    DONE       = "done"
    FAILED     = "failed"

class Task:
    def __init__(self, task_type, payload):
        self.id         = str(uuid.uuid4())[:8]
        self.task_type  = task_type
        self.payload    = payload
        self.status     = TaskStatus.PENDING
        self.result     = None
        self.created_at = datetime.now().isoformat()
        self.done_at    = None

    def to_dict(self):
        return {"id": self.id, "type": self.task_type,
                "status": self.status.value, "result": self.result}

print("=" * 60)
print("SECTION 1: SIMPLE IN-MEMORY QUEUE")
print("=" * 60)

task_queue   = queue.Queue()
task_results = {}

def process_email(payload):
    time.sleep(0.2)
    return f"Email sent to {payload['to']} with subject '{payload['subject']}'"

def process_report(payload):
    time.sleep(0.5)
    rows = payload.get("rows", 100)
    return f"Report '{payload['name']}' generated ({rows} rows)"

def process_ml_inference(payload):
    time.sleep(0.3)
    text = payload.get("text", "")
    sentiment = "positive" if any(w in text.lower() for w in ["good","great","love","amazing"]) else "negative"
    return f"Sentiment: {sentiment} | Text: {text[:30]}"

PROCESSORS = {
    "email":        process_email,
    "report":       process_report,
    "ml_inference": process_ml_inference,
}

def worker(worker_id):
    """Background worker that processes tasks from the queue."""
    print(f"  Worker {worker_id} started")
    while True:
        try:
            task = task_queue.get(timeout=3)
            if task is None:  # poison pill to stop worker
                break
            task.status = TaskStatus.PROCESSING
            print(f"  [Worker {worker_id}] Processing task {task.id} ({task.task_type})")
            processor = PROCESSORS.get(task.task_type)
            if processor:
                task.result = processor(task.payload)
                task.status = TaskStatus.DONE
            else:
                task.result = f"Unknown task type: {task.task_type}"
                task.status = TaskStatus.FAILED
            task.done_at = datetime.now().isoformat()
            task_results[task.id] = task
            print(f"  [Worker {worker_id}] Done task {task.id}: {str(task.result)[:50]}")
            task_queue.task_done()
        except queue.Empty:
            break

# Start workers
NUM_WORKERS = 3
workers = [threading.Thread(target=worker, args=(i+1,), daemon=True)
           for i in range(NUM_WORKERS)]
for w in workers: w.start()

# Submit tasks
tasks_submitted = []

def submit_task(task_type, payload):
    task = Task(task_type, payload)
    task_results[task.id] = task
    task_queue.put(task)
    print(f"  Submitted task {task.id} ({task_type})")
    return task.id

print("\nSubmitting tasks:")
ids = [
    submit_task("email",        {"to": "nav@mail.com", "subject": "Welcome to Week 10!"}),
    submit_task("report",       {"name": "Monthly Sales", "rows": 500}),
    submit_task("ml_inference", {"text": "This product is absolutely amazing!"}),
    submit_task("email",        {"to": "alice@mail.com", "subject": "Your task is done"}),
    submit_task("ml_inference", {"text": "Very disappointing experience."}),
    submit_task("report",       {"name": "User Analytics", "rows": 1200}),
]

task_queue.join()  # wait for all tasks to complete

print("\nResults:")
for task_id in ids:
    task = task_results[task_id]
    print(f"  [{task.status.value:10s}] {task.id} — {str(task.result)[:60]}")

# Stop workers
for _ in workers: task_queue.put(None)
for w in workers: w.join()

print("\n" + "=" * 60)
print("SECTION 2: PRIORITY QUEUE")
print("=" * 60)

pq = queue.PriorityQueue()
pq.put((3, "Low priority task"))
pq.put((1, "URGENT task"))
pq.put((2, "Medium priority task"))
pq.put((1, "Another urgent task"))

print("Processing by priority:")
while not pq.empty():
    priority, task = pq.get()
    print(f"  Priority {priority}: {task}")

print("\n" + "=" * 60)
print("SECTION 3: REAL QUEUE SYSTEMS")
print("=" * 60)

print("""
RabbitMQ (AMQP):
  pip install pika
  import pika

  # Producer
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  channel.queue_declare(queue='tasks')
  channel.basic_publish(exchange='', routing_key='tasks',
                        body=json.dumps({"type": "email", "to": "nav@mail.com"}))

  # Consumer (worker)
  def callback(ch, method, properties, body):
      task = json.loads(body)
      process_task(task)

  channel.basic_consume(queue='tasks', on_message_callback=callback, auto_ack=True)
  channel.start_consuming()

AWS SQS:
  import boto3
  sqs = boto3.client('sqs')

  # Send
  sqs.send_message(QueueUrl='https://sqs...', MessageBody=json.dumps(task))

  # Receive
  msgs = sqs.receive_message(QueueUrl='...', MaxNumberOfMessages=10)
  for msg in msgs['Messages']:
      process(json.loads(msg['Body']))
      sqs.delete_message(QueueUrl='...', ReceiptHandle=msg['ReceiptHandle'])

Celery + Redis (most popular for Python):
  pip install celery redis

  # tasks.py
  from celery import Celery
  app = Celery('tasks', broker='redis://localhost:6379/0')

  @app.task
  def send_email(to, subject):
      # ... send email logic
      return f"Sent to {to}"

  # Submit task (returns immediately)
  result = send_email.delay("nav@mail.com", "Hello")
  print(result.id)  # task ID

  # Check later
  print(result.get(timeout=10))  # wait for result
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("Message queue  → decouple producer from consumer")
print("Worker         → background process that consumes tasks")
print("Priority queue → process urgent tasks first")
print("Celery+Redis   → most popular Python task queue")
print("RabbitMQ/SQS   → production message brokers")
print("Poison pill    → None signal to stop a worker thread")
