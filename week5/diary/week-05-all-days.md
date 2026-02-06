# WEEK 5 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — Intro to Machine Learning

Today was a big jump — from data analysis to actual machine learning. The core idea clicked: instead of writing rules, you feed the model data and it learns the rules itself.

The train/test split concept is crucial. I was surprised that you must fit the scaler ONLY on training data — fitting on test data would be "data leakage."

KNN is beautifully simple: classify a new point by looking at its K nearest neighbors. Best accuracy at K=5 on the Iris dataset.

**Ran today:** `day1/intro_to_ml.py`

---

## Day 2 — Linear and Logistic Regression

Linear regression finds the best-fit line. The equation `score = 6.2 * hours + 25` is actually meaningful — for every extra study hour, the score goes up by ~6 points.

Logistic regression predicts probabilities (0 to 1) then picks a class. It's not really "regression" in the traditional sense — confusing name, but powerful tool. Achieved 97%+ on breast cancer classification.

**Ran today:** `day2/regression.py`

---

## Day 3 — Decision Trees and Random Forests

Decision trees are the most interpretable ML model — you can literally read the rules it learned (export_text). The overfitting demo was eye-opening: a tree with no max_depth gets 100% training accuracy but much worse test accuracy.

Random Forest fixes overfitting by building 100 trees on random subsets and voting. Feature importance is a bonus — it tells you which columns actually matter.

**Ran today:** `day3/trees_and_forests.py`

---

## Day 4 — Clustering and PCA

Unsupervised learning is different — no labels, just patterns. K-Means clustering groups similar data points automatically. The silhouette score tells you how well-separated the clusters are.

PCA reducing 4 Iris features to 2 while keeping 97% of variance is impressive. I can now visualize high-dimensional data in 2D.

**Ran today:** `day4/clustering_pca.py`

---

## Day 5 — Week 5 Final Project: Model Comparison Pipeline

Built a pipeline that trains 6 different classifiers (KNN, Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, SVM) on the same dataset, evaluates them all, and ranks them in a table.

Gradient Boosting and SVM typically topped the leaderboard. Running cross-validation on all models gives a more reliable comparison than a single test split.

**Ran today:** `day5/week5_final_project.py`
