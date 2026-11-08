# Phishing Email Detector

A machine-learning project that classifies emails as phishing or legitimate, and tests how well the model holds up against evasion attempts.

> Status: work in progress. See [PROGRESS.md](PROGRESS.md) for the day-by-day log.

## Goals

1. Build a baseline text classifier (TF-IDF + Logistic Regression).
2. Compare it with stronger models (Random Forest, XGBoost).
3. Evaluate with precision, recall, F1 and a confusion matrix.
4. Test robustness: character substitution, "benign" padding text, LLM-generated phishing.

## Project structure

```
phishing-detector/
├── data/            # datasets (not committed, see data/README.md)
├── notebooks/       # exploration and experiments
├── src/             # reusable code (training, evaluation)
├── reports/         # results and figures
├── PROGRESS.md      # learning and progress log
├── requirements.txt
└── README.md
```

## Quick start

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
# put the dataset into data/ (see data/README.md)
python src/baseline.py --data data/emails.csv --text-col text --label-col label
```

## Results

| Model | Precision | Recall | F1 |
|-------|-----------|--------|----|
| TF-IDF + Logistic Regression | TBD | TBD | TBD |

## Roadmap

- [ ] Baseline model
- [ ] Confusion matrix and error analysis
- [ ] Random Forest / XGBoost comparison
- [ ] Robustness tests against evasion
- [ ] Final write-up
