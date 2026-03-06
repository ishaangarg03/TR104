# =============================================================================
# WEEK 9 - DAY 2: Prompt Engineering
# Intern: ISHAAN GARG
# Topic: Techniques to get better LLM outputs
# =============================================================================

print("=" * 60)
print("  WEEK 9 DAY 2: PROMPT ENGINEERING")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
Prompt Engineering = the skill of writing prompts that get the
best possible output from an LLM.

A well-crafted prompt can be the difference between:
  ❌ A vague, generic answer
  ✅ A specific, accurate, formatted answer
""")

print("=" * 60)
print("TECHNIQUE 1: ZERO-SHOT vs FEW-SHOT")
print("=" * 60)

print("""
ZERO-SHOT: Just ask — no examples given.
  Prompt: "Classify the sentiment: 'This product is amazing!'"
  Output: "Positive"

FEW-SHOT: Give examples to show the pattern.
  Prompt:
    Classify the sentiment. Examples:
    Text: "I love this!" → Positive
    Text: "Terrible quality." → Negative
    Text: "It is okay." → Neutral
    ---
    Text: "Best purchase ever!" → ?

  Output: "Positive"  ← more reliable with examples
""")

print("=" * 60)
print("TECHNIQUE 2: CHAIN-OF-THOUGHT (CoT)")
print("=" * 60)

print("""
For reasoning tasks, ask the model to think step by step.

WITHOUT CoT:
  Q: "If a train travels 120km in 1.5 hours, what is its speed?"
  A: "80 km/h"  ← may be right but may hallucinate

WITH CoT ("Let's think step by step"):
  Q: "If a train travels 120km in 1.5 hours, what is its speed?
      Let's think step by step."
  A: "Step 1: Speed = Distance / Time
      Step 2: Speed = 120 km / 1.5 hours
      Step 3: Speed = 80 km/h
      The train's speed is 80 km/h."

CoT dramatically improves accuracy on math, logic, and reasoning.
""")

print("=" * 60)
print("TECHNIQUE 3: ROLE PROMPTING")
print("=" * 60)

print("""
Assigning a persona to the model shapes its response style.

"You are an expert Python developer with 10 years of experience.
 Review this code and suggest improvements."

vs.

"Review this code."

Role prompts work well for:
  - Expert reviewer / code review
  - Friendly teacher / tutoring
  - Strict editor / writing review
  - Devil's advocate / stress testing ideas
""")

print("=" * 60)
print("TECHNIQUE 4: OUTPUT FORMATTING")
print("=" * 60)

print("""
Always specify the format you want.

BAD: "Tell me about Python."
GOOD: "Explain Python in exactly 3 bullet points, each under 15 words."

GREAT (JSON output):
  "Extract the following info from this text and return ONLY a JSON object:
   {
     'name': string,
     'age': integer,
     'skills': list of strings
   }
   
   Text: 'Ishaan Garg is 21 years old and knows Python, Git, and ML.'"

JSON output is ideal for downstream processing in your code.
""")

def build_extraction_prompt(text, schema):
    """Build a structured extraction prompt."""
    schema_str = "\n".join(f"  {k}: {v}" for k, v in schema.items())
    return f"""Extract information from the text below.
Return ONLY a valid JSON object with these exact keys:
{schema_str}

If a field is not found, use null.
Text: "{text}"
JSON:"""

schema = {"name": "string", "city": "string", "role": "string", "skills": "list of strings"}
text = "Hi, I'm Navkiran from Ludhiana. I work as an AI intern and know Python and ML."
prompt = build_extraction_prompt(text, schema)
print("Built extraction prompt:")
print(prompt)

print("=" * 60)
print("TECHNIQUE 5: PROMPT TEMPLATES")
print("=" * 60)

class PromptTemplate:
    """Reusable prompt template with variable substitution."""

    def __init__(self, template):
        self.template = template

    def format(self, **kwargs):
        result = self.template
        for key, value in kwargs.items():
            result = result.replace(f"{{{key}}}", str(value))
        return result

code_review_template = PromptTemplate("""
You are a senior {language} developer.
Review the following code for:
1. Bugs and errors
2. Performance issues
3. Security concerns
4. Code style and readability

Code to review:
```{language}
{code}
```

Provide specific, actionable feedback. Be concise.
""")

sample_code = """
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return db.execute(query)
"""

prompt = code_review_template.format(language="python", code=sample_code)
print("Code review prompt:")
print(prompt)

print("=" * 60)
print("TECHNIQUE 6: CONSTRAINTS AND GUARDRAILS")
print("=" * 60)

print("""
Always add constraints to control output:

"Answer in exactly 2 sentences."
"Use only information from the provided context. Say 'I don't know' if not in context."
"Do not use technical jargon. Explain as if to a 15-year-old."
"Return ONLY the JSON. No explanation, no markdown, no preamble."
"If the question is unrelated to Python, say 'Out of scope'."
""")

print("=" * 60)
print("TECHNIQUE 7: SELF-CONSISTENCY")
print("=" * 60)

print("""
For important decisions, generate multiple responses and take the majority vote.

answers = []
for _ in range(5):
    response = llm.complete(prompt, temperature=0.8)
    answers.append(response)

# Take majority vote
from collections import Counter
final_answer = Counter(answers).most_common(1)[0][0]

This reduces hallucination for factual questions.
""")

print("=" * 60)
print("SUMMARY — Prompt Engineering Checklist")
print("=" * 60)
print("✓ Use few-shot examples for classification tasks")
print("✓ Add 'step by step' for reasoning/math")
print("✓ Assign a role for expert knowledge")
print("✓ Specify exact output format (JSON, bullets, sentences)")
print("✓ Add constraints (length, scope, style)")
print("✓ Use templates for repeatable prompts")
print("✓ Self-consistency for high-stakes answers")
