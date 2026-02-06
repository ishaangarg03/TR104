# =============================================================================
# WEEK 6 - DAY 1: Deep Learning Intro — Neural Networks with Keras
# Intern: ISHAAN GARG
# Topic: What is a neural network, layers, activation functions, training
# =============================================================================

# pip install tensorflow

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("=" * 55)
print("SECTION 1: WHAT IS A NEURAL NETWORK?")
print("=" * 55)
print(f"""
A neural network is inspired by the human brain.
It consists of layers of "neurons" (nodes).

Input Layer  → receives raw features
Hidden Layers → learn complex patterns
Output Layer  → final prediction

Each neuron:
  1. Receives inputs
  2. Multiplies by weights
  3. Adds a bias
  4. Applies an activation function
  
TensorFlow version: {tf.__version__}
""")

print("=" * 55)
print("SECTION 2: YOUR FIRST NEURAL NETWORK")
print("=" * 55)

# Dataset
cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# Build model
model = keras.Sequential([
    layers.Input(shape=(X_train_s.shape[1],)),   # input layer
    layers.Dense(64, activation="relu"),          # hidden layer 1
    layers.Dense(32, activation="relu"),          # hidden layer 2
    layers.Dense(1,  activation="sigmoid")        # output (binary)
])

model.summary()

print("\n" + "=" * 55)
print("SECTION 3: ACTIVATION FUNCTIONS EXPLAINED")
print("=" * 55)
print("""
ReLU (Rectified Linear Unit):
  f(x) = max(0, x)
  Most popular for hidden layers — fast, avoids vanishing gradient.

Sigmoid:
  f(x) = 1 / (1 + e^-x)  → output between 0 and 1
  Use for binary classification output.

Softmax:
  Converts raw scores to probabilities that sum to 1.
  Use for multi-class classification output.

Tanh:
  f(x) = (e^x - e^-x) / (e^x + e^-x) → output between -1 and 1
  Sometimes used in recurrent networks.
""")

print("=" * 55)
print("SECTION 4: COMPILE AND TRAIN")
print("=" * 55)

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    X_train_s, y_train,
    epochs=30,
    batch_size=32,
    validation_split=0.2,
    verbose=0
)

print("Training complete!")
final_train_acc = history.history["accuracy"][-1]
final_val_acc   = history.history["val_accuracy"][-1]
print(f"Final Train Accuracy     : {final_train_acc*100:.1f}%")
print(f"Final Validation Accuracy: {final_val_acc*100:.1f}%")

print("\n" + "=" * 55)
print("SECTION 5: EVALUATE ON TEST SET")
print("=" * 55)

loss, accuracy = model.evaluate(X_test_s, y_test, verbose=0)
print(f"Test Loss    : {loss:.4f}")
print(f"Test Accuracy: {accuracy*100:.1f}%")

# Predict probabilities and classes
probs = model.predict(X_test_s[:5], verbose=0).flatten()
preds = (probs > 0.5).astype(int)
print("\nSample predictions (first 5):")
for i, (prob, pred, actual) in enumerate(zip(probs, preds, y_test[:5])):
    status = "✓" if pred == actual else "✗"
    label = cancer.target_names[pred]
    print(f"  [{status}] Predicted: {label:9s} | Prob: {prob:.3f} | Actual: {cancer.target_names[actual]}")

print("\n" + "=" * 55)
print("SECTION 6: TRAINING HISTORY ANALYSIS")
print("=" * 55)

epochs = range(1, len(history.history["accuracy"]) + 1)
train_acc_list = history.history["accuracy"]
val_acc_list   = history.history["val_accuracy"]
train_loss_list = history.history["loss"]
val_loss_list   = history.history["val_loss"]

print(f"\n{'Epoch':>5} | {'Train Acc':>10} | {'Val Acc':>10} | {'Train Loss':>10} | {'Val Loss':>10}")
print("-" * 58)
for e in [1, 5, 10, 15, 20, 25, 30]:
    i = e - 1
    print(f"{e:>5} | {train_acc_list[i]*100:>9.1f}% | {val_acc_list[i]*100:>9.1f}% | {train_loss_list[i]:>10.4f} | {val_loss_list[i]:>10.4f}")

print("\n" + "=" * 55)
print("SUMMARY — Key Concepts")
print("=" * 55)
print("Dense layer      → fully connected layer")
print("ReLU             → activation for hidden layers")
print("Sigmoid          → activation for binary output")
print("binary_crossentropy → loss for binary classification")
print("adam             → popular adaptive optimizer")
print("epochs           → how many times to loop through data")
print("batch_size       → samples processed at once")
print("validation_split → portion of train data for validation")
