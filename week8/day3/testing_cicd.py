# =============================================================================
# WEEK 8 - DAY 3: Testing & CI/CD Pipelines
# Intern: ISHAAN GARG
# Topic: unittest, pytest, GitHub Actions workflow
# =============================================================================

import unittest

print("=" * 60)
print("  WEEK 8 DAY 3: TESTING & CI/CD")
print("  Intern: ISHAAN GARG")
print("=" * 60)

# -----------------------------------------------------------------------
# THE CODE WE'RE TESTING
# -----------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        return self._balance

    @property
    def balance(self):
        return self._balance

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)


def calculate_grade(score):
    if not 0 <= score <= 100:
        raise ValueError(f"Score {score} out of valid range.")
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"


# -----------------------------------------------------------------------
# UNIT TESTS
# -----------------------------------------------------------------------

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Called before EACH test method."""
        self.account = BankAccount("Navkiran", 1000)
        self.other   = BankAccount("Alice", 500)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_deposit_positive(self):
        new_bal = self.account.deposit(500)
        self.assertEqual(new_bal, 1500)
        self.assertEqual(self.account.balance, 1500)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_valid(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(9999)

    def test_transfer(self):
        self.account.transfer(self.other, 200)
        self.assertEqual(self.account.balance, 800)
        self.assertEqual(self.other.balance, 700)

    def test_negative_initial_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("Bad", -100)


class TestGradeCalculator(unittest.TestCase):

    def test_grade_A(self):
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(90), "A")

    def test_grade_B(self):
        self.assertEqual(calculate_grade(85), "B")
        self.assertEqual(calculate_grade(80), "B")

    def test_grade_F(self):
        self.assertEqual(calculate_grade(55), "F")
        self.assertEqual(calculate_grade(0),  "F")

    def test_perfect_score(self):
        self.assertEqual(calculate_grade(100), "A")

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            calculate_grade(105)
        with self.assertRaises(ValueError):
            calculate_grade(-1)


# -----------------------------------------------------------------------
# RUN TESTS
# -----------------------------------------------------------------------

print("\n--- Running Unit Tests ---\n")
loader = unittest.TestLoader()
suite  = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(TestBankAccount))
suite.addTests(loader.loadTestsFromTestCase(TestGradeCalculator))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

# -----------------------------------------------------------------------
# CI/CD CONCEPT
# -----------------------------------------------------------------------

print("\n" + "=" * 60)
print("SECTION 2: CI/CD PIPELINE EXPLAINED")
print("=" * 60)
print("""
CI = Continuous Integration
  → Every push to GitHub automatically runs tests
  → If tests fail, the merge is blocked
  → Everyone's code is always tested

CD = Continuous Deployment
  → If all tests pass, automatically deploy to server
  → No manual deployment steps

GitHub Actions workflow (.github/workflows/ci.yml):

  name: CI Pipeline

  on:
    push:
      branches: [main, develop]
    pull_request:
      branches: [main]

  jobs:
    test:
      runs-on: ubuntu-latest

      steps:
        - name: Checkout code
          uses: actions/checkout@v3

        - name: Set up Python 3.11
          uses: actions/setup-python@v4
          with:
            python-version: '3.11'

        - name: Install dependencies
          run: |
            pip install -r requirements.txt
            pip install pytest pytest-cov

        - name: Run tests
          run: pytest --cov=. --cov-report=xml

        - name: Upload coverage
          uses: codecov/codecov-action@v3
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("unittest.TestCase → base class for tests")
print("setUp()           → runs before each test")
print("assertEqual()     → check expected == actual")
print("assertRaises()    → check exception is raised")
print("CI/CD             → automate testing + deployment")
print("GitHub Actions    → free CI/CD for GitHub repos")
