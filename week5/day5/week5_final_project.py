# =============================================================================
# WEEK 5 - DAY 5: Final Project — ML Model Comparison Pipeline
# Intern: ISHAAN GARG
# Topic: Compare multiple classifiers on a real dataset
# =============================================================================

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, classification_report
import numpy as np
import pandas as pd
from datetime import datetime

print("=" * 60)
print("  ISHAAN GARG — ML MODEL COMPARISON PIPELINE")
print("=" * 60)

# Load data
data = load_breast_cancer()
X, y = data.data, data.target
feature_names = data.feature_names
class_names = data.target_names

print(f"\nDataset: Breast Cancer Wisconsin")
print(f"Samples: {X.shape[0]} | Features: {X.shape[1]}")
print(f"Classes: {class_names} | Distribution: {np.bincount(y)}")

# Split and scale
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
scaler = StandardScaler()
X_tr_s = scaler.fit_transform(X_train)
X_te_s = scaler.transform(X_test)

# Define models
models = {
    "KNN (k=5)":           KNeighborsClassifier(n_neighbors=5),
    "Logistic Regression": LogisticRegression(max_iter=2000, random_state=42),
    "Decision Tree":       DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting":   GradientBoostingClassifier(n_estimators=100, random_state=42),
    "SVM":                 SVC(kernel="rbf", probability=True, random_state=42),
}

# Train and evaluate all
results = []
print("\n--- Training and Evaluating Models ---")
for name, model in models.items():
    model.fit(X_tr_s, y_train)
    y_pred = model.predict(X_te_s)
    test_acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")
    cv = cross_val_score(model, scaler.transform(X), y, cv=5, scoring="accuracy")
    results.append({
        "Model":        name,
        "Test Acc (%)": round(test_acc * 100, 2),
        "F1 Score":     round(f1, 4),
        "CV Mean (%)":  round(cv.mean() * 100, 2),
        "CV Std":       round(cv.std(), 4),
    })
    print(f"  ✓ {name}")

# Results table
df_results = pd.DataFrame(results).sort_values("Test Acc (%)", ascending=False)
df_results = df_results.reset_index(drop=True)
df_results.index += 1
print("\n" + "=" * 60)
print("RESULTS COMPARISON TABLE")
print("=" * 60)
print(df_results.to_string())

# Best model detail
best_name = df_results.iloc[0]["Model"]
best_model = models[best_name]
best_pred = best_model.predict(X_te_s)
print(f"\n{'=' * 60}")
print(f"BEST MODEL: {best_name}")
print(f"{'=' * 60}")
print(classification_report(y_test, best_pred, target_names=class_names))

# Feature importance (if Random Forest)
if "Random Forest" in models:
    rf = models["Random Forest"]
    top5 = pd.Series(rf.feature_importances_, index=feature_names).sort_values(ascending=False).head(5)
    print("Top 5 Important Features (Random Forest):")
    for feat, imp in top5.items():
        print(f"  {feat[:35]:35s}: {imp:.4f}")

# Save report
report = f"""
ML MODEL COMPARISON REPORT
Intern: ISHAAN GARG
Dataset: Breast Cancer Wisconsin
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
{'='*55}
{df_results.to_string()}

Best Model: {best_name} ({df_results.iloc[0]['Test Acc (%)']}%)
"""
with open("ml_report.txt", "w") as f:
    f.write(report)
print("\nReport saved: ml_report.txt")

import os; os.remove("ml_report.txt")
print("\n✅ Week 5 Complete! Great ML work, Navkiran!")
print("=" * 60)
