import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "Natural Language Processing is very interesting."

words = nltk.word_tokenize(text)

tags = nltk.pos_tag(words)

print(tags)
