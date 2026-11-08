import os

import kagglehub as kh
from kagglehub import KaggleDatasetAdapter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# def searching_path():
#     dataset_folder = kh.dataset_download(handle='naserabdullahalam/phishing-email-dataset')
#     print(os.listdir(path=dataset_folder))


def main():
    dataset = kh.dataset_load(adapter=KaggleDatasetAdapter.PANDAS,
                            handle='naserabdullahalam/phishing-email-dataset',
                            path='phishing_email.csv')
    print('\nDataset info:', dataset.head())
    print('\nDataset shape:', dataset.shape)
    print('\nValue counts:')
    print(dataset['label'].value_counts())
    print('\nIs NA:', dataset.isna().sum())
    print('\nDuplicates:', dataset.duplicated().sum())
    
    cleared_dataset = dataset.drop_duplicates(subset='text_combined')
    print('\nCleared dataset shape:', cleared_dataset.shape)
    #print(cleared_dataset[cleared_dataset['label'] == 1].head(3))
    # cleared_dataset = cleared_dataset.sample(n=10000, random_state=42)
    x = cleared_dataset['text_combined']
    y = cleared_dataset['label']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y) 
    print(X_train.shape + y_train.shape)
    print(X_test.shape + y_test.shape)

    vectorizer = TfidfVectorizer(max_features=50000, ngram_range=(1,2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    print("X_train_vec shape:", X_train_vec.shape)
    print("X_test_vec shape:", X_test_vec.shape)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)
    y_pred = model.predict(X_test_vec)
    print(y_pred[:10])
    print(y_test.head(10))

    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    main()
