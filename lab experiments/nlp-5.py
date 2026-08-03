import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "connection", "connected"]

for word in words:
    print(word, "->", stemmer.stem(word))
