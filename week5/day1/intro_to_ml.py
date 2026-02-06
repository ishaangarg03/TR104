# =============================================================================
# WEEK 5 - DAY 1: Intro to Machine Learning — scikit-learn
# Intern: ISHAAN GARG
# Topic: What is ML, train/test split, first classifier
# =============================================================================

# pip install scikit-learn

from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import pandas as pd

print("=" * 55)
print("SECTION 1: WHAT IS MACHINE LEARNING?")
print("=" * 55)
print("""
Traditional Programming:
  Rules + Data → Output

Machine Learning:
  Data + Output → Rules (learned by the model)

Three main types:
  Supervised   → labeled data (we'll use this today)
  Unsupervised → find patterns in unlabeled data
  Reinforcement → agent learns by trial and reward
""")

print("=" * 55)
print("SECTION 2: LOAD AND EXPLORE DATASET")
print("=" * 55)

iris = load_iris()
X = iris.data       # features (sepal/petal measurements)
y = iris.target     # labels (0=setosa, 1=versicolor, 2=virginica)

df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in y]

print("Shape:", X.shape)
print("Features:", iris.feature_names)
print("Target classes:", iris.target_names)
print("\nFirst 5 rows:\n", df.head())
print("\nClass distribution:\n", df["species"].value_counts())
print("\nStats:\n", df.describe().round(2))

print("\n" + "=" * 55)
print("SECTION 3: TRAIN / TEST SPLIT")
print("=" * 55)

# Split data: 80% train, 20% test
# random_state=42 ensures reproducibility
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training samples : {len(X_train)}")
print(f"Test samples     : {len(X_test)}")
print(f"Train class dist : {np.bincount(y_train)}")
print(f"Test class dist  : {np.bincount(y_test)}")

print("\n" + "=" * 55)
print("SECTION 4: FEATURE SCALING")
print("=" * 55)

# Many ML models need features on same scale
# StandardScaler: (x - mean) / std → mean=0, std=1
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit on train only!
X_test_scaled  = scaler.transform(X_test)         # transform test using train stats

print("Before scaling — mean:", X_train[:, 0].mean().round(2),
      "| std:", X_train[:, 0].std().round(2))
print("After scaling  — mean:", X_train_scaled[:, 0].mean().round(4),
      "| std:", X_train_scaled[:, 0].std().round(4))
print("(mean ≈ 0, std ≈ 1 ✓)")

print("\n" + "=" * 55)
print("SECTION 5: TRAIN A K-NEAREST NEIGHBORS MODEL")
print("=" * 55)

# KNN: classify a point by looking at its K nearest neighbors
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)
print("Model trained!")

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nTest Accuracy: {accuracy * 100:.1f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("(rows = actual, cols = predicted)")

print("\n" + "=" * 55)
print("SECTION 6: PREDICT NEW DATA")
print("=" * 55)

# Imagine a new flower measurement
new_flower = [[5.1, 3.5, 1.4, 0.2]]
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)
probabilities = model.predict_proba(new_flower_scaled)

print(f"New flower measurements: {new_flower[0]}")
print(f"Predicted species: {iris.target_names[prediction[0]]}")
print(f"Confidence: {max(probabilities[0]) * 100:.1f}%")

print("\n" + "=" * 55)
print("SECTION 7: TRY DIFFERENT K VALUES")
print("=" * 55)

for k in [1, 3, 5, 7, 11]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test_scaled))
    print(f"  K={k:2d} → Accuracy: {acc * 100:.1f}%")

print("\n" + "=" * 55)
print("SUMMARY — ML Pipeline Steps")
print("=" * 55)
print("1. Load data")
print("2. Explore (shape, types, distribution)")
print("3. Split into train/test")
print("4. Scale features")
print("5. Train model: model.fit(X_train, y_train)")
print("6. Evaluate: accuracy, confusion matrix, report")
print("7. Predict: model.predict(X_new)")
