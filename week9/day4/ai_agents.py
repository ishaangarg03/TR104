# =============================================================================
# WEEK 9 - DAY 4: AI Agents & Tool Use
# Intern: ISHAAN GARG
# Topic: Build a simple ReAct agent with tools
# =============================================================================

import json
import math
import re
from datetime import datetime

print("=" * 60)
print("  WEEK 9 DAY 4: AI AGENTS & TOOL USE")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
WHAT IS AN AI AGENT?
  An LLM that can:
    1. Plan what steps to take
    2. Use tools (functions, APIs, code)
    3. Observe results
    4. Repeat until task is done

  LLM alone: text in → text out
  Agent:     text in → think → use tools → think → answer

REACT PATTERN (Reason + Act):
  Thought: I need to find the current weather in Delhi
  Action: search_weather("Delhi")
  Observation: 28°C, partly cloudy
  Thought: Now I can answer the question
  Answer: The weather in Delhi is 28°C and partly cloudy.
""")

print("=" * 60)
print("SECTION 1: DEFINE TOOLS")
print("=" * 60)

# Tools are just Python functions the agent can call
def calculator(expression: str) -> str:
    """Evaluate a math expression safely."""
    try:
        allowed = set("0123456789+-*/().% ")
        if not all(c in allowed for c in expression):
            return f"Error: Invalid characters in expression"
        result = eval(expression)
        return f"{result}"
    except Exception as e:
        return f"Error: {str(e)}"

def word_count(text: str) -> str:
    """Count words in text."""
    words = text.split()
    chars = len(text)
    return f"Words: {len(words)}, Characters: {chars}"

def search_knowledge(query: str) -> str:
    """Simple knowledge lookup (simulates RAG)."""
    knowledge = {
        "python": "Python is a high-level, interpreted programming language known for readability.",
        "ml": "Machine learning is a subset of AI where models learn patterns from data.",
        "flask": "Flask is a lightweight Python web framework for building APIs and web apps.",
        "docker": "Docker is a containerization platform that packages apps and their dependencies.",
        "git": "Git is a version control system for tracking code changes.",
    }
    query_lower = query.lower()
    for key, value in knowledge.items():
        if key in query_lower:
            return value
    return "No information found for that query."

def get_current_time() -> str:
    """Return current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def unit_converter(value: float, from_unit: str, to_unit: str) -> str:
    """Convert between common units."""
    conversions = {
        ("km", "miles"): lambda x: x * 0.621371,
        ("miles", "km"): lambda x: x * 1.60934,
        ("kg", "lbs"):   lambda x: x * 2.20462,
        ("lbs", "kg"):   lambda x: x / 2.20462,
        ("c", "f"):      lambda x: x * 9/5 + 32,
        ("f", "c"):      lambda x: (x - 32) * 5/9,
        ("m", "ft"):     lambda x: x * 3.28084,
        ("ft", "m"):     lambda x: x / 3.28084,
    }
    key = (from_unit.lower(), to_unit.lower())
    if key in conversions:
        result = conversions[key](value)
        return f"{value} {from_unit} = {result:.4f} {to_unit}"
    return f"Conversion from {from_unit} to {to_unit} not supported."

TOOLS = {
    "calculator":       calculator,
    "word_count":       word_count,
    "search_knowledge": search_knowledge,
    "get_current_time": get_current_time,
    "unit_converter":   unit_converter,
}

print("Available tools:")
for name, func in TOOLS.items():
    print(f"  {name:20s} → {func.__doc__}")

print("\n" + "=" * 60)
print("SECTION 2: SIMPLE RULE-BASED AGENT")
print("=" * 60)

