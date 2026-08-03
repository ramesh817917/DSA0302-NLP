import random

tag_dictionary = {
    "I": ["PRP"],
    "eat": ["VB", "NN"],
    "rice": ["NN"],
    "daily": ["RB"],
    "play": ["VB", "NN"],
    "football": ["NN"]
}

sentence = input("Enter sentence: ").split()

print("\nTagged Sentence:")

for word in sentence:
    if word in tag_dictionary:
        tag = random.choice(tag_dictionary[word])
    else:
        tag = "NN"
    print(word, "->", tag)
