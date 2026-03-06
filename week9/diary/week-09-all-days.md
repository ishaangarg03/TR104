# WEEK 9 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — LLM Concepts & APIs

LLMs are everywhere now but understanding the fundamentals — tokens, temperature, context windows, statelessness — makes it much clearer why they work the way they do. The token counting and cost estimation demo made pricing feel concrete. The key insight: always send full conversation history because the model has no memory between calls.

**Ran today:** `day1/llm_concepts.py`

---

## Day 2 — Prompt Engineering

Prompt engineering is genuinely a skill. The same question asked differently can produce completely different quality answers. Few-shot examples, chain-of-thought reasoning, and output formatting constraints are now part of my toolkit. The PromptTemplate class for reusable prompts is something I'll use in every LLM project.

**Ran today:** `day2/prompt_engineering.py`

---

## Day 3 — RAG Pipeline

RAG solves the hallucination problem for factual domains. Building the full pipeline manually — chunking, vectorizing, similarity search, prompt construction — made me understand why it works. TF-IDF as a proxy for real embeddings captured the concept perfectly.

**Ran today:** `day3/rag_pipeline.py`

---

## Day 4 — AI Agents & Tool Use

Agents are where LLMs get truly powerful. The ReAct pattern (Reason → Act → Observe) is elegant. Building a rule-based agent first, then seeing how real LLM APIs handle tool use natively, showed me both the concept and the production implementation path.

**Ran today:** `day4/ai_agents.py`

---

## Day 5 — Week 9 Final Project: AI Study Chatbot

Built a full conversational assistant combining RAG (TF-IDF retrieval over a 12-doc knowledge base), tools (calculator, clock), quiz mode, session stats, and conversation history — all without any LLM API key. This is a solid prototype that could be upgraded to use a real LLM API in production.

**Ran today:** `day5/week9_final_project.py`
