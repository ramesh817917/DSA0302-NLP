def plural(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    elif noun.endswith("y") and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"

while True:
    word = input("Enter noun: ")
    print("Plural:", plural(word))

    ch = input("Continue(y/n): ")
    if ch.lower() != 'y':
        break
