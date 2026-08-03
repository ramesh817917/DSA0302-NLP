import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = ["connected", "connecting", "connection", "running", "better"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
