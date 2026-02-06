# WEEK 6 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — Neural Networks with Keras

First taste of deep learning! Building a neural network felt surprisingly approachable with Keras — it's just stacking layers. The `model.summary()` showing all parameters made it concrete.

Key insight: you MUST scale features before a neural network. Unscaled inputs cause training to diverge.

**Ran today:** `day1/neural_network_intro.py`

---

## Day 2 — CNNs for Image Classification

CNNs blew my mind. The convolution operation is elegant — a filter slides over the image detecting patterns. MaxPooling discards redundant info and keeps only the strongest signals. Got ~98%+ on MNIST digit recognition in just 5 epochs.

**Ran today:** `day2/cnn_image_classification.py`

---

## Day 3 — Transfer Learning

Why train from scratch when MobileNetV2 already knows how to see? Freezing the base and just training a custom head is fast and effective. The concept of "feature extraction vs fine-tuning" is a core engineering decision in real AI projects.

**Ran today:** `day3/transfer_learning.py`

---

## Day 4 — NLP Basics

Text is just data in a different form. Bag of Words and TF-IDF turn words into numbers. TF-IDF is smarter because it penalizes common words. Built a spam detector with Naive Bayes + TF-IDF that worked on real test cases.

**Ran today:** `day4/nlp_basics.py`

---

## Day 5 — Week 6 Final Project: Sentiment Analyzer

Built a 3-class sentiment analyzer (positive/neutral/negative) on product reviews. The Pipeline combining TF-IDF + Logistic Regression is clean and easy to deploy. The interactive prediction loop makes it feel like a real product.

**Ran today:** `day5/week6_final_project.py`
