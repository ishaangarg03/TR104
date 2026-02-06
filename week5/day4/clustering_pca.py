# =============================================================================
# WEEK 5 - DAY 4: Unsupervised Learning — Clustering & PCA
# Intern: ISHAAN GARG
# =============================================================================

from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs, load_iris
from sklearn.metrics import silhouette_score
import numpy as np
import pandas as pd

print("=" * 55)
print("SECTION 1: K-MEANS CLUSTERING")
print("=" * 55)
print("""
Unsupervised learning: No labels — find patterns in raw data.
K-Means groups data into K clusters by minimizing distance
between points and their cluster center (centroid).
""")

np.random.seed(42)
X, true_labels = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=42)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X_scaled)
labels = kmeans.labels_

print(f"Cluster sizes: {np.bincount(labels)}")
print(f"Inertia (lower = tighter clusters): {kmeans.inertia_:.2f}")
print(f"Silhouette Score (higher = better, max=1): {silhouette_score(X_scaled, labels):.3f}")

print("\n" + "=" * 55)
print("SECTION 2: ELBOW METHOD — CHOOSING K")
print("=" * 55)
print("Run K-Means with different K and look for the 'elbow' in inertia.")

inertias = []
sil_scores = []
k_range = range(2, 9)

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_scaled, km.labels_))

print(f"\n{'K':>3} | {'Inertia':>10} | {'Silhouette':>10}")
print("-" * 30)
for k, inertia, sil in zip(k_range, inertias, sil_scores):
    print(f"{k:>3} | {inertia:>10.1f} | {sil:>10.3f}")

best_k = list(k_range)[np.argmax(sil_scores)]
print(f"\nBest K by silhouette score: {best_k}")

print("\n" + "=" * 55)
print("SECTION 3: PCA — DIMENSIONALITY REDUCTION")
print("=" * 55)
print("""
PCA (Principal Component Analysis) reduces many features to fewer
while preserving as much variance (information) as possible.
Use case: visualize high-dim data, speed up training.
""")

iris = load_iris()
X_iris = iris.data    # 4 features
y_iris = iris.target

scaler2 = StandardScaler()
X_iris_scaled = scaler2.fit_transform(X_iris)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_iris_scaled)

print(f"Original shape: {X_iris.shape}")
print(f"After PCA shape: {X_pca.shape}")
print(f"\nVariance explained by each component:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var*100:.1f}%")
print(f"Total variance retained: {sum(pca.explained_variance_ratio_)*100:.1f}%")

df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["species"] = [iris.target_names[i] for i in y_iris]
print("\nPCA DataFrame sample:\n", df_pca.head())

print("\n" + "=" * 55)
print("SECTION 4: DBSCAN — DENSITY BASED CLUSTERING")
print("=" * 55)
print("""
DBSCAN doesn't need K specified. It finds clusters based on density.
Points in sparse areas become noise (outliers).
""")

dbscan = DBSCAN(eps=0.5, min_samples=5)
db_labels = dbscan.fit_predict(X_scaled)

n_clusters = len(set(db_labels)) - (1 if -1 in db_labels else 0)
n_noise = list(db_labels).count(-1)
print(f"Clusters found: {n_clusters}")
print(f"Noise points  : {n_noise}")
print(f"Cluster dist  : {np.bincount(db_labels[db_labels >= 0])}")

print("\n" + "=" * 55)
print("SUMMARY")
print("=" * 55)
print("K-Means    → partition into K clusters")
print("Elbow/Sil  → choose best K")
print("PCA        → reduce features, keep variance")
print("DBSCAN     → density clustering, auto finds clusters")
