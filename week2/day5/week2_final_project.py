# =============================================================================
# WEEK 2 - DAY 5: Final Project — Personal Learning Dashboard
# Topic: Combine everything from Week 2 into one real project
# Uses: Classes, File I/O, Error Handling, JSON, os, datetime
# =============================================================================

# This project builds a simple CLI Learning Dashboard where you can:
# 1. Add topics you've learned
# 2. View your learning history
# 3. Track your progress
# 4. Save everything to a JSON file (persistent storage)
# 5. Generate a weekly report

import json
import os
import random
from datetime import datetime


# =============================================================================
# CLASS DEFINITIONS
# =============================================================================

class LearningEntry:
    """Represents a single learning entry (topic learned on a day)."""

    def __init__(self, topic, notes, difficulty):
        self.topic = topic
        self.notes = notes
        self.difficulty = difficulty              # easy / medium / hard
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.xp = {"easy": 10, "medium": 20, "hard": 30}.get(difficulty, 10)

    def to_dict(self):
        """Converts entry to a dict so we can save it as JSON."""
        return {
            "topic": self.topic,
            "notes": self.notes,
            "difficulty": self.difficulty,
            "timestamp": self.timestamp,
            "xp": self.xp
        }

    def __str__(self):
        return f"[{self.timestamp}] {self.topic} ({self.difficulty}) +{self.xp}XP"


