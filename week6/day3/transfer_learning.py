# =============================================================================
# WEEK 6 - DAY 3: Transfer Learning
# Intern: ISHAAN GARG
# Topic: Reuse pretrained models to solve new problems fast
# =============================================================================

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2

print("=" * 55)
print("SECTION 1: WHAT IS TRANSFER LEARNING?")
print("=" * 55)
print("""
Training a CNN from scratch needs millions of images and hours.
Transfer Learning: take a model already trained on millions of images
(like ImageNet) and reuse its learned features for YOUR task.

Two strategies:
  Feature Extraction → freeze base model, only train new head
  Fine-tuning        → unfreeze some base layers, train everything

Why it works:
  Early layers learn universal features (edges, textures)
  → these transfer to almost any image task
  Later layers learn task-specific features
  → replace these with your own
""")

print("=" * 55)
print("SECTION 2: LOAD PRETRAINED BASE (MobileNetV2)")
print("=" * 55)

base_model = MobileNetV2(
    input_shape=(96, 96, 3),
    include_top=False,          # exclude ImageNet classifier head
    weights="imagenet"
)
base_model.trainable = False    # freeze — don't update during training
print(f"MobileNetV2 loaded")
print(f"Total layers   : {len(base_model.layers)}")
print(f"Trainable params: 0 (frozen)")

print("\n" + "=" * 55)
print("SECTION 3: ADD CUSTOM HEAD")
print("=" * 55)

inputs = keras.Input(shape=(96, 96, 3))
x = base_model(inputs, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.3)(x)
x = layers.Dense(128, activation="relu")(x)
outputs = layers.Dense(2, activation="softmax")(x)     # 2 custom classes

model = keras.Model(inputs, outputs)
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

print("Model architecture (feature extraction mode):")
print(f"  Base model params  : {base_model.count_params():,} (frozen)")
print(f"  Custom head params : {model.count_params() - base_model.count_params():,} (trainable)")
print(f"  Total params       : {model.count_params():,}")
model.summary(line_length=70)

print("\n" + "=" * 55)
print("SECTION 4: SIMULATE TRAINING ON SYNTHETIC DATA")
print("=" * 55)

np.random.seed(42)
n = 200
X_fake = np.random.rand(n, 96, 96, 3).astype("float32")
y_fake = np.random.randint(0, 2, n)

split = int(0.8 * n)
X_tr, X_te = X_fake[:split], X_fake[split:]
y_tr, y_te = y_fake[:split], y_fake[split:]

history = model.fit(X_tr, y_tr, epochs=3, batch_size=16,
                    validation_data=(X_te, y_te), verbose=1)

loss, acc = model.evaluate(X_te, y_te, verbose=0)
print(f"\nTest Accuracy (random data): {acc*100:.1f}%")
print("(~50% expected since data is random — architecture is correct)")

print("\n" + "=" * 55)
print("SECTION 5: FINE-TUNING STRATEGY")
print("=" * 55)
print("""
After feature extraction training converges, unfreeze top base layers:

  base_model.trainable = True

  # Only train the last N layers
  for layer in base_model.layers[:-20]:
      layer.trainable = False

Then recompile with a LOWER learning rate (important!):
  model.compile(optimizer=Adam(1e-5), ...)

And continue training for a few more epochs.

Why lower LR? The base weights are already good — we want small
adjustments, not to destroy what was already learned.
""")

print("=" * 55)
print("SECTION 6: POPULAR PRETRAINED MODELS")
print("=" * 55)
models_table = [
    ("MobileNetV2",  "Small/fast, good for mobile",     3_400_000),
    ("VGG16",        "Simple, widely used baseline",   138_000_000),
    ("ResNet50",     "Skip connections, very popular",  25_600_000),
    ("InceptionV3",  "Efficient multi-scale features",  23_800_000),
    ("EfficientNetB0","State-of-art accuracy/size",      5_300_000),
    ("CLIP",         "Image + text understanding",      88_000_000),
]
print(f"{'Model':20s} | {'Use Case':35s} | {'Params':>12}")
print("-" * 72)
for name, use, params in models_table:
    print(f"{name:20s} | {use:35s} | {params:>12,}")

print("\n" + "=" * 55)
print("SUMMARY")
print("=" * 55)
print("Transfer Learning = reuse pretrained weights for new task")
print("include_top=False = remove original classifier head")
print("base.trainable=False = freeze base (feature extraction)")
print("GlobalAveragePooling = replace Flatten after conv base")
print("Fine-tune with low LR after initial training converges")
