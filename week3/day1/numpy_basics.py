# =============================================================================
# WEEK 3 - DAY 1: NumPy Basics
# Intern: ISHAAN GARG
# Topic: Numerical computing with NumPy arrays
# =============================================================================

# Install if needed: pip install numpy

import numpy as np

print("=" * 50)
print("SECTION 1: CREATING ARRAYS")
print("=" * 50)

# From a list
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)
print("Type:", type(arr))
print("dtype:", arr.dtype)

# 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Matrix:\n", matrix)
print("Shape:", matrix.shape)   # (rows, cols)
print("Size:", matrix.size)     # total elements
print("ndim:", matrix.ndim)     # number of dimensions

# Special arrays
print("\nZeros:\n", np.zeros((3, 3)))
print("Ones:\n", np.ones((2, 4)))
print("Identity:\n", np.eye(3))
print("Range:", np.arange(0, 10, 2))        # like range() but numpy
print("Linspace:", np.linspace(0, 1, 5))    # 5 evenly spaced numbers from 0-1

print("\n" + "=" * 50)
print("SECTION 2: ARRAY OPERATIONS")
print("=" * 50)

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Element-wise operations (this is what makes NumPy powerful vs plain lists)
print("a + b:", a + b)
print("a * b:", a * b)
print("a ** 2:", a ** 2)
print("b / a:", b / a)

# Scalar operations
print("a + 100:", a + 100)
print("a * 5:", a * 5)

print("\n" + "=" * 50)
print("SECTION 3: INDEXING AND SLICING")
print("=" * 50)

arr2d = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])

print("Full matrix:\n", arr2d)
print("Row 0:", arr2d[0])
print("Element [1][2]:", arr2d[1, 2])
print("Column 1:", arr2d[:, 1])
print("Sub-matrix (rows 0-1, cols 0-1):\n", arr2d[0:2, 0:2])

# Boolean indexing
nums = np.array([5, 12, 3, 18, 7, 25, 1])
print("\nOriginal:", nums)
print("Greater than 10:", nums[nums > 10])

print("\n" + "=" * 50)
print("SECTION 4: MATH AND STATISTICS")
print("=" * 50)

data = np.array([23, 45, 12, 67, 34, 89, 56, 22, 41, 78])
print("Data:", data)
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", round(np.std(data), 2))
print("Min:", np.min(data), "| Max:", np.max(data))
print("Sorted:", np.sort(data))

# Axis operations on 2D
scores = np.array([[85, 90, 78],
                   [92, 88, 76],
                   [70, 95, 83]])
print("\nScores matrix:\n", scores)
print("Row averages (per student):", np.mean(scores, axis=1))
print("Column averages (per subject):", np.mean(scores, axis=0))

print("\n" + "=" * 50)
print("SECTION 5: RESHAPING AND STACKING")
print("=" * 50)

flat = np.arange(1, 13)
print("Flat array:", flat)
reshaped = flat.reshape(3, 4)
print("Reshaped to 3x4:\n", reshaped)

# Stack arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("\nVstack:\n", np.vstack([x, y]))
print("Hstack:", np.hstack([x, y]))

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("np.array()     → create array")
print("arr.shape      → dimensions")
print("arr[row, col]  → indexing")
print("arr[arr > x]   → boolean indexing")
print("np.mean/std    → statistics")
print("arr.reshape()  → change shape")
