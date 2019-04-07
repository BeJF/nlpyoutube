from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import nltk
#nltk.download("punkt")

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


def list_words(sentences):
    words = []
    for sentence in sentences :
        for word in sentence :
            words.append(word)
    return (words)

all_words = list_words(comments_tokenized)
distribution = nltk.FreqDist(all_words)
print("\n", distribution.most_common(100))

most_commons = [w[0] for w in distribution.most_common(10)]
#print('\n', most_commons)

usefull_comments = []

#make a general function of that

def find_comments(include, exclude, comments) :
    usefull_comments = []
    for comment in comments :
        if all(inc in comment for inc in include):
            if all(exc not in comment for exc in exclude):
                usefull_comments.append(comment)
    return (usefull_comments)

'''for comment in comments_tokenized :
	if "camera" in comment and "oneplus" in comment:
		usefull_comments.append(comment)
	for word in most_commons :
		if word in comment :
			usefull_comments.append(comment)
			break'''
'''for comment in comments_list :
    for word in most_commons :
        #if contain_word(comment, word) == 1 :
        if contain_word(comment, "camera") == 1 and contain_word(comment, "0:57") == 0:
			#print(word)
            #print(comment)
            usefull_comments.append(comment)
            break'''

part_words = []

for comment in usefull_comments :
	for word in comment :
		part_words.append(word)

#print(part_words)
part_words = nltk.FreqDist(part_words)
print("\n", part_words.most_common(100))

usefull_comments = find_comments(["camera"], ["oneplus"], comments_tokenized)

print(usefull_comments)
print(len(comments_list))
print(len(usefull_comments))
