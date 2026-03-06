# =============================================================================
# WEEK 9 - DAY 3: RAG — Retrieval Augmented Generation
# Intern: ISHAAN GARG
# Topic: Build a simple RAG pipeline from scratch with embeddings
# =============================================================================

# pip install numpy scikit-learn

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

print("=" * 60)
print("  WEEK 9 DAY 3: RAG PIPELINE")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
WHY RAG?
  LLMs have a knowledge cutoff date and limited context.
  RAG = give the model relevant documents at query time.

  Traditional:  User Query → LLM → Answer (from training only)
  RAG:          User Query → Retrieve Docs → LLM + Docs → Answer

STEPS IN A RAG PIPELINE:
  1. INDEXING (done once):
     a. Collect documents
     b. Split into chunks
     c. Embed each chunk → vector
     d. Store in vector database

  2. QUERYING (done per request):
     a. Embed the user query
     b. Find most similar chunks (vector search)
     c. Build prompt: question + retrieved chunks
     d. Send to LLM → get answer
""")

print("=" * 60)
print("SECTION 1: KNOWLEDGE BASE")
print("=" * 60)

knowledge_base = [
    {
        "id": 1,
        "title": "Python Data Types",
        "content": "Python has several built-in data types: integers (int), "
                   "floating-point numbers (float), strings (str), booleans (bool), "
                   "lists, tuples, dictionaries, and sets. Each serves different purposes."
    },
    {
        "id": 2,
        "title": "List vs Tuple",
        "content": "Lists are mutable (changeable) ordered collections using square brackets. "
                   "Tuples are immutable (unchangeable) ordered collections using parentheses. "
                   "Use lists when data changes, tuples for fixed data like coordinates."
    },
    {
        "id": 3,
        "title": "Python Functions",
        "content": "Functions in Python are defined with the def keyword. They accept parameters, "
                   "can have default values, return values with return. *args accepts variable "
                   "positional arguments, **kwargs accepts variable keyword arguments."
    },
    {
        "id": 4,
        "title": "Machine Learning Overview",
        "content": "Machine learning is a subset of AI where models learn patterns from data. "
                   "Supervised learning uses labeled data. Unsupervised learning finds patterns "
                   "without labels. The main steps are: collect data, preprocess, train model, evaluate."
    },
    {
        "id": 5,
        "title": "Neural Networks",
        "content": "Neural networks consist of layers: input, hidden, and output. Each neuron "
                   "applies weights, biases, and an activation function. Training uses backpropagation "
                   "to minimize loss. Common activations: ReLU for hidden layers, sigmoid for binary output."
    },
    {
        "id": 6,
        "title": "Git Version Control",
        "content": "Git tracks changes in code. Key commands: git init to start, git add to stage, "
                   "git commit to save, git push to upload, git pull to download. Branches allow "
                   "parallel development without affecting the main codebase."
    },
    {
        "id": 7,
        "title": "REST APIs",
        "content": "REST APIs use HTTP methods: GET (read), POST (create), PUT (update), DELETE (remove). "
                   "They return JSON data. Status codes: 200 OK, 201 Created, 400 Bad Request, "
                   "404 Not Found, 500 Server Error."
    },
    {
        "id": 8,
        "title": "Docker Containers",
        "content": "Docker packages apps and dependencies into containers. A Dockerfile defines the image. "
                   "docker build creates an image, docker run starts a container. Containers are isolated, "
                   "lightweight, and run identically on any machine."
    },
]

print(f"Knowledge base: {len(knowledge_base)} documents")
for doc in knowledge_base:
    print(f"  [{doc['id']}] {doc['title']}")

print("\n" + "=" * 60)
print("SECTION 2: DOCUMENT CHUNKING")
print("=" * 60)

def chunk_text(text, chunk_size=100, overlap=20):
    """Split text into overlapping chunks (word-based)."""
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

# For this example each doc is already small enough as one chunk
chunks = []
for doc in knowledge_base:
    doc_chunks = chunk_text(doc["content"], chunk_size=50)
    for j, chunk in enumerate(doc_chunks):
        chunks.append({"doc_id": doc["id"], "title": doc["title"],
                        "chunk_id": f"{doc['id']}_{j}", "text": chunk})

print(f"Total chunks after splitting: {len(chunks)}")

print("\n" + "=" * 60)
print("SECTION 3: BUILD VECTOR INDEX (TF-IDF as proxy for embeddings)")
print("=" * 60)

print("""
Real RAG uses dense embeddings (e.g., OpenAI text-embedding-ada-002,
sentence-transformers, Cohere). Here we use TF-IDF as a simple proxy
that demonstrates the same retrieval concept.
""")

corpus = [c["text"] for c in chunks]
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
chunk_vectors = vectorizer.fit_transform(corpus)
print(f"Indexed {len(corpus)} chunks as {chunk_vectors.shape[1]}-dim vectors")

print("\n" + "=" * 60)
print("SECTION 4: RETRIEVAL")
print("=" * 60)

def retrieve(query, top_k=3):
    """Find top-k most relevant chunks for a query."""
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, chunk_vectors).flatten()
    top_indices = scores.argsort()[-top_k:][::-1]
    results = []
    for idx in top_indices:
        if scores[idx] > 0:
            results.append({
                "chunk":  chunks[idx],
                "score":  round(float(scores[idx]), 4)
            })
    return results

test_queries = [
    "What is the difference between a list and a tuple?",
    "How do I use git to commit code?",
    "What is a neural network?",
    "How do Docker containers work?",
    "What HTTP methods do REST APIs use?",
]

for query in test_queries:
    results = retrieve(query, top_k=2)
    print(f"\nQuery: '{query}'")
    for r in results:
        print(f"  [{r['score']:.3f}] {r['chunk']['title']}: {r['chunk']['text'][:80]}...")

print("\n" + "=" * 60)
print("SECTION 5: AUGMENTED GENERATION (PROMPT BUILDING)")
print("=" * 60)

def build_rag_prompt(question, retrieved_chunks):
    """Build a RAG prompt from question + retrieved context."""
    context = "\n\n".join(
        f"[Source: {c['chunk']['title']}]\n{c['chunk']['text']}"
        for c in retrieved_chunks
    )
    return f"""Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't have that information."

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""