class SimpleAgent:
    """
    A rule-based agent that decides which tool to use
    based on keywords in the query.
    (In production, an LLM decides which tool to call.)
    """

    def __init__(self, tools):
        self.tools = tools
        self.history = []

    def log(self, step_type, content):
        entry = {"step": step_type, "content": content}
        self.history.append(entry)
        print(f"  [{step_type.upper()}] {content}")

    def run(self, query):
        print(f"\n{'─' * 55}")
        print(f"  QUERY: {query}")
        print(f"{'─' * 55}")
        self.history = []

        self.log("thought", f"Analyzing query: '{query}'")

        # Decide which tool to use
        q = query.lower()

        if any(w in q for w in ["calculate", "what is", "+", "-", "*", "/"]):
            expr = re.findall(r"[\d\+\-\*\/\.\(\)\s]+", query)
            if expr:
                expr_str = expr[0].strip()
                self.log("action", f"calculator('{expr_str}')")
                result = self.tools["calculator"](expr_str)
                self.log("observation", f"Result = {result}")
                return f"The answer is: {result}"

        if any(w in q for w in ["convert", "km", "miles", "kg", "celsius", "fahrenheit"]):
            nums = re.findall(r"\d+\.?\d*", query)
            if nums:
                val = float(nums[0])
                if "km" in q and "miles" in q:
                    self.log("action", f"unit_converter({val}, 'km', 'miles')")
                    result = self.tools["unit_converter"](val, "km", "miles")
                elif "celsius" in q or "°c" in q:
                    self.log("action", f"unit_converter({val}, 'c', 'f')")
                    result = self.tools["unit_converter"](val, "c", "f")
                elif "kg" in q and "lbs" in q:
                    self.log("action", f"unit_converter({val}, 'kg', 'lbs')")
                    result = self.tools["unit_converter"](val, "kg", "lbs")
                else:
                    result = "Could not determine conversion type."
                self.log("observation", result)
                return result

        if any(w in q for w in ["time", "date", "now", "today"]):
            self.log("action", "get_current_time()")
            result = self.tools["get_current_time"]()
            self.log("observation", result)
            return f"Current date and time: {result}"

        if any(w in q for w in ["count", "words", "characters", "length"]):
            text_match = re.search(r"['\"](.+)['\"]", query)
            if text_match:
                text = text_match.group(1)
                self.log("action", f"word_count('{text[:30]}...')")
                result = self.tools["word_count"](text)
                self.log("observation", result)
                return result

        if any(w in q for w in ["what is", "explain", "tell me about", "define"]):
            self.log("action", f"search_knowledge('{query[:40]}')")
            result = self.tools["search_knowledge"](query)
            self.log("observation", result)
            return result

        return "I don't know how to handle that query yet."

agent = SimpleAgent(TOOLS)

test_queries = [
    "Calculate 25 * 48 + 100",
    "What time is it now?",
    "Convert 100 km to miles",
    "Convert 30 celsius to fahrenheit",
    "What is Python?",
    "What is machine learning?",
    "Convert 75 kg to lbs",
]

for query in test_queries:
    answer = agent.run(query)
    print(f"  FINAL ANSWER: {answer}\n")

print("=" * 60)
print("SECTION 3: TOOL USE IN REAL LLM APIS")
print("=" * 60)

print("""
Real LLM APIs support function calling natively.
The model decides when and how to call tools.

ANTHROPIC TOOL USE:

  tools = [
    {
      "name": "calculator",
      "description": "Evaluates a math expression",
      "input_schema": {
        "type": "object",
        "properties": {
          "expression": {"type": "string", "description": "Math expression"}
        },
        "required": ["expression"]
      }
    }
  ]

  response = client.messages.create(
      model="claude-opus-4-6",
      tools=tools,
      messages=[{"role": "user", "content": "What is 128 * 256?"}]
  )

  # If model wants to call a tool:
  if response.stop_reason == "tool_use":
      tool_call = response.content[0]
      tool_name = tool_call.name
      tool_input = tool_call.input
      result = your_function(tool_input["expression"])
      # Send result back to model for final answer
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("Agent = LLM + tools + loop (plan → act → observe)")
print("ReAct = Thought → Action → Observation pattern")
print("Tools = any Python function the model can call")
print("Tool use = LLM tells you WHICH function + WHAT args")
print("You execute the function and return result to LLM")