class LearningDashboard:
    """Main dashboard that manages all learning entries."""

    SAVE_FILE = "navkiran_learning_log.json"

    def __init__(self, intern_name):
        self.intern_name = intern_name
        self.entries = []
        self.total_xp = 0
        self.load_data()

    def add_entry(self, topic, notes="", difficulty="medium"):
        """Add a new learning entry."""
        try:
            if not topic.strip():
                raise ValueError("Topic cannot be empty.")
            if difficulty not in ("easy", "medium", "hard"):
                raise ValueError("Difficulty must be easy, medium, or hard.")

            entry = LearningEntry(topic.strip(), notes.strip(), difficulty)
            self.entries.append(entry)
            self.total_xp += entry.xp
            self.save_data()
            print(f"\n✅ Entry added: {entry}")
            print(f"   Total XP: {self.total_xp}")
            self._check_badge()

        except ValueError as e:
            print(f"❌ Error adding entry: {e}")

    def view_all(self):
        """Display all learning entries."""
        if not self.entries:
            print("\nNo entries yet. Start learning!")
            return

        print(f"\n{'=' * 55}")
        print(f"  {self.intern_name}'s Learning Log")
        print(f"{'=' * 55}")
        for i, entry in enumerate(self.entries, 1):
            print(f"{i:2}. {entry}")
        print(f"\n  Total Entries: {len(self.entries)}")
        print(f"  Total XP: {self.total_xp}")
        print(f"{'=' * 55}")

    def view_by_difficulty(self, difficulty):
        """Filter entries by difficulty."""
        filtered = [e for e in self.entries if e.difficulty == difficulty]
        if not filtered:
            print(f"\nNo '{difficulty}' entries found.")
            return
        print(f"\n--- {difficulty.upper()} entries ({len(filtered)}) ---")
        for entry in filtered:
            print(f"  • {entry}")

    def get_stats(self):
        """Show statistics about learning progress."""
        if not self.entries:
            print("No data yet!")
            return

        topics = [e.topic for e in self.entries]
        difficulties = [e.difficulty for e in self.entries]

        easy_count = difficulties.count("easy")
        medium_count = difficulties.count("medium")
        hard_count = difficulties.count("hard")

        print(f"\n{'=' * 45}")
        print(f"  📊 Statistics for {self.intern_name}")
        print(f"{'=' * 45}")
        print(f"  Total topics learned : {len(self.entries)}")
        print(f"  Total XP earned      : {self.total_xp}")
        print(f"  Easy topics          : {easy_count}")
        print(f"  Medium topics        : {medium_count}")
        print(f"  Hard topics          : {hard_count}")
        print(f"  Current level        : {self._get_level()}")
        print(f"{'=' * 45}")

    def generate_report(self):
        """Generate a text report and save it to a file."""
        if not self.entries:
            print("No entries to generate a report from.")
            return

        filename = f"week2_report_{self.intern_name.replace(' ', '_')}.txt"
        report_lines = [
            f"INTERNSHIP LEARNING REPORT",
            f"Intern: {self.intern_name}",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "=" * 45,
            f"Total Topics: {len(self.entries)}",
            f"Total XP: {self.total_xp}",
            f"Level: {self._get_level()}",
            "=" * 45,
            "TOPICS COVERED:",
            ""
        ]

        for i, entry in enumerate(self.entries, 1):
            report_lines.append(f"{i}. [{entry.difficulty.upper()}] {entry.topic}")
            if entry.notes:
                report_lines.append(f"   Notes: {entry.notes}")
            report_lines.append("")

        report_lines.append("=" * 45)
        report_lines.append("Keep learning. Stay consistent!")

        try:
            with open(filename, "w") as f:
                f.write("\n".join(report_lines))
            print(f"\n📄 Report saved to: {filename}")
        except IOError as e:
            print(f"❌ Could not save report: {e}")

        return filename

    def save_data(self):
        """Save all entries to JSON file."""
        data = {
            "intern": self.intern_name,
            "total_xp": self.total_xp,
            "entries": [e.to_dict() for e in self.entries]
        }
        try:
            with open(self.SAVE_FILE, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save data — {e}")

    def load_data(self):
        """Load entries from JSON file if it exists."""
        if not os.path.exists(self.SAVE_FILE):
            return

        try:
            with open(self.SAVE_FILE, "r") as f:
                data = json.load(f)

            self.total_xp = data.get("total_xp", 0)
            for entry_dict in data.get("entries", []):
                entry = LearningEntry(
                    entry_dict["topic"],
                    entry_dict.get("notes", ""),
                    entry_dict.get("difficulty", "medium")
                )
                entry.timestamp = entry_dict.get("timestamp", entry.timestamp)
                entry.xp = entry_dict.get("xp", entry.xp)
                self.entries.append(entry)

            print(f"📂 Loaded {len(self.entries)} existing entries.")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not load saved data — {e}")

    def _get_level(self):
        """Returns level based on XP."""
        if self.total_xp < 50:
            return "🌱 Beginner"
        elif self.total_xp < 150:
            return "🔥 Learner"
        elif self.total_xp < 300:
            return "⚡ Developer"
        else:
            return "🚀 Pro Intern"

    def _check_badge(self):
        """Print a motivational badge at milestones."""
        badges = {
            1:   "🎉 First entry! The journey begins.",
            5:   "📚 5 topics learned! You're on a roll!",
            10:  "🏆 10 topics! Seriously impressive.",
            50:  "💎 50 XP milestone reached!",
            100: "⚡ 100 XP! You're unstoppable!",
            200: "🚀 200 XP!! LEGEND status incoming.",
        }
        message = badges.get(len(self.entries)) or badges.get(self.total_xp)
        if message:
            print(f"   {message}")


# =============================================================================
# DEMO — Run the dashboard with sample data
# =============================================================================

def run_demo():
    print("=" * 55)
    print("  🎓 ISHAAN GARG — LEARNING DASHBOARD DEMO")
    print("=" * 55)

    # Initialize dashboard
    dashboard = LearningDashboard("Ishaan Garg")

    # Add Week 2 topics
    print("\n--- Adding Week 2 Topics ---")
    dashboard.add_entry("Lists and Tuples", "Ordered data structures in Python", "easy")
    dashboard.add_entry("Dictionaries", "Key-value storage, .get(), comprehensions", "easy")
    dashboard.add_entry("Sets", "Unique values, union/intersection operations", "medium")
    dashboard.add_entry("Functions & Lambdas", "def, return, *args, **kwargs, lambda", "medium")
    dashboard.add_entry("File Handling", "open(), read/write/append, CSV, JSON", "medium")
    dashboard.add_entry("OOP - Classes", "Class, __init__, self, methods", "hard")
    dashboard.add_entry("OOP - Inheritance", "Parent/child classes, super(), isinstance", "hard")
    dashboard.add_entry("Error Handling", "try/except/else/finally, raise, custom exceptions", "hard")
    dashboard.add_entry("Python Modules", "math, random, datetime, os, json", "medium")

    # Test error handling in add_entry
    print("\n--- Testing Validation ---")
    dashboard.add_entry("", "empty topic test")          # should fail
    dashboard.add_entry("Test", difficulty="expert")     # invalid difficulty

    # View all entries
    dashboard.view_all()

    # Filter by difficulty
    dashboard.view_by_difficulty("hard")

    # Stats
    dashboard.get_stats()

    # Generate report
    report_file = dashboard.generate_report()

    # Show saved files
    print("\n--- Files Created ---")
    for fname in [dashboard.SAVE_FILE, report_file]:
        if fname and os.path.exists(fname):
            size = os.path.getsize(fname)
            print(f"  📁 {fname} ({size} bytes)")

    # Clean up demo files
    print("\n--- Cleaning up ---")
    for fname in [dashboard.SAVE_FILE, report_file]:
        if fname and os.path.exists(fname):
            os.remove(fname)
            print(f"  🗑️ Removed: {fname}")

    print("\n✅ Demo complete! The dashboard works end-to-end.")
    print("   In a real project, you'd keep the JSON file and build on it daily.")
    print("\n" + "=" * 55)
    print("  WEEK 2 COMPLETE — Great work, Navkiran! 🎓")
    print("=" * 55)


if __name__ == "__main__":
    run_demo()
