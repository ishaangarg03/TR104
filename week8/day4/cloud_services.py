# =============================================================================
# WEEK 8 - DAY 4: Cloud Services — AWS/GCP/Azure Concepts
# Intern: ISHAAN GARG
# Topic: Cloud architecture, key services, boto3 AWS SDK basics
# =============================================================================

print("=" * 60)
print("  WEEK 8 DAY 4: CLOUD SERVICES")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
WHAT IS CLOUD COMPUTING?
  Rent computing resources (servers, storage, databases)
  instead of buying and maintaining physical hardware.

  Pay-as-you-go → no upfront hardware cost
  Scalable      → scale up in minutes
  Global        → deploy close to users worldwide
  Managed       → provider handles hardware, security patches

THREE MAJOR PROVIDERS:
  AWS   (Amazon Web Services)  → market leader, most services
  GCP   (Google Cloud Platform) → best ML/data tools
  Azure (Microsoft)             → best for enterprise/.NET
""")

print("=" * 60)
print("KEY AWS SERVICES (most important to know)")
print("=" * 60)

services = [
    ("EC2",              "Virtual machines (servers)"),
    ("S3",               "Object storage (files, images, data)"),
    ("RDS",              "Managed relational databases (MySQL, Postgres)"),
    ("Lambda",           "Serverless functions (run code without a server)"),
    ("API Gateway",      "Managed HTTP API endpoints"),
    ("ECS/EKS",          "Run Docker containers at scale"),
    ("CloudWatch",       "Monitoring, logs, alerts"),
    ("IAM",              "Identity & access management"),
    ("SQS",              "Message queue (async communication)"),
    ("Elastic Beanstalk","Easy web app deployment"),
    ("SageMaker",        "Managed ML training & deployment"),
    ("DynamoDB",         "Managed NoSQL database"),
]

print(f"{'Service':20s} | Description")
print("-" * 60)
for svc, desc in services:
    print(f"  {svc:18s} | {desc}")

print("\n" + "=" * 60)
print("BOTO3 — AWS SDK FOR PYTHON (Simulated Demo)")
print("=" * 60)
print("""
# pip install boto3

import boto3

# Configure credentials (use IAM roles in production, never hardcode)
# aws configure  →  enter Access Key, Secret, Region

# S3 — Upload a file
s3 = boto3.client('s3')
s3.upload_file('data.csv', 'my-bucket', 'uploads/data.csv')
print("File uploaded to S3")

# S3 — Download a file
s3.download_file('my-bucket', 'uploads/data.csv', 'local_data.csv')

# S3 — List files in bucket
response = s3.list_objects_v2(Bucket='my-bucket', Prefix='uploads/')
for obj in response.get('Contents', []):
    print(obj['Key'], obj['Size'])

# Lambda — Invoke a function
lambda_client = boto3.client('lambda')
response = lambda_client.invoke(
    FunctionName='my-ml-function',
    Payload=json.dumps({"text": "Analyze this!"}),
)
result = json.loads(response['Payload'].read())
print(result)

# DynamoDB — Put an item
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('students')
table.put_item(Item={'id': '1', 'name': 'Navkiran', 'score': 88})

# Read an item
response = table.get_item(Key={'id': '1'})
print(response['Item'])
""")

print("=" * 60)
print("SERVERLESS ARCHITECTURE — AWS LAMBDA")
print("=" * 60)
print("""
Lambda function handler:

  def lambda_handler(event, context):
      '''
      event   → input data (from API Gateway, S3 trigger, etc.)
      context → runtime info (function name, timeout, etc.)
      '''
      text = event.get('text', '')

      # Your logic here
      sentiment = analyze_sentiment(text)

      return {
          'statusCode': 200,
          'body': json.dumps({'sentiment': sentiment})
      }

Use cases:
  • API backend (triggered by API Gateway)
  • File processing (triggered when file uploaded to S3)
  • Scheduled tasks (triggered by CloudWatch Events)
  • Real-time stream processing (triggered by SQS/Kinesis)

Benefits:
  • No server to manage
  • Auto-scales from 0 to millions of requests
  • Pay only per invocation (very cheap for low traffic)
""")

print("=" * 60)
print("DEPLOYMENT ARCHITECTURE — TYPICAL WEB APP")
print("=" * 60)
print("""
User Request
     ↓
Route 53 (DNS)
     ↓
CloudFront (CDN) ← static assets (JS, CSS, images)
     ↓
API Gateway (HTTPS endpoint)
     ↓
ECS/Lambda (Flask/FastAPI app in container)
     ↓
RDS PostgreSQL ←→ ElastiCache Redis (caching)
     ↓
S3 (file storage)
     ↓
CloudWatch (logs + alerts) → SNS (email/SMS alerts)
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("S3        → store any file at any scale")
print("EC2       → virtual machine (like renting a computer)")
print("Lambda    → serverless function, no server management")
print("RDS       → managed database")
print("IAM       → control WHO can access WHAT")
print("boto3     → Python SDK to talk to AWS services")
