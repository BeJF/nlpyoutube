from nltk.tokenize import word_tokenize

sentence = "l'avion a beaucoup d'essence"
tokenized = word_tokenize(sentence)
filtered = []
for word in tokenized :
    if word.isalpha() == 0 :
        word = word.split("'")
        word = word[1]
    print(word)
print(tokenized)
