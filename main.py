# ml.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import BaggingClassifier
import joblib
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv(r'/home/muhammad-ahmad-nadeem/Projects/SPAM_HAM_FILTER/spam_ham/spam_ham_dataset.csv')

# Data Cleaning
new_d = pd.DataFrame(data.drop(data.columns[[0, 1]], axis=1))

# Vectorization (this will be used for both training and prediction)
vectorizer = TfidfVectorizer()

# Transform the text data into a numerical format
X = vectorizer.fit_transform(new_d['text'])
y = new_d['label_num']

# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model: BaggingClassifier
bc = BaggingClassifier(n_estimators=30)
bc.fit(x_train, y_train)

# Function to predict email
def predict_email(text):
    # Transform the input text using the same vectorizer
    transformed_text = vectorizer.transform([text])
    
    # Predict using the model
    prediction = bc.predict(transformed_text)
    
    # Return the result as 'Ham' or 'Spam'
    return "Ham" if prediction == 0 else "Spam"
