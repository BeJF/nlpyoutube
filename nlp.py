from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import nltk
#nltk.download("stopwords")

ps = PorterStemmer()

#Initialize lists
comments_list = []
filtered_sentence = []
comments_tokenized = []


def contain_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

# Open the file with comments and store it in a list of string.
with open("comments.txt", "r") as f :
    comments_list=f.read().splitlines()
#print("Comments => \n\n", comments_list, "\n")

# Set a list of stop words. Used to filter the comments. Can add more of common words.
stop_words = set(stopwords.words("english"))
#print("Stop words => \n\n", stop_words, "\n")

# Each comment is tokenized. We have a list of list of words. We filter out the stopwords in the same time.
# => what to do with comments with multiple sentences?
#print("Tokenized sentences => \n") 
for comment in comments_list :
    sentence = word_tokenize(comment)
    #try for stemming but bug
    '''for word in sentence :
        
        word = word.lower()
        #word = ps.stem(word)
        print(word)
        if not word in stop_words and word.isalpha() :
            filtered_sentence.append(ps.stem(word))'''
    filtered_sentence = [w.lower() for w in sentence if not w.lower() in stop_words and w.isalpha()]
    comments_tokenized.append(filtered_sentence)
    #print(filtered_sentence, "\n")

all_words = []

for comment in comments_tokenized :
    for word in comment :
        all_words.append(word)

all_words = nltk.FreqDist(all_words)
#print("\n", all_words.most_common(100))

most_commons = [w[0] for w in all_words.most_common(10)]
print('\n', most_commons)

usefull_comments = []

for comment in comments_list :
    for word in most_commons :
        if contain_word(comment, word) == 1 :
            #print(word)
            #print(comment)
            usefull_comments.append(comment)
            break

#print(usefull_comments)
print(len(comments_list))
print(len(usefull_comments))