question = "What is the difference between a list and a tuple in Python?"
retrieved = retrieve(question, top_k=3)
prompt = build_rag_prompt(question, retrieved)
print("Built RAG prompt:")
print(prompt)

print("\nIn a real system, this prompt gets sent to an LLM API.")
print("The LLM answers ONLY from the provided context, preventing hallucination.")

print("\n" + "=" * 60)
print("SECTION 6: VECTOR DATABASES")
print("=" * 60)

print("""
Production RAG uses vector databases for fast similarity search
at scale (millions of documents).

Popular vector databases:
  Pinecone    → fully managed, easy to start
  Weaviate    → open-source, self-hostable
  Qdrant      → open-source, fast, Rust-based
  ChromaDB    → simple, great for prototyping
  pgvector    → PostgreSQL extension (vectors in SQL)
  FAISS       → Facebook's in-memory library

Basic ChromaDB usage:
  import chromadb
  client = chromadb.Client()
  collection = client.create_collection("my_docs")

  collection.add(
      documents=["text1", "text2"],
      ids=["id1", "id2"]
  )

  results = collection.query(
      query_texts=["search query"],
      n_results=3
  )
""")

print("=" * 60)
print("SUMMARY — RAG Pipeline")
print("=" * 60)
print("1. Collect and chunk documents")
print("2. Embed chunks → vectors → store in vector DB")
print("3. User query → embed → similarity search → top-k chunks")
print("4. Build prompt: question + retrieved context")
print("5. Send to LLM → grounded, factual answer")
