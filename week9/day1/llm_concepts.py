# =============================================================================
# WEEK 9 - DAY 1: Large Language Models (LLMs) — Concepts & APIs
# Intern: ISHAAN GARG
# Topic: What are LLMs, tokens, context, calling LLM APIs
# =============================================================================

print("=" * 60)
print("  WEEK 9 — LARGE LANGUAGE MODELS & PROMPT ENGINEERING")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
WHAT IS AN LLM?
  A Large Language Model is a neural network trained on massive text.
  It learns to predict the next token given previous tokens.
  
  Examples:
    GPT-4, Claude, Gemini, Llama, Mistral

KEY CONCEPTS:

  Token:
    Basic unit of text. Roughly 0.75 words (English).
    "Hello world" = 2 tokens
    "Navkiran" = ~3 tokens
    1000 tokens ≈ 750 words

  Context Window:
    Max tokens the model can "see" at once.
    GPT-4: 128K tokens  |  Claude 3: 200K tokens

  Temperature:
    Controls randomness of output.
    0.0 = deterministic (same answer always)
    0.7 = balanced (good for most tasks)
    1.0+ = creative, unpredictable

  System Prompt:
    Instructions that define the model's behavior.
    Set before the conversation starts.

  Completion:
    The model's response to your input (prompt).

  Fine-tuning:
    Training an LLM further on your own dataset.
    Expensive but gives domain-specific knowledge.

  RAG (Retrieval Augmented Generation):
    Give the LLM relevant documents at query time.
    Cheaper than fine-tuning for factual tasks.
""")

print("=" * 60)
print("SECTION 2: CALLING LLM APIS")
print("=" * 60)

print("""
ANTHROPIC CLAUDE API:

  pip install anthropic

  import anthropic
  client = anthropic.Anthropic(api_key="your-key")

  message = client.messages.create(
      model="claude-opus-4-6",
      max_tokens=1024,
      system="You are a helpful Python tutor.",
      messages=[
          {"role": "user", "content": "Explain list comprehensions."}
      ]
  )
  print(message.content[0].text)

OPENAI API:

  pip install openai

  from openai import OpenAI
  client = OpenAI(api_key="your-key")

  response = client.chat.completions.create(
      model="gpt-4",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user",   "content": "What is a neural network?"}
      ],
      temperature=0.7,
      max_tokens=500
  )
  print(response.choices[0].message.content)

GOOGLE GEMINI API:

  pip install google-generativeai

  import google.generativeai as genai
  genai.configure(api_key="your-key")
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content("Explain Python decorators.")
  print(response.text)
""")

print("=" * 60)
print("SECTION 3: TOKEN COUNTING SIMULATION")
print("=" * 60)

def estimate_tokens(text):
    """Rough estimate: 1 token ≈ 4 chars for English."""
    return max(1, len(text) // 4)

def estimate_cost(prompt_tokens, completion_tokens, model="gpt-4"):
    """Estimate API cost in USD."""
    pricing = {
        "gpt-4":         (0.03,  0.06),     # per 1K tokens input/output
        "gpt-3.5-turbo": (0.001, 0.002),
        "claude-3-opus": (0.015, 0.075),
        "claude-3-sonnet":(0.003, 0.015),
    }
    in_price, out_price = pricing.get(model, (0.01, 0.03))
    return round((prompt_tokens * in_price + completion_tokens * out_price) / 1000, 6)

prompts = [
    "What is Python?",
    "Write a 500-word essay about machine learning applications in healthcare.",
    "Explain the difference between supervised and unsupervised learning with examples.",
]

print(f"\n{'Prompt (truncated)':50s} | {'~Tokens':>8} | {'~Cost (GPT-4)'}")
print("-" * 75)
for p in prompts:
    tokens = estimate_tokens(p)
    cost = estimate_cost(tokens, tokens * 3)  # assume 3x output
    print(f"  {p[:48]:48s} | {tokens:>8} | ${cost:.6f}")

print("""
COST TIPS:
  • Use GPT-3.5 or Claude Haiku for simple tasks (10-50x cheaper)
  • Cache repeated prompts
  • Truncate context — only send relevant info
  • Set max_tokens to limit response length
  • Use streaming to show response progressively
""")

print("=" * 60)
print("SECTION 4: MULTI-TURN CONVERSATIONS")
print("=" * 60)

print("""
LLMs are stateless — they don't remember previous calls.
YOU must send the full conversation history every time.

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Python tutor."},
            *conversation_history          # send full history
        ]
    )
    
    assistant_reply = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply
    })
    return assistant_reply

reply1 = chat("What is a decorator?")
reply2 = chat("Can you give me an example?")  # model remembers context
reply3 = chat("How is that different from a wrapper?")
""")

print("=" * 60)
print("SUMMARY — LLM Key Terms")
print("=" * 60)
print("Token          → basic text unit (~0.75 words)")
print("Temperature    → randomness (0=deterministic, 1=creative)")
print("System prompt  → persistent instructions for the model")
print("Context window → max tokens model can process at once")
print("RAG            → give model documents at query time")
print("Fine-tuning    → train model on your data")
print("Stateless      → always send full conversation history")
