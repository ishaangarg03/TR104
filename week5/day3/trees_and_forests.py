# =============================================================================
# WEEK 5 - DAY 3: Decision Trees and Random Forests
# Intern: ISHAAN GARG
# =============================================================================

from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import pandas as pd

print("=" * 55)
print("SECTION 1: DECISION TREE")
print("=" * 55)
print("""
A Decision Tree asks a series of YES/NO questions about features
to classify data. Like a flowchart!

Example:
  Is petal_length < 2.5?
    YES → Setosa
    NO  → Is petal_width < 1.75?
            YES → Versicolor
            NO  → Virginica
""")

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# max_depth prevents overfitting
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
dt.fit(X_train, y_train)

print("Decision Tree Rules:")
print(export_text(dt, feature_names=list(iris.feature_names)))

y_pred = dt.predict(X_test)
print(f"Decision Tree Accuracy: {accuracy_score(y_test, y_pred) * 100:.1f}%")

print("\n" + "=" * 55)
print("SECTION 2: OVERFITTING DEMO")
print("=" * 55)

for depth in [1, 2, 3, 4, 5, None]:
    dt_d = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt_d.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, dt_d.predict(X_train))
    test_acc  = accuracy_score(y_test,  dt_d.predict(X_test))
    overfit = "← OVERFIT" if train_acc - test_acc > 0.05 else ""
    label = str(depth) if depth else "None (full)"
    print(f"  depth={label:4s} | Train: {train_acc*100:.1f}% | Test: {test_acc*100:.1f}% {overfit}")

print("\n" + "=" * 55)
print("SECTION 3: RANDOM FOREST")
print("=" * 55)
print("""
Random Forest = many Decision Trees trained on random subsets
→ Each tree votes → majority class wins
→ More trees = more robust (less overfitting)
""")

cancer = load_breast_cancer()
X2, y2 = cancer.data, cancer.target
X_tr, X_te, y_tr, y_te = train_test_split(X2, y2, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_tr, y_tr)

y_pred_rf = rf.predict(X_te)
print(f"Random Forest Accuracy: {accuracy_score(y_te, y_pred_rf)*100:.1f}%")
print("\nClassification Report:")
print(classification_report(y_te, y_pred_rf, target_names=cancer.target_names))

print("\n" + "=" * 55)
print("SECTION 4: FEATURE IMPORTANCE")
print("=" * 55)

importances = pd.Series(rf.feature_importances_, index=cancer.feature_names)
top10 = importances.sort_values(ascending=False).head(10)
print("Top 10 Most Important Features:")
for feat, imp in top10.items():
    bar = "█" * int(imp * 100)
    print(f"  {feat[:30]:30s}: {imp:.4f} {bar}")

print("\n" + "=" * 55)
print("SECTION 5: CROSS-VALIDATION")
print("=" * 55)
print("Cross-val splits data into k folds to get reliable accuracy estimate.")

cv_scores = cross_val_score(rf, X2, y2, cv=5, scoring="accuracy")
print(f"5-fold CV scores: {cv_scores.round(3)}")
print(f"Mean: {cv_scores.mean():.3f} | Std: {cv_scores.std():.3f}")

print("\n" + "=" * 55)
print("SUMMARY")
print("=" * 55)
print("Decision Tree  → interpretable, can overfit")
print("Random Forest  → ensemble of trees, more accurate")
print("max_depth      → controls overfitting")
print("Feature import → tells which features matter most")
print("Cross-val      → more reliable accuracy estimate")
