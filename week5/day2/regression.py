# =============================================================================
# WEEK 5 - DAY 2: Linear and Logistic Regression
# Intern: ISHAAN GARG
# =============================================================================

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.datasets import make_regression, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (mean_squared_error, r2_score,
                              accuracy_score, classification_report)
import numpy as np
import pandas as pd

print("=" * 55)
print("SECTION 1: LINEAR REGRESSION")
print("=" * 55)
print("Goal: Predict a continuous number (e.g., house price, score)")

# Synthetic data: study hours → exam score
np.random.seed(42)
hours = np.linspace(1, 10, 80).reshape(-1, 1)
scores = 6 * hours.flatten() + 25 + np.random.normal(0, 5, 80)

X_train, X_test, y_train, y_test = train_test_split(hours, scores, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)

print(f"\nCoefficient (slope): {lr.coef_[0]:.2f}")
print(f"Intercept          : {lr.intercept_:.2f}")
print(f"Equation           : score = {lr.coef_[0]:.2f} * hours + {lr.intercept_:.2f}")

y_pred = lr.predict(X_test)
print(f"\nMSE  : {mean_squared_error(y_test, y_pred):.2f}")
print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
print(f"R²   : {r2_score(y_test, y_pred):.4f}  (1.0 = perfect)")

# Predict for specific hours
for h in [3, 6, 9]:
    pred = lr.predict([[h]])[0]
    print(f"  Study {h}h → predicted score: {pred:.1f}")

print("\n" + "=" * 55)
print("SECTION 2: LOGISTIC REGRESSION (Classification)")
print("=" * 55)
print("Goal: Predict a category (yes/no, spam/not spam)")

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target   # 0=malignant, 1=benign

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

log_reg = LogisticRegression(max_iter=1000, random_state=42)
log_reg.fit(X_train_s, y_train)

y_pred = log_reg.predict(X_test_s)
print(f"\nBreast Cancer Dataset: {X.shape[0]} samples, {X.shape[1]} features")
print(f"Classes: {cancer.target_names}")
print(f"\nAccuracy: {accuracy_score(y_test, y_pred) * 100:.1f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=cancer.target_names))

print("\n" + "=" * 55)
print("SECTION 3: LINEAR vs LOGISTIC — KEY DIFFERENCES")
print("=" * 55)
print("Linear Regression:")
print("  • Output: any continuous number")
print("  • Use case: price prediction, score estimation")
print("  • Metrics: MSE, RMSE, R²")
print("\nLogistic Regression:")
print("  • Output: probability → class label (0 or 1)")
print("  • Use case: spam detection, disease diagnosis")
print("  • Metrics: accuracy, precision, recall, F1")
