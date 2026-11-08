"""Baseline phishing email classifier: TF-IDF + Logistic Regression.

Usage:
    python src/baseline.py --data data/emails.csv --text-col text --label-col label
"""
import argparse

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="path to the CSV file")
    parser.add_argument("--text-col", default="text")
    parser.add_argument("--label-col", default="label")
    args = parser.parse_args()

    df = pd.read_csv(args.data).dropna(subset=[args.text_col, args.label_col])
    print("Class balance:")
    print(df[args.label_col].value_counts(), "\n")

    X, y = df[args.text_col], df[args.label_col]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    vec = TfidfVectorizer(max_features=50000, ngram_range=(1, 2))
    X_train_v = vec.fit_transform(X_train)
    X_test_v = vec.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_v, y_train)

    print(classification_report(y_test, model.predict(X_test_v)))


if __name__ == "__main__":
    main()
