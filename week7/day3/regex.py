# =============================================================================
# WEEK 7 - DAY 3: Regular Expressions (Regex)
# Intern: ISHAAN GARG
# Topic: Pattern matching for text extraction and validation
# =============================================================================

import re

print("=" * 55)
print("SECTION 1: REGEX BASICS")
print("=" * 55)
print("""
Regex = patterns to match text.
Key symbols:
  .     → any single character
  *     → 0 or more of previous
  +     → 1 or more of previous
  ?     → 0 or 1 of previous
  ^     → start of string
  $     → end of string
  []    → character class  [a-z] [0-9]
  \\d    → digit (0-9)
  \\w    → word char (a-z, A-Z, 0-9, _)
  \\s    → whitespace
  {n,m} → between n and m repetitions
  ()    → capture group
""")

text = "Navkiran's email is navkiran@techcorp.com and her phone is +91-9876543210"
print("Text:", text)

email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w{2,}", text)
print(f"\nEmail found: {email_match.group()}")

phone_match = re.search(r"\+\d{2}-\d{10}", text)
print(f"Phone found: {phone_match.group()}")

print("\n" + "=" * 55)
print("SECTION 2: FIND ALL MATCHES")
print("=" * 55)

log = """
2024-01-15 ERROR: Connection failed for user alice@mail.com
2024-01-16 INFO: Login successful for user bob@company.org
2024-01-17 ERROR: Timeout for request from 192.168.1.100
2024-01-18 WARNING: High memory usage detected
2024-01-19 ERROR: Database connection lost for diana@test.net
"""

emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w{2,}", log)
print("All emails:", emails)

dates = re.findall(r"\d{4}-\d{2}-\d{2}", log)
print("All dates:", dates)

errors = re.findall(r"\d{4}-\d{2}-\d{2} ERROR: .+", log)
print("Error lines:")
for e in errors:
    print(f"  {e}")

ip_addresses = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log)
print("IP addresses:", ip_addresses)

print("\n" + "=" * 55)
print("SECTION 3: SUBSTITUTION AND CLEANING")
print("=" * 55)

messy = "  Hello,   World!!!   How    are you???  "
clean = re.sub(r"\s+", " ", messy).strip()
clean = re.sub(r"[!?]+", ".", clean)
print(f"Original: '{messy}'")
print(f"Cleaned : '{clean}'")

html_text = "<h1>Hello <b>World</b></h1><p>This is <i>great</i>!</p>"
plain = re.sub(r"<[^>]+>", "", html_text)
print(f"\nHTML stripped: '{plain}'")

phone = "+91 (987) 654-3210"
digits_only = re.sub(r"[^\d]", "", phone)
print(f"Phone digits only: {digits_only}")

print("\n" + "=" * 55)
print("SECTION 4: GROUPS AND NAMED CAPTURES")
print("=" * 55)

date_str = "Meeting on 2024-03-15 at 14:30"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_str)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")

# Named groups (more readable)
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, date_str)
if match:
    print(f"Named — Year: {match.group('year')}, Month: {match.group('month')}")

print("\n" + "=" * 55)
print("SECTION 5: VALIDATION FUNCTIONS")
print("=" * 55)

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_phone_in(phone):
    pattern = r"^(\+91|0)?[6-9]\d{9}$"
    return bool(re.match(pattern, re.sub(r"[\s\-]", "", phone)))

def validate_password(pwd):
    checks = {
        "Min 8 chars": len(pwd) >= 8,
        "Has uppercase": bool(re.search(r"[A-Z]", pwd)),
        "Has lowercase": bool(re.search(r"[a-z]", pwd)),
        "Has digit":     bool(re.search(r"\d", pwd)),
        "Has special":   bool(re.search(r"[!@#$%^&*]", pwd)),
    }
    return checks

# Test
print("Email validation:")
for em in ["nav@mail.com", "bad-email", "user@domain.co.in", "@noname.com"]:
    print(f"  {em:25s} → {'✓' if validate_email(em) else '✗'}")

print("\nPhone validation (India):")
for ph in ["+919876543210", "9876543210", "1234567890", "08765432109"]:
    print(f"  {ph:15s} → {'✓' if validate_phone_in(ph) else '✗'}")

print("\nPassword strength check:")
for pwd in ["abc", "Password1", "Navkiran@2024", "weakpass"]:
    checks = validate_password(pwd)
    passed = sum(checks.values())
    print(f"  '{pwd}': {passed}/5 checks passed")
    for check, result in checks.items():
        print(f"    {'✓' if result else '✗'} {check}")

print("\n" + "=" * 55)
print("SUMMARY")
print("=" * 55)
print("re.search()   → find first match anywhere in string")
print("re.findall()  → list of all matches")
print("re.sub()      → replace matches")
print("re.match()    → match at start of string")
print("()            → capture group")
print("(?P<name>...) → named group")
print("r'pattern'    → always use raw strings for regex")
