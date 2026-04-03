# =============================================================================
# WEEK 12 - DAY 1: Technical Interview Preparation
# Intern: ISHAAN GARG
# Topic: DSA fundamentals, common patterns, Python solutions
# =============================================================================

print("=" * 60)
print("  WEEK 12 — CAREER PREP & INTERNSHIP WRAP-UP")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
TECHNICAL INTERVIEW STRUCTURE (typical):
  1. Resume screening
  2. Online assessment (DSA problems — LeetCode style)
  3. Technical phone/video screen (1-2 coding questions)
  4. System design round (senior roles)
  5. HR / behavioural round
""")

print("=" * 60)
print("SECTION 1: TIME & SPACE COMPLEXITY")
print("=" * 60)

print("""
Big O Notation — how performance scales with input size n:

  O(1)       Constant    → dict lookup, array index
  O(log n)   Logarithmic → binary search
  O(n)       Linear      → single loop
  O(n log n) Linearithmic→ merge sort, heap sort
  O(n²)      Quadratic   → nested loops
  O(2ⁿ)      Exponential → recursive fibonacci (naive)

RULE: always try to beat O(n²).

Space complexity = extra memory used by your solution.
  In-place sorting → O(1) space
  Creating a new list → O(n) space
  Recursion stack → O(depth) space
""")

print("=" * 60)
print("SECTION 2: ARRAYS & STRINGS")
print("=" * 60)

# ── Two Sum ──────────────────────────────────────────────────────
def two_sum(nums, target):
    """Find indices of two numbers that add up to target.
    Time: O(n)  Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print("Two Sum:")
print(f"  [2,7,11,15], target=9 → {two_sum([2,7,11,15], 9)}")
print(f"  [3,2,4],     target=6 → {two_sum([3,2,4], 6)}")

# ── Maximum Subarray (Kadane's Algorithm) ─────────────────────────
def max_subarray(nums):
    """Find contiguous subarray with largest sum. Time: O(n)"""
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print("\nMax Subarray (Kadane's):")
print(f"  [-2,1,-3,4,-1,2,1,-5,4] → {max_subarray([-2,1,-3,4,-1,2,1,-5,4])}")

# ── Valid Palindrome ──────────────────────────────────────────────
def is_palindrome(s):
    """Check if string is palindrome (alphanumeric only). Time: O(n)"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print("\nPalindrome Check:")
for s in ["A man a plan a canal Panama", "race a car", "Was it a car or a cat I saw"]:
    print(f"  '{s[:30]}' → {is_palindrome(s)}")

print("\n" + "=" * 60)
print("SECTION 3: HASHMAPS & SETS")
print("=" * 60)

# ── Group Anagrams ────────────────────────────────────────────────
from collections import defaultdict

def group_anagrams(strs):
    """Group words that are anagrams. Time: O(n * k log k)"""
    groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())

words = ["eat","tea","tan","ate","nat","bat"]
print(f"Group anagrams {words}:")
print(f"  → {group_anagrams(words)}")

# ── Longest Consecutive Sequence ──────────────────────────────────
def longest_consecutive(nums):
    """Find length of longest consecutive sequence. Time: O(n)"""
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:  # start of a sequence
            current = n
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

print(f"\nLongest consecutive [100,4,200,1,3,2] → {longest_consecutive([100,4,200,1,3,2])}")

print("\n" + "=" * 60)
print("SECTION 4: LINKED LISTS")
print("=" * 60)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def reverse_list(head):
    """Reverse a linked list in place. Time: O(n) Space: O(1)"""
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def has_cycle(head):
    """Detect cycle using Floyd's two-pointer. Time: O(n) Space: O(1)"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

ll = make_list([1, 2, 3, 4, 5])
print(f"Original list : {to_list(ll)}")
print(f"Reversed list : {to_list(reverse_list(ll))}")

ll2 = make_list([3, 1, 2])
print(f"Has cycle (no): {has_cycle(ll2)}")

print("\n" + "=" * 60)
print("SECTION 5: BINARY SEARCH")
print("=" * 60)

def binary_search(nums, target):
    """Classic binary search. Time: O(log n)"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:   return mid
        elif nums[mid] < target:  left = mid + 1
        else:                     right = mid - 1
    return -1

def search_rotated(nums, target):
    """Search in rotated sorted array. Time: O(log n)"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]: right = mid - 1
            else: left = mid + 1
        else:
            if nums[mid] < target <= nums[right]: left = mid + 1
            else: right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Binary search for 7 in {arr}: index {binary_search(arr, 7)}")
rotated = [4, 5, 6, 7, 0, 1, 2]
print(f"Search 0 in rotated {rotated}: index {search_rotated(rotated, 0)}")

print("\n" + "=" * 60)
print("SECTION 6: SLIDING WINDOW")
print("=" * 60)

def longest_substring_no_repeat(s):
    """Longest substring without repeating characters. Time: O(n)"""
    char_index = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

def max_sum_subarray_k(nums, k):
    """Max sum of subarray of size k. Time: O(n)"""
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

print(f"Longest no-repeat substring 'abcabcbb' → {longest_substring_no_repeat('abcabcbb')}")
print(f"Max sum subarray k=3: [2,1,5,1,3,2] → {max_sum_subarray_k([2,1,5,1,3,2], 3)}")

print("\n" + "=" * 60)
print("SECTION 7: TREES")
print("=" * 60)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def make_bst():
    root = TreeNode(4)
    root.left  = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))
    return root

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

tree = make_bst()
print(f"Inorder traversal (sorted): {inorder(tree)}")
print(f"Max depth: {max_depth(tree)}")

print("\n" + "=" * 60)
print("INTERVIEW TIPS")
print("=" * 60)
print("""
1. Clarify the problem before coding — ask about edge cases
2. State your approach before writing code
3. Start with brute force, then optimize
4. Think out loud — interviewers want to see your process
5. Test your solution with examples and edge cases
6. Know your time/space complexity

Most important patterns to know:
  Two pointers, sliding window, binary search
  Hash map for O(1) lookup
  BFS/DFS for trees and graphs
  Dynamic programming for optimization
""")
