# Progress Log

A short entry after each work session: what I did, what I learned, what's next.

## Day 1
- [x] Chose the project: phishing/spam detector as a first ML project
- [x] Set up the repository structure (README, PROGRESS, `src/`, `data/`, `notebooks/`, `reports/`)
- [x] Learned what TF-IDF is and why it is used for text

**What I learned:**
- TF-IDF turns text into numbers: words that are frequent in one email but rare overall get a high weight.
- `max_features` limits the vocabulary size; `ngram_range=(1, 2)` adds pairs of words such as "click here".

**Problems:**
- Cleaned up packages that were accidentally installed globally; from now on everything goes into a virtual environment.

**Next:**
- Load the dataset and train the first model.

---

## Day 2 
- [x] Loaded the Kaggle dataset directly with `kagglehub` (no manual download)
- [x] Explored the data: 82,486 rows, balanced classes, no missing values, 408 duplicates removed
- [x] Stratified 80/20 train/test split
- [x] TF-IDF (50,000 features, unigrams + bigrams) + Logistic Regression
- [x] Evaluated on the full test set: accuracy 0.99, F1 0.99 for both classes
- [x] First commit and push to GitHub

**What I learned:**
- Why the data is split into train and test, and why `stratify` keeps class proportions equal.
- Fit the vectorizer on the training data only, then only `transform` the test data (otherwise data leaks from test into training).
- How to read precision, recall, F1, support and the confusion matrix.
- Label `1` in this dataset is mostly generic spam, not targeted phishing, so 0.99 is probably too optimistic. The data comes from several sources, which makes a cross-source test important.
- Each script run retrains everything; a notebook or saving the model avoids the wait.

**Problems:**
- zsh needs quotes around `"kagglehub[pandas-datasets]"`.
- A typo in the file name caused a 404, and the interrupted download left a corrupted cache file (checksum error). Fixed by deleting the dataset's cache folder.
- GitHub rejected the push (GH007) because of the private email setting. Fixed by using the GitHub `noreply` address for commits.

**Next:**
- Error analysis: read misclassified emails.
- Show the most informative words from the model.
- Compare with other models and test on a different data source.

---

## Entry template

## Day N (date)
- [ ] what I did

**What I learned:**
-

**Problems:**
-

**Next:**
-