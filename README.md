# Phishing Email Detector

A machine-learning project that classifies emails as spam/phishing or legitimate, and tests how well the model holds up against evasion attempts.

> Status: work in progress. See [PROGRESS.md](PROGRESS.md) for the day-by-day log.

## Goals

1. Build a baseline text classifier (TF-IDF + Logistic Regression). **Done.**
2. Compare it with other models (Naive Bayes, Random Forest, XGBoost).
3. Evaluate with precision, recall, F1 and a confusion matrix.
4. Test robustness: character substitution, "benign" padding text, LLM-generated phishing.
5. Test generalization: train on one data source, test on another.

## Dataset

[Phishing Email Dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) from Kaggle, file `phishing_email.csv`.

- 82,486 emails, 2 columns: `text_combined` (preprocessed email text) and `label`
- `0` = legitimate (e.g. Enron corporate emails), `1` = spam/phishing
- 408 duplicate texts removed, leaving 82,078 emails
- Classes are almost balanced: 52% label 1, 48% label 0

Note: label `1` contains mostly generic spam (ads, pills, etc.), not only targeted phishing. The text is already lowercased and stripped of punctuation.

## Method (baseline)

1. Remove duplicates (by email text).
2. Stratified 80/20 train/test split (`random_state=42`).
3. TF-IDF features: `max_features=50000`, `ngram_range=(1, 2)`. The vectorizer is fitted on the training set only to avoid data leakage.
4. Logistic Regression (`max_iter=1000`).

## Project structure

```
phishing-detector/
├── data/            # dataset notes (data is downloaded automatically)
├── notebooks/       # exploration and experiments
├── src/             # training and evaluation code
├── reports/         # results and figures
├── PROGRESS.md      # learning and progress log
├── requirements.txt
└── README.md
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

The dataset is downloaded automatically with `kagglehub` on the first run and cached locally.

## Results

Test set: 16,416 emails (20% of the deduplicated data).

| Model | Class | Precision | Recall | F1 |
|-------|-------|-----------|--------|----|
| TF-IDF + Logistic Regression | 0 (legitimate) | 0.99 | 0.98 | 0.99 |
| TF-IDF + Logistic Regression | 1 (spam/phishing) | 0.99 | 0.99 | 0.99 |

Overall accuracy: **0.99**.

Confusion matrix (rows = true class, columns = predicted):

|  | Predicted 0 | Predicted 1 |
|---|---|---|
| **True 0** | 7720 | 127 |
| **True 1** | 99 | 8470 |

127 legitimate emails were flagged as spam (false positives) and 99 spam emails were missed (false negatives).

**Caveat:** these scores are measured on data from the same sources as the training set, and the spam class is mostly easy-to-detect generic spam. The model may partly learn source-specific style rather than phishing itself, so the numbers likely overestimate real-world performance. Cross-source and robustness tests are next.

## Roadmap

- [x] Baseline model
- [ ] Error analysis (read misclassified emails)
- [ ] Most informative words (model coefficients)
- [ ] Naive Bayes / Random Forest / XGBoost comparison
- [ ] Cross-source test (train on one file, test on another)
- [ ] Robustness tests against evasion
- [ ] Final write-up