# =============================================================================
# WEEK 6 - DAY 2: Convolutional Neural Networks (CNNs) — Image Classification
# Intern: ISHAAN GARG
# =============================================================================

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print("=" * 55)
print("SECTION 1: WHY CNNs FOR IMAGES?")
print("=" * 55)
print("""
A plain Dense network doesn't understand spatial relationships.
CNNs use:
  Conv2D  → detect local patterns (edges, textures, shapes)
  Pooling → reduce spatial size, keep important features
  Flatten → convert to 1D for Dense layers
""")

print("=" * 55)
print("SECTION 2: LOAD MNIST DATASET")
print("=" * 55)

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
print(f"Train shape: {X_train.shape}  →  {X_train.shape[0]} images of 28x28 pixels")
print(f"Test shape : {X_test.shape}")
print(f"Classes    : digits 0-9")

# Normalize and reshape
X_train = X_train.astype("float32") / 255.0
X_test  = X_test.astype("float32") / 255.0
X_train = X_train[..., np.newaxis]   # (60000, 28, 28, 1)
X_test  = X_test[...,  np.newaxis]

print(f"After reshape: {X_train.shape}")

print("\n" + "=" * 55)
print("SECTION 3: BUILD CNN")
print("=" * 55)

model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, kernel_size=(3,3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Conv2D(64, kernel_size=(3,3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])

model.summary()

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\n" + "=" * 55)
print("SECTION 4: TRAIN (subset for speed)")
print("=" * 55)

history = model.fit(
    X_train[:10000], y_train[:10000],
    epochs=5,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)

print("\n" + "=" * 55)
print("SECTION 5: EVALUATE")
print("=" * 55)

loss, acc = model.evaluate(X_test[:2000], y_test[:2000], verbose=0)
print(f"Test Accuracy (subset): {acc*100:.1f}%")

preds = model.predict(X_test[:5], verbose=0)
print("\nPredictions on first 5 test images:")
for i, (pred_probs, actual) in enumerate(zip(preds, y_test[:5])):
    predicted = np.argmax(pred_probs)
    conf = pred_probs[predicted]
    status = "✓" if predicted == actual else "✗"
    print(f"  [{status}] Predicted: {predicted} | Confidence: {conf*100:.1f}% | Actual: {actual}")

print("\n" + "=" * 55)
print("SECTION 6: CNN LAYER CONCEPTS")
print("=" * 55)
print("""
Conv2D(32, (3,3)):
  → Apply 32 different 3x3 filters across the image
  → Each filter detects a different pattern (edge, curve, etc.)

MaxPooling2D(2,2):
  → Take max value from each 2x2 region
  → Reduces spatial size by half, keeps strongest features

Dropout(0.5):
  → Randomly turn off 50% of neurons during training
  → Prevents overfitting — forces network to not rely on any one neuron

Flatten:
  → Convert 2D feature maps to 1D vector for Dense layers

Softmax output:
  → 10 values that sum to 1.0 (probabilities for each digit)
""")

print("=" * 55)
print("SUMMARY")
print("=" * 55)
print("Conv2D      → detect local spatial patterns")
print("MaxPooling  → reduce size, keep strong features")
print("Dropout     → regularization (prevent overfitting)")
print("Flatten     → connect conv layers to dense layers")
print("Softmax     → multi-class probability output")
print("sparse_categorical_crossentropy → loss for integer labels")
