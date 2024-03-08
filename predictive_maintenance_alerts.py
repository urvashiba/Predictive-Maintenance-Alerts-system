import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
import re

# Example maintenance logs
data = [
    "Engine noise observed during acceleration",
    "Routine maintenance, oil change",
    "Brake pads replacement after 20,000 miles",
    "Battery replaced after failing to start",
    "Tire wear observed, requires alignment"
]

# Simulate data as a DataFrame
df = pd.DataFrame(data, columns=['MaintenanceLog'])

# Text preprocessing
def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove numbers and punctuation
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    # Stemming
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in tokens]
    return " ".join(stemmed)

df['ProcessedLog'] = df['MaintenanceLog'].apply(clean_text)

# Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['ProcessedLog'])

# Rule-based issue prediction (for demonstration)
# In a real scenario, this could be replaced with a trained model prediction.
def predict_issue(text):
    if 'noise' in text or 'fail' in text or 'wear' in text:
        return 'Potential Issue Detected'
    else:
        return 'No Issue Detected'

df['Prediction'] = df['ProcessedLog'].apply(predict_issue)

# Display the results
print(df[['MaintenanceLog', 'Prediction']])
